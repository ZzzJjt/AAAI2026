import json
import torch
import csv
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForLanguageModeling, AutoConfig
from datasets import Dataset
from torch.utils.data import DataLoader
from peft import LoraConfig, get_peft_model
from accelerate import Accelerator
from torch.optim import AdamW
from pathlib import Path  # ✅ 添加这一行
# ========== 1. 初始化 Accelerate ==========
accelerator = Accelerator(
    mixed_precision="bf16",  # 如果你不是 A100 就用 bf16
    gradient_accumulation_steps=2
)

# ========== 2. 加载本地模型与分词器 ==========
# 替换模型路径为 Mistral 的路径
model_path = "/root/AAAI2026/AlignmentGuideFineTuning/Mistral-7B-Instruct-v0.3"

# 显式禁用 huggingface hub 下载（关键）
tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True,
    local_files_only=True
)

# ✅ 加这一句：使用 eos_token 作为 pad_token
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    use_cache=False,
    local_files_only=True
)

model.gradient_checkpointing_enable()
# ========== 3. 配置 LoRA ==========
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],  # 如果报错可以改成 ["q_proj", "k_proj", "v_proj", "o_proj"]
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
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
    return tokenizer(example["text"], truncation=True, max_length=1024)

tokenized_dataset = dataset.map(tokenize, batched=False, remove_columns=["text"])

# ========== 6. 构建 Dataloader ==========
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
train_loader = DataLoader(tokenized_dataset, batch_size=1, shuffle=True, collate_fn=data_collator)

# ========== 7. 优化器 ==========
optimizer = AdamW(model.parameters(), lr=5e-5)

# ========== 8. 加速器准备 ==========
model, optimizer, train_loader = accelerator.prepare(model, optimizer, train_loader)

# ========== 9. 开始训练 ==========
log_path = "logs/loss_log_mistral.csv"
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
    model_dir = "./finetuned_mistral_7b_instruct"
    unwrapped_model = accelerator.unwrap_model(model)
    state_dict = accelerator.get_state_dict(unwrapped_model)
    unwrapped_model.save_pretrained(model_dir, state_dict=state_dict, safe_serialization=True)
    tokenizer.save_pretrained(model_dir)
    accelerator.print(f"✅ Model saved to {model_dir}")