import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取 SAS 分数数据
sas_df = pd.read_csv("sas_score.csv")

# 所有语义标签
tags = ['FIC', 'TIC', 'PIC', 'INTLK', 'ALM', 'ACT', 'SEN', 'LOGIC', 'SEQ', 'RPT']
N = len(tags)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图

# 所有模型
models = sas_df['Model'].unique()
prompt_types = ['BAB', 'CARE', 'RISE', 'RTF', 'TAG']

# 为每个模型生成一张雷达图
for model in models:
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

    for prompt_type in prompt_types:
        subset = sas_df[(sas_df['Model'] == model) & (sas_df['PromptType'] == prompt_type)]
        if not subset.empty:
            values = subset[tags].values.flatten().tolist()
            values += values[:1]  # 闭合
            ax.plot(angles, values, label=prompt_type, linewidth=2)
            ax.fill(angles, values, alpha=0.1)

    ax.set_thetagrids(np.degrees(angles[:-1]), tags)
    ax.set_title(f'{model} - SAS Radar (All Prompts)', fontsize=14)
    ax.grid(True)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    plt.tight_layout()
    plt.savefig(f"radar_{model}_all_prompts.png")
    plt.close()

print("✅ 三张雷达图（每个模型一张）已保存为 PNG")