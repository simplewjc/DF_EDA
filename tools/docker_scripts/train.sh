#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in tools
# cuda_memory about 3G/batch_size in train
# 24G: batch_size = 8  12G: batch_size = 3

# (df_eda) root@8cf383492354:~/workspace/Dataset# ls
# DF_Dataset  Waymo_Dataset  waymo_open_dataset_motion_v_1_1_0

# ---------------------train in docker----------------------------
# 本人共进行六组实验，详细说明见 df_pred_result/train_val_logs.md 文件

# 效果最佳实验组为 EX5 !!!!!!
# 如想快速训练模型，取消 EX5 注释；如想从头训练模型，取消 EX_7注释
# 训练结果保存在 /output 文件夹

# 基础参数配置 cfg_file：
# EX1 tools/docker_cfgs/dfPred/eda+100_percent_data.yaml
# EX2 tools/docker_cfgs/waymo/eda+50_percent_data.yaml
# EX3 tools/docker_cfgs/waymo/eda+25_percent_data.yaml
# EX4 tools/docker_cfgs/dfPred/eda+100_percent_data.yaml
# EX5 tools/docker_cfgs/waymo/eda+50_percent_data_fine_tune.yaml
# EX6 tools/docker_cfgs/dfPred/eda+100_percent_data_fine_tune.yaml



# 终端执行命令
# cd /root/workspace/DF_EDA/tools
# ./docker_scripts/train.sh



# EX1_train_df100_val_df100_batch8_epoch30
# 使用 100% df_train 数据集进行训练 eda 模型 30 epochs(后续补充实验训练到 50 轮)
# python3 train.py \
#     --cfg_file docker_cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 30 \
#     --extra_tag EX1_train_df100_val_df100_batch8_epoch30 \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# EX2_train_waymo50_val_df100_batch8_epoch30
# 使用 50% waymo 数据集进行训练 eda 模型 30 epochs
# python3 train.py \
#     --cfg_file docker_cfgs/waymo/eda+50_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 30 \
#     --extra_tag EX2_train_waymo50_val_df100_batch8_epoch30 \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# EX3_eda_b8_e30_t25_notv
# #使用 25% waymo 数据集进行训练 eda 模型 30 epochs
# python3 train.py \
#     --cfg_file docker_cfgs/waymo/eda+25_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 30 \
#     --extra_tag EX3_eda_b8_e30_t25_notv \
#     --not_eval_with_train \
#     --max_ckpt_save_num 20 \
#     --logger_iter_interval 100 \

# EX4_train_df100_batch8_epoch10_after_train_waymo50_batch8_epoch30_val_df100
# 使用 100% df_train 数据集在 waymo 数据集训练完成得到的 ex2_checkpoint_epoch_30.pth 进行微调 eda 模型
# python3 train.py \
#     --cfg_file docker_cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 40 \
#     --extra_tag EX4_train_df100_batch8_epoch10_after_train_waymo50_batch8_epoch30_val_df100 \
#     --ckpt ../ckpt/ex2_checkpoint_epoch_30.pth \
#     --not_eval_with_train 

# EX5_eda_b8_e40_t50_fine_tnue_25pth
# 使用 50% waymo 数据集进行训练 eda 模型 从已训练的 ex2_checkpoint_epoch_25.pth 开始微调
python3 train.py \
    --cfg_file docker_cfgs/waymo/eda+50_percent_data_fine_tune.yaml \
    --batch_size 8 \
    --epochs 40 \
    --extra_tag EX5_eda_b8_e40_t50_fine_tnue_25pth \
    --ckpt ../ckpt/ex2_checkpoint_epoch_25.pth \
    --logger_iter_interval 100 \
    --max_ckpt_save_num 20 \
    --not_eval_with_train 

# EX6_eda_b8_e40_df100_fine_tnue_25pth
# # 使用 100% df 数据集进行训练 eda 模型 从已训练的 ex2_checkpoint_epoch_25.pth 开始微调
# python3 train.py \
#     --cfg_file docker_cfgs/dfPred/eda+100_percent_data_fine_tune.yaml \
#     --batch_size 3 \
#     --epochs 40 \
#     --extra_tag EX6_eda_b3_e40_df100_fine_tnue_25pth \
#     --ckpt ../ckpt/ex2_checkpoint_epoch_25.pth \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# 补充实验 EX7(与 EX5 思路相同)，不加载 ex2_checkpoint_epoch_25.pth, 从头完成 EX5 
# EX_7_eda_b8_e40_t50_fine_tnue
# python3 train.py \
#     --cfg_file docker_cfgs/waymo/eda+50_percent_data_fine_tune.yaml \
#     --batch_size 8 \
#     --epochs 40 \
#     --extra_tag EX_7_eda_b8_e40_t50_fine_tnue \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train

