import json
import pandas as pd
import re

# 📂 Paths
finetune_data_path = "finetune_data.jsonl"
sas_score_path = "/home/zhengjiatong/AAAI2026/SemanticAlignmentAnalysis/sas_score.csv"
filtered_output_path = "finetune_data_high_alignment.jsonl"
alignment_quantile = 0.7  # 前70%样本

# 🔄 Load the SAS score file
sas_df = pd.read_csv(sas_score_path)

# 🧠 建立 (Model, PromptType) 到 AlignmentScore 的映射
alignment_map = {
    (row['Model'], row['PromptType']): row['AlignmentScore']
    for _, row in sas_df.iterrows()
}

# 🔍 计算筛选阈值
threshold = sas_df['AlignmentScore'].quantile(1 - alignment_quantile)
print(f"(筛选阈值为前{int(alignment_quantile*100)}%，对应 AlignmentScore ≥ {threshold:.4f})")

# 🧠 Helper：规范化PromptType，比如 B-A-B(Before-After-Before) -> BAB
def normalize_prompt_type(ptype: str) -> str:
    # 提取第一个括号前的部分，然后取其中大写字母拼接
    base = ptype.split("(")[0]
    return "".join(re.findall(r"[A-Z]", base))

# 🧠 读取 finetune_data.jsonl 并筛选
filtered_data = []
with open(finetune_data_path, encoding="utf-8") as f:
    for line in f:
        example = json.loads(line)
        model = example.get("Model")
        prompt_type = normalize_prompt_type(example.get("PromptType"))
        score = alignment_map.get((model, prompt_type), -1.0)

        # 🔍 打印检查信息
        print(f"{model}-{example.get('PromptType')}: score={score}")

        if score >= threshold:
            filtered_data.append(example)

# 🧠 输出筛选后的文件
with open(filtered_output_path, "w", encoding="utf-8") as f:
    for row in filtered_data:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"✅ Saved {len(filtered_data)} high-alignment examples to {filtered_output_path}")