import json
import torch
import csv
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForLanguageModeling
from datasets import Dataset
from torch.utils.data import DataLoader
from peft import LoraConfig, get_peft_model
from accelerate import Accelerator
from torch.optim import AdamW

# ========== 1. 初始化 Accelerate ==========
accelerator = Accelerator(
    mixed_precision="bf16",  # 对 A10 GPU 更友好
    gradient_accumulation_steps=16
)

# ========== 2. 加载本地模型与分词器 ==========
model_path = "/root/AAAI2026/AlignmentGuideFineTuning/InternLM2-7B-Chat"

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True,
    local_files_only=True
)
tokenizer.padding_side = "right"
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    use_cache=False,
    local_files_only=True
)
model.gradient_checkpointing_enable()
model.config.use_cache = False
model.config.pad_token_id = tokenizer.pad_token_id

# ========== 3. 配置 LoRA ==========
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["wqkv", "wo"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    modules_to_save=["lm_head"]
)
model = get_peft_model(model, lora_config)

# ========== 4. 加载 POI 数据 ==========
with open("finetune_data_poi.jsonl", "r") as f:
    raw_data = [json.loads(line) for line in f]

examples = [{
    "text": ex["intent"].replace("**Intent Summary:**", "").strip() +
            "\n" + ex["prompt"].strip() +
            "\n" + ex["completion"].strip()
} for ex in raw_data]

dataset = Dataset.from_list(examples)

# ========== 5. 分词 ==========
def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=256)

tokenized_dataset = dataset.map(tokenize, batched=False, remove_columns=["text"])

# ========== 6. 构建 Dataloader ==========
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
train_loader = DataLoader(tokenized_dataset, batch_size=1, shuffle=True, collate_fn=data_collator)

# ========== 7. 优化器 ==========
optimizer = AdamW(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=5e-5
)

# ========== 8. 加速器准备 ==========
model, optimizer, train_loader = accelerator.prepare(model, optimizer, train_loader)

# ========== 9. 开始训练 ==========
log_path = "logs/loss_log_internlm2.csv"
os.makedirs("logs", exist_ok=True)

if accelerator.is_main_process:
    with open(log_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["epoch", "step", "loss"])

model.train()
num_epochs = 3
for epoch in range(num_epochs):
    for step, batch in enumerate(train_loader):
        outputs = model(**batch)
        loss = outputs.loss
        accelerator.backward(loss)

        if (step + 1) % accelerator.gradient_accumulation_steps == 0:
            optimizer.step()
            optimizer.zero_grad()

        if step % 50 == 0:
            accelerator.print(f"Epoch {epoch}, Step {step}, Loss = {loss.item():.4f}")
            if accelerator.is_main_process:
                with open(log_path, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([epoch, step, round(loss.item(), 6)])

# ========== 10. 保存权重 ==========
accelerator.wait_for_everyone()
if accelerator.is_main_process:
    model_dir = "./finetuned_internlm2_7b"
    unwrapped_model = accelerator.unwrap_model(model)
    state_dict = accelerator.get_state_dict(unwrapped_model)
    unwrapped_model.save_pretrained(model_dir, state_dict=state_dict, safe_serialization=True)
    tokenizer.save_pretrained(model_dir)
    accelerator.print(f"✅ Model saved to {model_dir}")

# ========== 11. 简单测试 ==========
inputs = tokenizer("Hello world!", return_tensors="pt").to(model.device)
outputs = model(**inputs)
print(outputs.logits.shape)