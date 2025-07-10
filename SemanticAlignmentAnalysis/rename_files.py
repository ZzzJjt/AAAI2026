import os

root_path = os.path.expanduser("~/AAAI2026/Industrial-Control/Models")
model_names = ["Deepseek", "GPT", "Grok"]

# PromptType 文件夹名映射
prompt_type_map = {
    "B-A-B": "BAB",
    "C-A-R-E": "CARE",
    "R-I-S-E": "RISE",
    "R-T-F": "RTF",
    "T-A-G": "TAG"
}

# 各模型对应起始编号
base_ids = {
    "Deepseek": {"BAB": 1, "CARE": 101, "RISE": 201, "RTF": 301, "TAG": 401},
    "GPT": {"BAB": 501, "CARE": 601, "RISE": 701, "RTF": 801, "TAG": 901},
    "Grok": {"BAB": 1001, "CARE": 1101, "RISE": 1201, "RTF": 1301, "TAG": 1401},
}

for model in model_names:
    model_path = os.path.join(root_path, model)
    if not os.path.exists(model_path):
        print(f"❌ Model path not found: {model_path}")
        continue

    for subfolder in os.listdir(model_path):
        full_type_path = os.path.join(model_path, subfolder)
        if not os.path.isdir(full_type_path):
            continue

        # 判断提示词类型
        prompt_type = None
        for key, val in prompt_type_map.items():
            if key in subfolder:
                prompt_type = val
                break
        if not prompt_type:
            print(f"❌ Skipped unknown prompt type folder: {subfolder}")
            continue

        base_id = base_ids[model][prompt_type]

        # 获取有效子分类，排除 “Standard Code in Prompts”
        valid_categories = [
            d for d in os.listdir(full_type_path)
            if os.path.isdir(os.path.join(full_type_path, d)) and d != "Standard Code in Prompts"
        ]

        # 确保 Advanced Process Control 是第一个，其余按字母排序
        categories = ["Advanced Process Control"] + sorted(
            [c for c in valid_categories if c != "Advanced Process Control"]
        )

        for i, category in enumerate(categories):
            category_path = os.path.join(full_type_path, category)
            current_id = base_id + i * 10  # 正确编号，不跳过任何编号

            md_files = sorted([
                f for f in os.listdir(category_path)
                if f.endswith(".md")
            ])
            for file in md_files:
                old_path = os.path.join(category_path, file)
                new_name = f"Answer{current_id:04d}_{prompt_type}_{model}.md"
                new_path = os.path.join(category_path, new_name)

                try:
                    os.rename(old_path, new_path)
                    print(f"✅ {file} → {new_name}")
                    current_id += 1
                except Exception as e:
                    print(f"❌ Failed: {file} → {e}")