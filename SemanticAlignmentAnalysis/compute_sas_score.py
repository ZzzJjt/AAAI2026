import pandas as pd
import numpy as np
from collections import Counter
import math

# =========================
# 配置与常量
# =========================
# 输入文件
metadata_path = "metadata.csv"
# 输出文件
output_path = "sas_score.csv"

# 所有语义标签
all_tags = ['FIC', 'TIC', 'PIC', 'INTLK', 'ALM', 'ACT', 'SEN', 'LOGIC', 'SEQ', 'RPT']

# =========================
# 加载数据
# =========================
df = pd.read_csv(metadata_path)

# 确保 Tags 列转换为列表
def parse_tags(tags):
    if isinstance(tags, float) and pd.isna(tags):
        return []
    if isinstance(tags, str):
        return [tag.strip() for tag in tags.split(',') if tag.strip()]
    return []

df['Tags'] = df['Tags'].apply(parse_tags)

# =========================
# 按模型 + 提示类型分组
# =========================
results = []
grouped = df.groupby(['Model', 'PromptType'])

for (model, prompt_type), group in grouped:
    total_files = len(group)
    tag_counts = Counter()
    # 统计每个文件中出现的标签
    for tags in group['Tags']:
        unique_tags = set(tags)
        tag_counts.update(unique_tags)

    # 计算出现频率向量
    tag_vector = np.array([tag_counts[tag] / total_files for tag in all_tags])
    # 计算熵
    entropy = -np.sum(tag_vector * np.log2(tag_vector + 1e-9))  # 避免 log(0)

    # 打包结果
    result = {
        "Model": model,
        "PromptType": prompt_type,
        "SAS_Entropy": round(entropy, 4),
    }
    for tag in all_tags:
        result[tag] = tag_counts[tag]

    results.append(result)

# =========================
# 计算对齐度评分
# =========================
sas_df = pd.DataFrame(results)

# 使用 min-max normalization 来规范化熵
min_entropy = sas_df['SAS_Entropy'].min()
max_entropy = sas_df['SAS_Entropy'].max()

sas_df['AlignmentScore'] = 1 - (sas_df['SAS_Entropy'] - min_entropy) / (max_entropy - min_entropy)
# =========================
# 输出文件
# =========================
sas_df.to_csv(output_path, index=False)
print(f"✅ SAS scores and AlignmentScore saved to {output_path}")