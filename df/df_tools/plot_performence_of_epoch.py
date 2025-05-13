import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv('./result/waymo_performance_summary.csv')

# 保存为 Excel 文件
df.to_excel('./result/waymo_performance_summary.xlsx', index=False)

# 设置图像的分辨率
dpi = 300

# 1. 绘制 Vehicle_mAP
plt.figure(figsize=(12, 10), dpi=dpi)
plt.plot(df['Epoch'], df['Vehicle_mAP'], label='Vehicle_mAP', color='blue', marker='o')
plt.plot(df['Epoch'], df['Pedestrian_mAP'], label='Pedestrian_mAP', color='green', marker='o')
plt.plot(df['Epoch'], df['Cyclist_mAP'], label='Cyclist_mAP', color='red', marker='o')
plt.plot(df['Epoch'], df['Avg_mAP'], label='Avg_mAP', color='purple', marker='o', linewidth=2)  # 加深 Avg 线条
plt.title('Vehicle, Pedestrian, Cyclist, and Avg mAP')
plt.xlabel('Epoch')
plt.ylabel('mAP')
plt.legend()

# 标记坐标值
for i, epoch in enumerate(df['Epoch']):
    plt.annotate(f"({df['Epoch'][i]}, {df['Vehicle_mAP'][i]:.3f})", 
                 (df['Epoch'][i], df['Vehicle_mAP'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Pedestrian_mAP'][i]:.3f})", 
                 (df['Epoch'][i], df['Pedestrian_mAP'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Cyclist_mAP'][i]:.3f})", 
                 (df['Epoch'][i], df['Cyclist_mAP'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Avg_mAP'][i]:.3f})", 
                 (df['Epoch'][i], df['Avg_mAP'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# 保存图像
plt.savefig('./df/df_output/Performance Metrics Over Epochs/vehicle_pedestrian_cyclist_mAP.png')

# 2. 绘制 Vehicle_minADE
plt.figure(figsize=(12, 10), dpi=dpi)
plt.plot(df['Epoch'], df['Vehicle_minADE'], label='Vehicle_minADE', color='blue', marker='o')
plt.plot(df['Epoch'], df['Pedestrian_minADE'], label='Pedestrian_minADE', color='green', marker='o')
plt.plot(df['Epoch'], df['Cyclist_minADE'], label='Cyclist_minADE', color='red', marker='o')
plt.plot(df['Epoch'], df['Avg_minADE'], label='Avg_minADE', color='purple', marker='o', linewidth=2)  # 加深 Avg 线条
plt.title('Vehicle, Pedestrian, Cyclist, and Avg minADE')
plt.xlabel('Epoch')
plt.ylabel('minADE')
plt.legend()

# 标记坐标值
for i, epoch in enumerate(df['Epoch']):
    plt.annotate(f"({df['Epoch'][i]}, {df['Vehicle_minADE'][i]:.3f})", 
                 (df['Epoch'][i], df['Vehicle_minADE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Pedestrian_minADE'][i]:.3f})", 
                 (df['Epoch'][i], df['Pedestrian_minADE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Cyclist_minADE'][i]:.3f})", 
                 (df['Epoch'][i], df['Cyclist_minADE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Avg_minADE'][i]:.3f})", 
                 (df['Epoch'][i], df['Avg_minADE'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# 保存图像
plt.savefig('./df/df_output/Performance Metrics Over Epochs/vehicle_pedestrian_cyclist_minADE.png')

# 3. 绘制 Vehicle_minFDE
plt.figure(figsize=(12, 10), dpi=dpi)
plt.plot(df['Epoch'], df['Vehicle_minFDE'], label='Vehicle_minFDE', color='blue', marker='o')
plt.plot(df['Epoch'], df['Pedestrian_minFDE'], label='Pedestrian_minFDE', color='green', marker='o')
plt.plot(df['Epoch'], df['Cyclist_minFDE'], label='Cyclist_minFDE', color='red', marker='o')
plt.plot(df['Epoch'], df['Avg_minFDE'], label='Avg_minFDE', color='purple', marker='o', linewidth=2)  # 加深 Avg 线条
plt.title('Vehicle, Pedestrian, Cyclist, and Avg minFDE')
plt.xlabel('Epoch')
plt.ylabel('minFDE')
plt.legend()

# 标记坐标值
for i, epoch in enumerate(df['Epoch']):
    plt.annotate(f"({df['Epoch'][i]}, {df['Vehicle_minFDE'][i]:.3f})", 
                 (df['Epoch'][i], df['Vehicle_minFDE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Pedestrian_minFDE'][i]:.3f})", 
                 (df['Epoch'][i], df['Pedestrian_minFDE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Cyclist_minFDE'][i]:.3f})", 
                 (df['Epoch'][i], df['Cyclist_minFDE'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Avg_minFDE'][i]:.3f})", 
                 (df['Epoch'][i], df['Avg_minFDE'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# 保存图像
plt.savefig('./df/df_output/Performance Metrics Over Epochs/vehicle_pedestrian_cyclist_minFDE.png')

# 4. 绘制 Vehicle_MissRate
plt.figure(figsize=(12, 10), dpi=dpi)
plt.plot(df['Epoch'], df['Vehicle_MissRate'], label='Vehicle_MissRate', color='blue', marker='o')
plt.plot(df['Epoch'], df['Pedestrian_MissRate'], label='Pedestrian_MissRate', color='green', marker='o')
plt.plot(df['Epoch'], df['Cyclist_MissRate'], label='Cyclist_MissRate', color='red', marker='o')
plt.plot(df['Epoch'], df['Avg_MissRate'], label='Avg_MissRate', color='purple', marker='o', linewidth=2)  # 加深 Avg 线条
plt.title('Vehicle, Pedestrian, Cyclist, and Avg MissRate')
plt.xlabel('Epoch')
plt.ylabel('MissRate')
plt.legend()

# 标记坐标值
for i, epoch in enumerate(df['Epoch']):
    plt.annotate(f"({df['Epoch'][i]}, {df['Vehicle_MissRate'][i]:.3f})", 
                 (df['Epoch'][i], df['Vehicle_MissRate'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Pedestrian_MissRate'][i]:.3f})", 
                 (df['Epoch'][i], df['Pedestrian_MissRate'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Cyclist_MissRate'][i]:.3f})", 
                 (df['Epoch'][i], df['Cyclist_MissRate'][i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"({df['Epoch'][i]}, {df['Avg_MissRate'][i]:.3f})", 
                 (df['Epoch'][i], df['Avg_MissRate'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# 保存图像
plt.savefig('./df/df_output/Performance Metrics Over Epochs/vehicle_pedestrian_cyclist_MissRate.png')

# 显示所有图形
plt.show()



# 1. 绘制 Vehicle_mAP
plt.figure(figsize=(12, 10), dpi=dpi)
plt.plot(df['Epoch'], df['Avg_mAP'], label='Avg_mAP', color='purple', marker='o', linewidth=2)  # 加深 Avg 线条
plt.title('Avg mAP')
plt.xlabel('Epoch')
plt.ylabel('mAP')
plt.legend()

# 标记坐标值
for i, epoch in enumerate(df['Epoch']):
    plt.annotate(f"({df['Epoch'][i]}, {df['Avg_mAP'][i]:.3f})", 
                 (df['Epoch'][i], df['Avg_mAP'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# 保存图像
plt.savefig('./df/df_output/Performance Metrics Over Epochs/Avg_mAP.png')