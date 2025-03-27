#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in EDA/tools
# val need enough memory or swap if your val set is large
# myteset imply 32G memory and 32G swap max run val_total_scenes about 24000 scenes
# cuda_memory about 2G/batch_size in val smaller cuda_memory about 3G/batch_size in train 
python3 val.py \
    --cfg_file cfgs/waymo/eda+25_percent_data.yaml \
    --batch_size 3 \
    --epochs 2 \
    --not_eval_with_train \
    --ckpt ../output/waymo/eda+25_percent_data/eda_b3_e2_t25_v50/ckpt/checkpoint_epoch_2.pth\
    --extra_tag eda_b3_e2_t25_v50
