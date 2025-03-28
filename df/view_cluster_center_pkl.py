import os
import pickle
import matplotlib
import numpy as np
from scipy.interpolate import make_interp_spline

matplotlib.use('Agg')  # 使用 Agg 后端
import matplotlib.pyplot as plt


def draw_individual_curves(data, label, color, output_path):
    """绘制从原点到每个点的单独平滑曲线"""
    plt.figure(figsize=(10, 8))  # 设置单张图尺寸

    # 遍历每个数据点，绘制从原点到数据点的平滑曲线
    for point in data:
        x_vals = [0, point[0]]  # 原点到数据点的 x 坐标
        y_vals = [0, point[1]]  # 原点到数据点的 y 坐标

        # 如果点数足够，则进行平滑插值
        if len(x_vals) >= 2:
            # 生成 50 个平滑插值点
            x_smooth = np.linspace(0, point[0], 50)

            # 进行二阶或三阶样条插值
            if len(x_vals) > 2:
                y_smooth = make_interp_spline(x_vals, y_vals, k=2)(x_smooth)  # k=2 二阶样条
            else:
                # 两个点时使用线性插值
                y_smooth = np.interp(x_smooth, x_vals, y_vals)

            # 绘制平滑曲线
            plt.plot(x_smooth, y_smooth, color=color, linewidth=1, alpha=0.7)  # 透明度 0.7

        # 在数据点绘制星形标记
        plt.scatter(point[0], point[1], color=color, marker='*', s=100)  # 星形标记

    # 设置图像标签
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title(f'{label} Cluster Centers with Individual Smooth Curves')
    plt.grid(True)
    plt.axis('equal')  # 保持比例尺一致

    # 保存图像
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"{label} plot saved as '{output_path}'")
    plt.close()


def view_cluster_center_dick_pkl(cluster_pkl_dir):
    # 读取 pkl 文件
    with open(cluster_pkl_dir, 'rb') as f:
        cluster_scene_data = pickle.load(f)

    # 提取不同类型的数据
    vehicle_data = cluster_scene_data['TYPE_VEHICLE']
    pedestrian_data = cluster_scene_data['TYPE_PEDESTRIAN']
    cyclist_data = cluster_scene_data['TYPE_CYCLIST']

    # 检查数据格式
    print(f"Vehicle Data Sample: {vehicle_data[:5]}")
    print(f"Pedestrian Data Sample: {pedestrian_data[:5]}")
    print(f"Cyclist Data Sample: {cyclist_data[:5]}")

    # 确保输出目录存在
    output_dir = './df/df_output'
    os.makedirs(output_dir, exist_ok=True)

    # 绘制每种数据类型的单独图像
    if len(vehicle_data) > 0:
        draw_individual_curves(vehicle_data, 'Vehicle', 'blue', os.path.join(output_dir, 'vehicle_cluster_plot.png'))

    if len(pedestrian_data) > 0:
        draw_individual_curves(pedestrian_data, 'Pedestrian', 'green', os.path.join(output_dir, 'pedestrian_cluster_plot.png'))

    if len(cyclist_data) > 0:
        draw_individual_curves(cyclist_data, 'Cyclist', 'red', os.path.join(output_dir, 'cyclist_cluster_plot.png'))


if __name__ == '__main__':
    cluster_pkl_dir = './MTR/data/waymo/cluster_64_center_dict.pkl'
    view_cluster_center_dick_pkl(cluster_pkl_dir)
