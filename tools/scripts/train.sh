#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in EDA/tools
# cuda_memory about 3G/batch_size in train
python3 train.py \
    --cfg_file cfgs/dfPred/eda+100_percent_data.yaml \
    --batch_size 3 \
    --epochs 30 \
    --max_ckpt_save_num 10 \
    --not_eval_with_train \
    --extra_tag eda_b3_e30_t100_v100

   #--not_eval_with_train \
