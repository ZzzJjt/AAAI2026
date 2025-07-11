import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

import json
import torch
import csv
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForLanguageModeling
from datasets import Dataset
from torch.utils.data import DataLoader
from peft import LoraConfig, get_peft_model
from accelerate import Accelerator
from transformers import BitsAndBytesConfig
import bitsandbytes as bnb  # ✅ 使用 bnb 优化器

# ========== 1. 初始化 Accelerate ==========
accelerator = Accelerator(
    mixed_precision=None,
    gradient_accumulation_steps=64  # ✅ 单卡建议保守些
)
accelerator.scaler = None  # ✅ 完全禁用 FP16 scaler

# ========== 2. 加载本地 Gemma 模型与分词器 ==========
model_path = "/root/AAAI2026/AlignmentGuideFineTuning/gemma-7b"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, local_files_only=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
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
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # 保守设置
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
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize, batched=False, remove_columns=["text"])

# ========== 6. 构建 Dataloader ==========
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
train_loader = DataLoader(tokenized_dataset, batch_size=1, shuffle=True, collate_fn=data_collator)

# ========== 7. 使用 bitsandbytes 的优化器 ==========
optimizer = bnb.optim.PagedAdamW(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=5e-5
)

# ========== 8. 加速器准备 ==========
model, optimizer, train_loader = accelerator.prepare(model, optimizer, train_loader)

# ========== 9. 开始训练 ==========
log_path = "logs/loss_log_gemma.csv"
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
    model_dir = "./finetuned_gemma_7b"
    unwrapped_model = accelerator.unwrap_model(model)
    state_dict = accelerator.get_state_dict(unwrapped_model)
    unwrapped_model.save_pretrained(model_dir, state_dict=state_dict, safe_serialization=True)
    tokenizer.save_pretrained(model_dir)
    accelerator.print(f"✅ Model saved to {model_dir}")

# ========== 11. 简单测试 ==========
inputs = tokenizer("Hello world!", return_tensors="pt").to(model.device)
outputs = model(**inputs)
print(outputs.logits.shape)