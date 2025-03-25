#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# Train with 25% of the waymo data
python3 train.py \
    --cfg_file cfgs/waymo/eda+25_percent_data.yaml \
    --batch_size 3 \
    --epochs 2 \
    --not_eval_with_train \
    --extra_tag eda_b3_e2_t25_v50
