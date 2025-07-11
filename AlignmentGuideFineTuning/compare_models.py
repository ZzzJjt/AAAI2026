import os
import json
import re
import pandas as pd
import sacrebleu

# ========================
# 配置路径与模型映射
# ========================
base_path = "/root/AAAI2026/AlignmentGuideFineTuning"
model_output_dir = os.path.join(base_path, "modeloutputs")
prompt_file = os.path.join(base_path, "finetune_data_poi.jsonl")

model_pairs = {
    "deepseek": ("deepseek-llm-7b-chat", "finetuned_deepseek_7b_chat"),
    "qwen2.5": ("Qwen2.5-7B", "finetuned_qwen2.5_7b"),
    "internlm2": ("InternLM2-7B-Chat", "finetuned_internlm2_7b"),
    "mistral": ("Mistral-7B-Instruct-v0.3", "finetuned_mistral_7b_instruct"),
    "gemma": ("gemma-7b", "finetuned_gemma_7b"),
}

# ========================
# 工具函数定义
# ========================
def is_executable(code: str) -> bool:
    return bool(re.search(r"\b(END_|:=|IF|THEN|VAR)\b", code, re.IGNORECASE))

def intent_match(code: str, intent: str) -> bool:
    tag = intent.strip().split()[0].upper()
    return tag in code.upper()

def task_success(code: str, intent: str) -> bool:
    return "IF" in code.upper() and "THEN" in code.upper() and intent_match(code, intent)

def is_valid_code(code: str) -> bool:
    code = code.strip()
    return bool(code) and not code.lower().startswith("intent summary")

def extract_generated_code(md_text: str) -> str:
    if "### Generated Code:" not in md_text:
        return ""
    return md_text.split("### Generated Code:")[-1].strip()

# ========================
# 计算 BLEU 分数
# ========================
def compute_bleu(pred: str, ref: str) -> float:
    if not ref.strip():
        return 0.0
    result = sacrebleu.corpus_bleu([pred], [[ref]])
    return result.score

# ========================
# 加载提示词数据
# ========================
with open(prompt_file, "r") as f:
    prompts = [json.loads(line.strip()) for line in f]

# ========================
# 主对比流程
# ========================
records = []
for model_name, (orig_tag, tuned_tag) in model_pairs.items():
    for i, item in enumerate(prompts, 1):
        idx = f"{i:04d}"
        intent = item["intent"]
        reference = item.get("completion", "")

        orig_file = os.path.join(model_output_dir, f"Answer{idx}_POI_{model_name}.md")
        tuned_file = os.path.join(model_output_dir, f"Answer{idx}_POI_finetuned_{model_name}.md")

        if not os.path.exists(orig_file) or not os.path.exists(tuned_file):
            continue

        with open(orig_file, "r") as f:
            orig_code = extract_generated_code(f.read())
        with open(tuned_file, "r") as f:
            tuned_code = extract_generated_code(f.read())

        if not is_valid_code(orig_code) or not is_valid_code(tuned_code):
            continue

        records.append({
            "model": model_name,
            "exec_orig": is_executable(orig_code),
            "exec_tuned": is_executable(tuned_code),
            "intent_orig": intent_match(orig_code, intent),
            "intent_tuned": intent_match(tuned_code, intent),
            "success_orig": task_success(orig_code, intent),
            "success_tuned": task_success(tuned_code, intent),
            "bleu_orig": compute_bleu(orig_code, reference),
            "bleu_tuned": compute_bleu(tuned_code, reference),
        })

df = pd.DataFrame(records)

# ========================
# 统计每个模型的平均性能
# ========================
summary = df.groupby("model").agg({
    "exec_orig": "mean",
    "exec_tuned": "mean",
    "intent_orig": "mean",
    "intent_tuned": "mean",
    "success_orig": "mean",
    "success_tuned": "mean",
    "bleu_orig": "mean",
    "bleu_tuned": "mean"
}).reset_index()

# ========================
# 输出表格（可改为保存 CSV）
# ========================
print(summary.to_markdown(index=False))

# 保存为 CSV 和 Markdown 文件
summary.to_csv("comparison_results.csv", index=False)
with open("comparison_results.md", "w") as f:
    f.write(summary.to_markdown(index=False))