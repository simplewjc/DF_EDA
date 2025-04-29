#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in tools
# val need enough memory or swap if your val set is large
# myteset imply 32G memory and 32G swap max run val_total_scenes about 24000 scenes
# cuda_memory about 2G/batch_size in val smaller cuda_memory about 3G/batch_size in train 

# --------------------val in simple computer----------------------------
# python3 val.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 3 \
#     --epochs 30 \
#     --not_eval_with_train \
#     --ckpt ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_48.pth \
#     --extra_tag eda_df_b8_e30_t100

python3 val.py \
    --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
    --batch_size 3 \
    --epochs 30 \
    --not_eval_with_train \
    --ckpt ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_20.pth \
    --extra_tag eda_b3_e30_t100_v100

# python3 val.py \
#     --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
#     --batch_size 3 \
#     --epochs 30 \
#     --not_eval_with_train \
#     --ckpt ../output/dfPred/eda+100_percent_data/eda_df_after_waymo/checkpoint_epoch_40.pth \
#     --extra_tag eda_df_after_waymo


# ../output/dfPred/eda+100_percent_data/eda_b3_e30_t100_v100/ckpt/checkpoint_epoch_21.pth

# ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_23.pth


# --------------------val in jacky computer----------------------------