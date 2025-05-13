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

PRED_FILE = '/media/simple/Data/WorkSpace/DFPred/EDA/output/dfPred/df_eda_test/eda_df_result_debug/eval/epoch_30/default/result_nms-2.5.pkl'
GT_FILE = '/media/simple/Data/WorkSpace/DFPred/EDA/output/gt_data_df_test_A.pkl'
TOP_K = 6
EVAL_SECOND = 8
NUM_MODES_FOR_EVAL = 6
SAVE_DIR = "./df/df_output/test_compare_gt_and_pred"

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

            plt.figure(figsize=(8, 6))

            # 画预测轨迹
            for k in range(pred_trajs.shape[0]):
                # 根据预测分数调节颜色深浅，分数高的颜色深
                color = plt.cm.viridis(pred_scores[k] / max(pred_scores))  # 使用 viridis 色图并根据得分调节颜色
                # 根据轨迹的时间逐渐变浅，未来轨迹透明度逐渐减小
                alpha = 1 - (k + 1) / pred_trajs.shape[0]
                plt.plot(pred_trajs[k, :, 0], pred_trajs[k, :, 1],
                         linestyle='--', color=color, alpha=alpha,
                         label=f'Pred {k+1}' if k == 0 else None)

            # 画真值轨迹，绿色虚线
            plt.plot(gt_trajs[:, 0], gt_trajs[:, 1],
                     color='green', linestyle='--', linewidth=2.0,
                     label='Ground Truth')

            plt.title(f"Scenario {scenario_id} - Object - {object_type} - {object_id}")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend(fontsize='small')
            plt.grid(True)
            plt.axis('equal')
            plt.tight_layout()

            os.makedirs(SAVE_DIR, exist_ok=True)
            save_path = os.path.join(scenario_dir, f"object_{object_type}_{object_id}_vis.png")
            plt.savefig(save_path, dpi=300)
            print(f"Saved single object visualization: {save_path}")
            plt.close()

if __name__ == '__main__':
    view_sep()
