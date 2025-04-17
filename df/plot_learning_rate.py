import matplotlib.pyplot as plt
import os

# 输出路径
save_path = "./df/df_output/Performance Metrics Over Epochs"
os.makedirs(save_path, exist_ok=True)

# 超参数
initial_lr = 1e-4
lr_clip = 1e-6
lr_decay = 0.5
# decay_steps = [22, 24, 28, 32, 36]
# num_epochs = 40

decay_steps = [22, 24, 26, 28]
num_epochs = 30

# 计算每个 epoch 的学习率
lrs = []
lr = initial_lr
for epoch in range(1, num_epochs + 1):
    factor = 1.0
    for step in decay_steps:
        if epoch > step:
            factor *= lr_decay
    lr = max(initial_lr * factor, lr_clip)
    lrs.append(lr)

# 绘图
plt.figure(figsize=(10, 6))
epochs = list(range(1, num_epochs + 1))
plt.plot(epochs, lrs, marker='o', color='purple', linewidth=2)
plt.title('Learning Rate Schedule (LambdaLR)', fontsize=16)
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Learning Rate', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# 只标记 decay_steps 和最后一个 epoch
for epoch, lr_val in zip(epochs, lrs):
    if epoch in decay_steps or epoch == num_epochs:
        label = f"({epoch}, {lr_val:.3e})"
        plt.annotate(label, (epoch, lr_val),
                     textcoords="offset points", xytext=(0, 10),
                     ha='center', fontsize=9, color='black')

plt.tight_layout()

# 保存图像
lr_fig_path = os.path.join(save_path, "LearningRate_Schedule.png")
plt.savefig(lr_fig_path, dpi=300)
plt.close()
print(f"Saved learning rate figure at: {lr_fig_path}")
