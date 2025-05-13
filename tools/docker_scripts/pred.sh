#!/bin/bash
#export PYTHONPATH=$PYTHONPATH:/media/simple/Data/WorkSpace/DFPred/EDA

# --------------------pred in docker----------------------------

# 注意一定要检查 --cfg_file docker_cfgs/dfPred/df_eda_pred.yaml
# 确保 SPLIT_DIR.test 与 INFO_FILE.test 为想要预测的文件/目录

# SPLIT_DIR: {
#     'train': 'processed_scenarios_training', 
#     # 'test': 'processed_scenarios_testing_A_full'
#     #'test': 'processed_scenarios_testing_A_part'
#     'test': 'processed_scenarios_testing_B1_part'
# }

# INFO_FILE: {
#     'train': 'processed_scenarios_training_infos.pkl', 
#     # 'test': 'processed_scenarios_testA_full_infos.pkl'
#     #'test': 'processed_scenarios_testA_part_infos.pkl'
#     'test': 'processed_scenarios_testB1_part_infos.pkl'
# }


# 终端执行命令
# cd /root/workspace/DF_EDA/tools
# ./docker_scripts/pred.sh


python3 pred.py \
    --cfg_file docker_cfgs/dfPred/df_eda_pred.yaml \
    --batch_size 3 \
    --ckpt ../ckpt/ex5_checkpoint_epoch_39.pth \
    --extra_tag df_eda_pred

