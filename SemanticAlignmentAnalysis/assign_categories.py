# assign_categories.py

def get_category_from_prompt_number(prompt_number: int) -> str:
    category_mapping = {
        range(1, 11): "APC",
        range(11, 21): "DIA",
        range(21, 31): "INT",
        range(31, 41): "MATH",
        range(41, 51): "PLC",
        range(51, 61): "CTRL",
        range(61, 71): "PSUP",
        range(71, 81): "SEQ",
        range(81, 91): "STD",
        range(91, 101): "ENG"
    }
    for key_range, category in category_mapping.items():
        if prompt_number in key_range:
            return category
    return "Unknown"


# 示例用法
if __name__ == "__main__":
    test_files = [
        "Answer03_BAB_GPT.md",
        "Answer27_RISE_Deepseek.md",
        "Answer49_TAG_Grok.md",
        "Answer73_CARE_GPT.md",
        "Answer91_RTF_Grok.md"
    ]

    for filename in test_files:
        try:
            prompt_number = int(filename.split("Answer")[1].split("_")[0])
            category = get_category_from_prompt_number(prompt_number)
            print(f"{filename} → {category}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")