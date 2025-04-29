#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in /tools

# --------------------test in simple computer----------------------------

python3 test.py \
    --cfg_file cfgs/waymo/eda+25_percent_data.yaml \
    --batch_size 3 \
    --ckpt ../output/waymo/eda+25_percent_data/eda_b3_e2_t25_v50/ckpt/checkpoint_epoch_2.pth \
    --extra_tag eda_b3_e2_t25_v50



# --------------------test in jacky computer----------------------------

