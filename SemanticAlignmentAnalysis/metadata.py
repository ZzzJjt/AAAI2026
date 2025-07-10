import os
import re
import pandas as pd
from collections import defaultdict

# 设置模型根目录
root_path = "../Industrial-Control/Models"
model_names = ["Deepseek", "GPT", "Grok"]

# 类别列表
category_list = [
    "Advanced Process Control",
    "Diagnostics and Communication",
    "Interlocks",
    "Mathematical Functions",
    "PLC Programing Tasks",
    "Process Control",
    "Programmer Support",
    "Sequential Control",
    "Standard Algorithms",
    "Various Engineering Inputs"
]

# PromptType 顺序
prompt_order = {
    "BAB": 0,
    "CARE": 1,
    "RISE": 2,
    "RTF": 3,
    "TAG": 4
}

# 模型编号起点
model_base = {
    "Deepseek": 0,
    "GPT": 500,
    "Grok": 1000
}

# 语义标签映射关键词
tag_keywords = {
    "FIC": ["flow control", "FIC", "flow rate"],
    "TIC": ["temperature control", "TIC", "heat exchanger"],
    "PIC": ["pressure control", "PIC", "bar", "psi"],
    "INTLK": ["interlock", "safety condition", "permissive", "block"],
    "ALM": ["alarm", "fault", "error", "warning"],
    "ACT": ["valve", "pump", "motor", "actuator", "output coil"],
    "SEN": ["sensor", "input", "acquire", "measured value"],
    "LOGIC": ["IF", "CASE", "logic", "comparison"],
    "SEQ": ["step", "sequence", "SFC", "sequential", "transition"],
    "RPT": ["log", "report", "record", "save"]
}

def extract_tags_from_content(content):
    content = content.lower()
    tags = set()
    for tag, keywords in tag_keywords.items():
        if any(kw in content for kw in keywords):
            tags.add(tag)
    return ",".join(sorted(tags))

# 遍历生成记录
all_rows = []
count_map = defaultdict(int)

for model in model_names:
    for root, dirs, files in os.walk(os.path.join(root_path, model)):
        if "Standard Code in Prompts" in root:
            continue
        for file in files:
            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)
            filename = os.path.basename(filepath)

            match = re.match(r"Answer(\d{4})_([A-Z]+)_(\w+)\.md", filename)
            if not match:
                print(f"❌ Skipped unrecognized filename: {filename}")
                continue

            prompt_id = int(match.group(1))
            prompt_type = match.group(2)
            model_name = match.group(3)

            base = model_base[model]
            type_offset = prompt_order[prompt_type] * 100
            local_id = prompt_id - base - type_offset
            category_index = local_id // 10
            category = category_list[category_index] if 0 <= category_index < 10 else "Unknown"

            # 读取内容并提取标签
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                tags = extract_tags_from_content(content)
            except Exception as e:
                print(f"❌ Failed to read {filepath}: {e}")
                tags = ""

            all_rows.append({
                "Filename": filepath,
                "PromptID": prompt_id,
                "PromptType": prompt_type,
                "Model": model_name,
                "Category": category,
                "Tags": tags
            })

            count_map[(model, prompt_type)] += 1

# 写入 CSV
df = pd.DataFrame(all_rows)
df.to_csv("metadata.csv", index=False)
print(f"✅ metadata.csv saved with {len(df)} rows.")

# 打印统计
print("\n📊 文件分布统计：")
for model in model_names:
    for ptype in prompt_order.keys():
        key = (model, ptype)
        count = count_map.get(key, 0)
        status = "✅" if count == 100 else "❌"
        print(f"{status} {model}-{ptype}: {count} files")