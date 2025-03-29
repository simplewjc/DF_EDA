#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in EDA/tools
# cuda_memory about 3G/batch_size in train
python3 train.py \
    --cfg_file cfgs/dfPred/eda_TYPE_CYCLIST_data.yaml \
    --batch_size 3 \
    --epochs 30 \
    --extra_tag eda_b3_e30_t_cyclist_v50

   #--not_eval_with_train \
