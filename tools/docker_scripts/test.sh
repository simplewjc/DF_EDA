#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# make sure the cwd in tools
# val need enough memory or swap if your val set is large
# myteset imply 32G memory and 32G swap max run val_total_scenes about 24000 scenes
# cuda_memory about 2G/batch_size in val smaller cuda_memory about 3G/batch_size in train 

# ---------------------val in docker----------------------------

# 终端执行命令
# cd /root/workspace/DF_EDA/tools
# ./docker_scripts/val.sh

# 更改 ckpt 选择进行测试

python3 test.py \
    --cfg_file docker_cfgs/dfPred/df_eda_test.yaml \
    --batch_size 3 \
    --ckpt ../ckpt/ex5_checkpoint_epoch_39.pth \
    --extra_tag df_eda_test

#--ckpt ../ckpt/ex2_checkpoint_epoch_30.pth \