# import pickle
# import numpy as np
# import matplotlib.pyplot as plt
# import os

# PRED_FILE = '/media/simple/Data/WorkSpace/DFPred/EDA/output/dfPred/df_eda_test/eda_df_result_debug/eval/epoch_30/default/result_nms-2.5.pkl'
# GT_FILE = '/media/simple/Data/WorkSpace/DFPred/EDA/output/gt_data_df_test_A.pkl'
# TOP_K = 6
# EVAL_SECOND = 8
# NUM_MODES_FOR_EVAL = 6
# SAVE_DIR = "./df/df_output/test_compare_gt_and_pred"

# def load_data(pred_file, gt_file):
#     with open(pred_file, 'rb') as f:
#         pred_data = pickle.load(f)
#     with open(gt_file, 'rb') as f:
#         gt_data = pickle.load(f)
#     return pred_data, gt_data

# def format_for_evaluation(pred_data, gt_data):
#     eval_data = []
#     for pred_scene in pred_data:
#         formatted_scene = []
#         scenario_id = pred_scene[0]['scenario_id']
#         if scenario_id not in gt_data:
#             print(f"Warning: scenario_id {scenario_id} not found in GT.")
#             continue
#         gt_scene = gt_data[scenario_id]
#         assert len(pred_scene) == len(gt_scene['tracks_to_predict'])
#         i = 0
#         for obj_pred in pred_scene:
#             obj_id = obj_pred['object_id']
#             if obj_id not in gt_scene['object_id']:
#                 print(f"Warning: object_id {obj_id} not found in GT.")
#                 continue
#             gt_idx = gt_scene['tracks_to_predict'][i]
#             pred_trajs = obj_pred['pred_trajs'][:, :80, :]
#             gt_trajs = gt_scene['gt_trajs'][gt_idx][:91, :]
#             scores = obj_pred['pred_scores']
#             sorted_indices = np.argsort(-scores)
#             topk_indices = sorted_indices[:TOP_K]
#             topk_trajs = pred_trajs[topk_indices, :, :]
#             topk_scores = scores[topk_indices]
#             formatted_scene.append({
#                 'scenario_id': scenario_id,
#                 'pred_trajs': topk_trajs,
#                 'pred_scores': topk_scores,
#                 'object_id': obj_id,
#                 'object_type': obj_pred['object_type'],
#                 'gt_trajs': gt_trajs
#             })
#             i += 1
#         if formatted_scene:
#             eval_data.append(formatted_scene)
#     return eval_data

# def view():
#     pred_data, gt_data = load_data(PRED_FILE, GT_FILE)
#     eval_data = format_for_evaluation(pred_data, gt_data)

#     for scene in eval_data:
#         if not scene:
#             continue
#         scenario_id = scene[0]['scenario_id']
#         plt.figure(figsize=(12, 10))
#         color_map = plt.cm.get_cmap('tab20', len(scene))

#         for i, obj_data in enumerate(scene):
#             object_id = obj_data['object_id']
#             pred_trajs = obj_data['pred_trajs']
#             gt_trajs = obj_data['gt_trajs']
#             object_type = obj_data['object_type']
#             color = color_map(i)
#             for k in range(pred_trajs.shape[0]):
#                 alpha = 0.5 + 0.5 * (k + 1) / pred_trajs.shape[0]
#                 plt.plot(pred_trajs[k, :, 0], pred_trajs[k, :, 1],
#                          linestyle='--', color=color, alpha=alpha,
#                          label=f'Obj {object_id} Pred {k+1}' if k == 0 else None)
#             plt.plot(gt_trajs[:, 0], gt_trajs[:, 1],
#                      color='black', linewidth=2.0,
#                      label=f'Obj {object_id} GT')

#         plt.title(f"Scenario {scenario_id}: Predicted vs Ground Truth")
#         plt.xlabel("X")
#         plt.ylabel("Y")
#         plt.legend(fontsize='small')
#         plt.grid(True)
#         plt.axis('equal')
#         plt.tight_layout()
#         save_path = os.path.join(SAVE_DIR, f"scenario_{scenario_id}_multi_obj_vis.png")
#         plt.savefig(save_path, dpi=300)
#         print(f"Saved visualization: {save_path}")
#         plt.close()

# def view_sep():
#     pred_data, gt_data = load_data(PRED_FILE, GT_FILE)
#     eval_data = format_for_evaluation(pred_data, gt_data)

#     for scene in eval_data:
#         if not scene:
#             continue
#         scenario_id = scene[0]['scenario_id']
#         scenario_dir = os.path.join(SAVE_DIR, scenario_id)
#         os.makedirs(scenario_dir, exist_ok=True)

#         for i, obj_data in enumerate(scene):
#             object_id = obj_data['object_id']
#             pred_trajs = obj_data['pred_trajs']
#             gt_trajs = obj_data['gt_trajs']
#             object_type = obj_data['object_type']

#             plt.figure(figsize=(8, 6))
#             # 颜色设置为渐变色系
#             for k in range(pred_trajs.shape[0]):
#                 alpha = 0.5 + 0.5 * (k + 1) / pred_trajs.shape[0]
#                 plt.plot(pred_trajs[k, :, 0], pred_trajs[k, :, 1],
#                          linestyle='--', color='blue', alpha=alpha,
#                          label=f'Pred {k+1}' if k == 0 else None)
#             # 画 GT
#             plt.plot(gt_trajs[:, 0], gt_trajs[:, 1],
#                      color='black', linewidth=2.0,
#                      label='Ground Truth')

#             plt.title(f"Scenario {scenario_id} - Object - {object_type} - {object_id}")
#             plt.xlabel("X")
#             plt.ylabel("Y")
#             plt.legend(fontsize='small')
#             plt.grid(True)
#             plt.axis('equal')
#             plt.tight_layout()

#             save_path = os.path.join(scenario_dir, f"object_{object_type}_{object_id}_vis.png")
#             plt.savefig(save_path, dpi=300)
#             #print(f"Saved single object visualization: {save_path}")
#             plt.close()


# if __name__ == '__main__':
#     #view()
#     view_sep()


import pickle
import numpy as np
import matplotlib.pyplot as plt
import os

PRED_FILE = '/media/simple/Data/WorkSpace/DF_EDA/df_pred_result/result_processed_scenarios_testing_A_part.pkl'
GT_FILE = '/media/simple/Data/WorkSpace/DF_EDA/df_pred_result/gt_data_df_test_A.pkl'
TOP_K = 6
EVAL_SECOND = 8
NUM_MODES_FOR_EVAL = 6
SAVE_DIR = "./df/df_output/ex5/test_compare_gt_and_pred_2"

def load_data(pred_file, gt_file):
    with open(pred_file, 'rb') as f:
        pred_data = pickle.load(f)
    with open(gt_file, 'rb') as f:
        gt_data = pickle.load(f)
    return pred_data, gt_data

def format_for_evaluation(pred_data, gt_data):
    eval_data = []
    for pred_scene in pred_data:
        formatted_scene = []
        scenario_id = pred_scene[0]['scenario_id']
        if scenario_id not in gt_data:
            print(f"Warning: scenario_id {scenario_id} not found in GT.")
            continue
        gt_scene = gt_data[scenario_id]
        assert len(pred_scene) == len(gt_scene['tracks_to_predict'])
        i = 0
        for obj_pred in pred_scene:
            obj_id = obj_pred['object_id']
            if obj_id not in gt_scene['object_id']:
                print(f"Warning: object_id {obj_id} not found in GT.")
                continue
            gt_idx = gt_scene['tracks_to_predict'][i]
            pred_trajs = obj_pred['pred_trajs'][:, :80, :]
            gt_trajs = gt_scene['gt_trajs'][gt_idx][:91, :]
            scores = obj_pred['pred_scores']
            sorted_indices = np.argsort(-scores)
            topk_indices = sorted_indices[:TOP_K]
            topk_trajs = pred_trajs[topk_indices, :, :]
            topk_scores = scores[topk_indices]
            formatted_scene.append({
                'scenario_id': scenario_id,
                'pred_trajs': topk_trajs,
                'pred_scores': topk_scores,
                'object_id': obj_id,
                'object_type': obj_pred['object_type'],
                'gt_trajs': gt_trajs
            })
            i += 1
        if formatted_scene:
            eval_data.append(formatted_scene)
    return eval_data

# def view_sep():
#     pred_data, gt_data = load_data(PRED_FILE, GT_FILE)
#     eval_data = format_for_evaluation(pred_data, gt_data)

#     for scene in eval_data:
#         if not scene:
#             continue
#         scenario_id = scene[0]['scenario_id']
#         scenario_dir = os.path.join(SAVE_DIR, scenario_id)
#         os.makedirs(scenario_dir, exist_ok=True)

#         for i, obj_data in enumerate(scene):
#             object_id = obj_data['object_id']
#             pred_trajs = obj_data['pred_trajs']
#             gt_trajs = obj_data['gt_trajs']
#             object_type = obj_data['object_type']
#             pred_scores = obj_data['pred_scores']

#             plt.figure(figsize=(8, 6))

#             # 画预测轨迹
#             for k in range(pred_trajs.shape[0]):
#                 # 根据预测分数调节颜色深浅，分数高的颜色深
#                 color = plt.cm.viridis(pred_scores[k] / max(pred_scores))  # 使用 viridis 色图并根据得分调节颜色
#                 # 根据轨迹的时间逐渐变浅，未来轨迹透明度逐渐减小
#                 alpha = 1 - (k + 1) / pred_trajs.shape[0]
#                 plt.plot(pred_trajs[k, :, 0], pred_trajs[k, :, 1],
#                          linestyle='--', color=color, alpha=alpha,
#                          label=f'Pred {k+1}' if k == 0 else None)

#             # 画真值轨迹，绿色虚线
#             plt.plot(gt_trajs[:, 0], gt_trajs[:, 1],
#                      color='green', linestyle='--', linewidth=2.0,
#                      label='Ground Truth')

#             plt.title(f"Scenario {scenario_id} - Object - {object_type} - {object_id}")
#             plt.xlabel("X")
#             plt.ylabel("Y")
#             plt.legend(fontsize='small')
#             plt.grid(True)
#             plt.axis('equal')
#             plt.tight_layout()

#             os.makedirs(SAVE_DIR, exist_ok=True)
#             save_path = os.path.join(scenario_dir, f"object_{object_type}_{object_id}_vis.png")
#             plt.savefig(save_path, dpi=300)
#             print(f"Saved single object visualization: {save_path}")
#             plt.close()

def view_sep():
    pred_data, gt_data = load_data(PRED_FILE, GT_FILE)
    eval_data = format_for_evaluation(pred_data, gt_data)

    for scene in eval_data:
        if not scene:
            continue
        scenario_id = scene[0]['scenario_id']
        scenario_dir = os.path.join(SAVE_DIR, scenario_id)
        os.makedirs(scenario_dir, exist_ok=True)

        for i, obj_data in enumerate(scene):
            object_id = obj_data['object_id']
            pred_trajs = obj_data['pred_trajs']
            gt_trajs = obj_data['gt_trajs']
            object_type = obj_data['object_type']
            pred_scores = obj_data['pred_scores']

            plt.figure(figsize=(10, 8))
            
            # 使用更稳定的样式
            plt.style.use('default')
            
            # 定义调色板
            cmap = plt.cm.viridis
            
            # 计算最高分
            max_score = max(pred_scores)
            
            # 绘制真实轨迹（降低zorder值确保在底层）
            num_gt_points = gt_trajs.shape[0]
            
            # 创建时间相关的颜色渐变
            times = np.linspace(0, 1, num_gt_points)
            colors = [plt.cm.coolwarm(t) for t in times]  # 使用红蓝渐变表示时间
            
            # 分段绘制GT轨迹，显示时间演进效果
            for t in range(num_gt_points - 1):
                alpha = 0.4 + 0.6 * (t / num_gt_points)  # 随时间增加透明度
                
                plt.plot(gt_trajs[t:t+2, 0], gt_trajs[t:t+2, 1],
                         color='green', 
                         linestyle='-', 
                         linewidth=1.5,
                         alpha=0.8,
                         zorder=0)
                
                # 添加时间标记点（使用不同形状）
                if t % 5 == 0:  # 每5个时间步画一个标记点
                    plt.scatter(gt_trajs[t, 0], gt_trajs[t, 1], 
                               c=[colors[t]], 
                               s=30, 
                               alpha=0.7,
                               edgecolors='black',
                               linewidths=0.3,
                               zorder=0,
                               marker='s')  # 正方形标记
                    
            # 绘制预测轨迹
            sorted_indices = np.argsort(-pred_scores)
            
            for rank, k in enumerate(sorted_indices):
                # 根据排名调整线宽
                base_linewidth = 1.5
                max_linewidth = 2.5
                linewidth = max_linewidth - (max_linewidth - base_linewidth) * (rank / len(sorted_indices))
                
                # 根据分数调整颜色深浅
                color = cmap(pred_scores[k] / max_score)
                
                # 创建渐变透明度
                alphas = np.linspace(0.9, 0.3, pred_trajs.shape[1])
                
                # 分段绘制轨迹
                for t in range(pred_trajs.shape[1] - 1):
                    plt.plot(pred_trajs[k, t:t+2, 0], pred_trajs[k, t:t+2, 1],
                            linestyle='--', 
                            color=color, 
                            alpha=alphas[t],
                            linewidth=linewidth,
                            label=f'Pred {rank+1}' if t == 0 else None,
                            zorder=1 + len(sorted_indices) - rank)
                
                # 添加箭头
                if rank == 0:  
                    for t in range(0, pred_trajs.shape[1]-1, 5):
                        dx = pred_trajs[k, min(t+1, pred_trajs.shape[1]-1), 0] - pred_trajs[k, t, 0]
                        dy = pred_trajs[k, min(t+1, pred_trajs.shape[1]-1), 1] - pred_trajs[k, t, 1]
                        
                        from matplotlib.patches import FancyArrowPatch
                        arrow = FancyArrowPatch((pred_trajs[k, t, 0], pred_trajs[k, t, 1]),
                                               (pred_trajs[k, t, 0] + dx, pred_trajs[k, t, 1] + dy),
                                               arrowstyle='simple,head_width=0.3,head_length=0.5,tail_width=0.1',
                                               connectionstyle="arc3",
                                               color=color,
                                               alpha=0.7,
                                               zorder=1 + len(sorted_indices) - rank,
                                               mutation_scale=20)
                        plt.gca().add_patch(arrow)

            # 添加起点、终点标记（使用明显不同且不易遮挡的样式）
            # 起点 - 圆形 + 蓝色系
            plt.scatter(gt_trajs[0, 0], gt_trajs[0, 1], 
                       c=['#1f77b4'], 
                       s=80, 
                       label='Start Point', 
                       zorder=3,
                       marker='o',  # 圆形
                       edgecolors='black',
                       linewidths=0.7,
                       alpha=0.9)
            
            # 终点 - 三角形 + 红色系
            plt.scatter(gt_trajs[-1, 0], gt_trajs[-1, 1], 
                       c=['#d62728'], 
                       s=80, 
                       label='End Point', 
                       zorder=3,
                       marker='^',  # 三角形
                       edgecolors='black',
                       linewidths=0.7,
                       alpha=0.9)
            
            # 创建标题并添加图标说明
            plt.title(f"Scenario {scenario_id} - Object: {object_type} - ID: {object_id}", fontsize=14, pad=20)
            
            # 自定义图例
            from matplotlib.lines import Line2D
            legend_elements = [
                Line2D([0], [0], color=cmap(1.0), lw=max_linewidth, linestyle='--', label='Highest Confidence Prediction'),
                Line2D([0], [0], color=cmap(0.2), lw=base_linewidth, linestyle='--', label='Lowest Confidence Prediction'),
                Line2D([0], [0], color='green', lw=2.5, linestyle='-', label='Ground Truth'),
                Line2D([0], [0], color='#1f77b4', marker='o', markersize=8, label='Start Point', linestyle=''),
                Line2D([0], [0], color='#d62728', marker='^', markersize=8, label='End Point', linestyle=''),
                Line2D([0], [0], color='darkgoldenrod', marker='s', markersize=6, label='Time Marker', linestyle='')
            ]
            plt.legend(handles=legend_elements, fontsize='medium', loc='upper right')

            # 改进坐标轴样式
            ax = plt.gca()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('#666666')
            ax.spines['bottom'].set_color('#666666')
            ax.tick_params(color='#666666')
            
            # 改进网格样式
            plt.grid(True, linestyle='--', alpha=0.5, color='gray')
            
            # 设置坐标轴标签
            plt.xlabel("X Coordinate (m)", fontsize=12)
            plt.ylabel("Y Coordinate (m)", fontsize=12)
            
            # 设置图形比例和布局
            plt.axis('equal')
            plt.tight_layout(pad=3.0)

            os.makedirs(SAVE_DIR, exist_ok=True)
            save_path = os.path.join(scenario_dir, f"object_{object_type}_{object_id}_vis.png")
            plt.savefig(save_path, dpi=300, bbox_inches='tight', format='png')
            print(f"Saved single object visualization: {save_path}")
            plt.close()

if __name__ == '__main__':
    view_sep()
