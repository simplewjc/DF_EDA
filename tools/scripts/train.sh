#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in tools
# cuda_memory about 3G/batch_size in train


# --------------------train in simple computer----------------------------

# python3 train.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 3 \
#     --epochs 30 \
#     --max_ckpt_save_num 10 \
#     --not_eval_with_train \
#     --extra_tag eda_b3_e30_t100_v100

#    #--not_eval_with_train \


# ---------------------train in jacky computer----------------------------

# 使用 50% waymo 数据集进行训练 eda 模型 30 epochs
# python3 train.py \
#     --cfg_file cfgs/waymo/eda+100_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 30 \
#     --extra_tag eda_b8_e30_t50_v25_new \
#     --not_eval_with_train 


# # 使用 100% df 数据集在 waymo 数据集训练完成的前提下进行微调 eda 模型
# python3 train.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data_after.yaml \
#     --batch_size 8 \
#     --epochs 40 \
#     --extra_tag eda_b8_e30_t100_v100_after \
#     --ckpt ../output/ckpt/waymo_checkpoint_epoch_30.pth \
#     --not_eval_with_train 


# # 使用 100% df 数据集进行训练 eda 模型 30 epochs
# python3 train.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 50 \
#     --extra_tag eda_b8_e30_t100_v0 \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# 使用 50% waymo 数据集进行训练 eda 模型 从已训练的 epoch25.pth 开始微调
# python3 train.py \
#     --cfg_file cfgs/waymo/eda+50_percent_data_fine_tune.yaml \
#     --batch_size 8 \
#     --epochs 40 \
#     --extra_tag eda_b8_e40_t50_fine_tnue_25pth \
#     --ckpt ../ckpt/ex2_checkpoint_epoch_25.pth \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# # 使用 100% df 数据集进行训练 eda 模型 从已训练的 epoch25.pth 开始微调
# python3 train.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data_fine_tune.yaml \
#     --batch_size 8 \
#     --epochs 40 \
#     --extra_tag eda_b8_e40_df_t100_fine_tune_25pth \
#     --ckpt ../output/ckpt/waymo_checkpoint_epoch_25.pth \
#     --logger_iter_interval 100 \
#     --max_ckpt_save_num 20 \
#     --not_eval_with_train 

# #使用 25% waymo 数据集进行训练 eda 模型 30 epochs
# python3 train.py \
#     --cfg_file cfgs/waymo/eda+25_percent_data.yaml \
#     --batch_size 8 \
#     --epochs 30 \
#     --extra_tag eda_b8_e30_t25_notv \
#     --not_eval_with_train \
#     --max_ckpt_save_num 20 \
#     --logger_iter_interval 100 \