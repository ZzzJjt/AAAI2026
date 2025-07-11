import matplotlib.pyplot as plt
import pandas as pd
import os

# 模型名及对应 CSV 文件路径
model_logs = {
    "DeepSeek-7B": "logs/loss_log_deepseek.csv",
    "Gemma-7B": "logs/loss_log_gemma.csv",
    "InternLM2-7B": "logs/loss_log_internlm2.csv",
    "Mistral-7B": "logs/loss_log_mistral.csv",
    "Qwen2.5-7B": "logs/loss_log_qwen2.5.csv"
}

plt.figure(figsize=(10, 6))
colors = plt.get_cmap("tab10")

# 准备保存 Origin 用的 CSV
loss_data = {}

# 为每个模型绘图（按 epoch 平均）
for idx, (model_name, log_path) in enumerate(model_logs.items()):
    df = pd.read_csv(log_path)
    avg_loss = df.groupby("epoch")["loss"].mean().reset_index()

    # Plotting
    plt.plot(
        avg_loss["epoch"],
        avg_loss["loss"],
        label=model_name,
        linewidth=2,
        color=colors(idx)
    )

    # 存入 CSV 数据
    if "Epoch" not in loss_data:
        loss_data["Epoch"] = avg_loss["epoch"]
    loss_data[model_name] = avg_loss["loss"]

# 图形设置
plt.xlabel("Epoch")
plt.ylabel("Average Training Loss")
plt.title("Average Training Loss per Epoch Across Models")
plt.legend()
plt.grid(True)
plt.tight_layout()

# 保存图像
plt.savefig("training_loss_comparison_epochwise.png")
plt.savefig("training_loss_comparison_epochwise.pdf")
print("✅ Saved plot: training_loss_comparison_epochwise.(png/pdf)")

# 保存 CSV（用于 Origin 导入）
output_df = pd.DataFrame(loss_data)
output_df.to_csv("training_loss_summary.csv", index=False)
print("✅ Saved training loss data to training_loss_summary.csv")