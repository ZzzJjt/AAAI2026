import os
import json

# 📂 Paths
prompt_root = "/home/zhengjiatong/AAAI2026/Industrial-Control/Prompt"
completion_root = "/home/zhengjiatong/AAAI2026/Industrial-Control/Models"
model_names = ["Deepseek", "GPT", "Grok"]
output_path = "finetune_data.jsonl"

# 🧠 Read file list
def list_md_files(path):
    return sorted(
        [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".md")]
    )

finetune_data = []

# 🧠 Traverse each prompt_type and category
for prompt_type_folder in sorted(os.listdir(prompt_root)):
    prompt_type_path = os.path.join(prompt_root, prompt_type_folder)
    if not os.path.isdir(prompt_type_path):
        continue

    for category in sorted(os.listdir(prompt_type_path)):
        category_path = os.path.join(prompt_type_path, category)
        if not os.path.isdir(category_path):
            continue

        prompt_files = list_md_files(category_path)

        # 🧠 Iterate models and match corresponding completion files
        for model in model_names:
            completion_category_path = os.path.join(
                completion_root, model, prompt_type_folder, category
            )
            if not os.path.exists(completion_category_path):
                continue

            completion_files = list_md_files(completion_category_path)

            if len(completion_files) != len(prompt_files):
                print(
                    f"⚠️ Warning: file count mismatch in {model}/{prompt_type_folder}/{category}"
                )
                continue

            for pf, cf in zip(prompt_files, completion_files):
                prompt_text = open(pf, encoding="utf-8").read().strip()
                completion_text = open(cf, encoding="utf-8").read().strip()

                # 🧠 Save example with Model & PromptType
                finetune_data.append(
                    {
                        "prompt": prompt_text,
                        "completion": completion_text,
                        "Model": model,
                        "PromptType": prompt_type_folder,
                    }
                )

# 🧠 Save as JSONL
with open(output_path, "w", encoding="utf-8") as f:
    for row in finetune_data:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"✅ Saved {len(finetune_data)} examples to {output_path}")