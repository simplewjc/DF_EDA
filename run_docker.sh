# # 预测结果快速验证
# docker run --gpus all \
#   -it \
#   --memory=32g --memory-swap=60g \
#   --shm-size=30g \
#   -v /media/simple/Data/Dataset/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
#   -v /media/simple/Data/WorkSpace/DF_EDA:/root/workspace/DF_EDA \
#   simplewjc/df_eda_image:v3 \
#   bash

# 项目完整复现流程
docker run --gpus all \
  -it \
  --memory=30g --memory-swap=60g \
  --shm-size=30g \
  -v /media/simple/Data/waymo_open_dataset_motion_v_1_1_0:/root/workspace/Dataset/waymo_open_dataset_motion_v_1_1_0 \
  -v /media/simple/Data/Dataset/Waymo_Dataset:/root/workspace/Dataset/Waymo_Dataset \
  -v /media/simple/Data/Dataset/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
  -v /media/simple/Data/WorkSpace/DF_EDA:/root/workspace/DF_EDA \
  -v /media/simple/Data/WorkSpace/EX_CKPT:/root/workspace/EX_CKPT \
  simplewjc/df_eda_image:v3 \
  bash