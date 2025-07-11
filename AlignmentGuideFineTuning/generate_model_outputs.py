import os
import json
import sys
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
sys.stdout.reconfigure(line_buffering=True)  # ✅ 插在这里
# ====== 配置 ======
base_path = "/root/AAAI2026/AlignmentGuideFineTuning"
data_path = os.path.join(base_path, "finetune_data_poi.jsonl")
output_dir = base_path
max_length = 512

# ====== 模型映射表 ======
model_pairs = {
    "gemma": ("gemma-7b", "finetuned_gemma_7b"),
    "mistral": ("Mistral-7B-Instruct-v0.3", "finetuned_mistral_7b_instruct"),
    "internlm2": ("InternLM2-7B-Chat", "finetuned_internlm2_7b"),
    "qwen2.5": ("Qwen2.5-7B", "finetuned_qwen2.5_7b"),
    "deepseek": ("deepseek-llm-7b-chat", "finetuned_deepseek_7b_chat"),
}

# ====== 加载数据 ======
with open(data_path, "r") as f:
    prompts = [json.loads(line.strip()) for line in f]

# ====== 推理函数 ======
def generate_response(model, tokenizer, prompt_text):
    inputs = tokenizer(prompt_text, return_tensors="pt").to("cuda")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_length,
        do_sample=False,
        temperature=0.7,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# ====== 按阶段生成（节省显存） ======
for stage in ["tuned", "orig"]:  # orig = 原始模型；tuned = 微调模型
    for model_name, (orig_path, tuned_path) in model_pairs.items():
        print(f"\n🔁 Stage: {stage.upper()}, Model: {model_name}")

        model_path = os.path.join(base_path, orig_path if stage == "orig" else tuned_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            torch_dtype=torch.float16
        ).to("cuda")
        model.eval()

        for i, item in tqdm(enumerate(prompts, 1), total=len(prompts)):
            idx = f"{i:04d}"  # 用四位数编号，避免 1, 10, 100 混乱
            intent = item["intent"].strip()
            prompt_text = item["prompt"].strip()
            input_text = f"{intent}\n{prompt_text}"

            output_name = f"Answer{idx}_POI_{'finetuned_' if stage == 'tuned' else ''}{model_name}.md"
            output_path = os.path.join(output_dir, output_name)

            # ⛔ 已存在则跳过
            if os.path.exists(output_path):
                continue

            output = generate_response(model, tokenizer, input_text)

            with open(output_path, "w") as f:
                f.write(f"### Intent:\n{intent}\n\n### Prompt:\n{prompt_text}\n\n### Generated Code:\n{output}\n")

         # 清理显存
        del model
        torch.cuda.empty_cache()

# ====== 移动所有生成的 .md 文件到 modeloutputs 文件夹 ======
import shutil

model_output_dir = os.path.join(base_path, "modeloutputs")
os.makedirs(model_output_dir, exist_ok=True)

for filename in os.listdir(base_path):
    if filename.startswith("Answer") and filename.endswith(".md"):
        src_path = os.path.join(base_path, filename)
        dst_path = os.path.join(model_output_dir, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")

print("\n✅ All .md files generated and moved to modeloutputs/")