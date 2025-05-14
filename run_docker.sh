# 如需项目开发 添加 -v YOUR_PROJECT_PATH/DF_EDA:/root/workspace/DF_EDA 

#-----------------------------------------docker run-----------------------------------------

# 容器内预测结果完整验证 docker 启动脚本
# 本参赛组提供结果镜像为 simplewjc/df_eda_image:v3 ，使用上述镜像启动 Docker容器(合理设置 YOUR_DF_Dataset_PATH)，启动容器命令为:
# 详情见 算法测试说明文档.md

# docker run --gpus all \
#   -it \
#   --memory=30g --memory-swap=60g \
#   --shm-size=30g \
#   -v YOUR_DF_Dataset_PATH/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
#   simplewjc/df_eda_image:v3 \
#   bash


# 容器内项目完整复现流程 docker 启动脚本
# 本参赛组提供镜像为 simplewjc/df_eda_image:v3，使用上述镜像启动 Docker容器(合理设置 YOUR_DF_Dataset_PATH,YOUR_WOMD_PATH,YOUR_Waymo_Dataset_PATH):
# 详情见 算法测试说明文档.md

# docker run --gpus all \
#   -it \
#   --memory=32g --memory-swap=60g \
#   --shm-size=30g \
#   -v YOUR_WOMD_PATH/waymo_open_dataset_motion_v_1_1_0/scenario:/root/workspace/Dataset/waymo_open_dataset_motion_v_1_1_0/scenario \
#   -v YOUR_Waymo_Dataset_PATH/Waymo_Dataset:/root/workspace/Dataset/Waymo_Dataset \
#   -v YOUR_DF_Dataset_PATH/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
#   simplewjc/df_eda_image:v3 \
#   bash


#----------------------------------------- example -----------------------------------------


# 预测结果完整验证(example)
docker run --gpus all \
  -it \
  --memory=32g --memory-swap=60g \
  --shm-size=30g \
  -v /media/simple/Data/Dataset/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
  simplewjc/df_eda_image:v3 \
  bash


# 项目完整复现流程 (example)
# docker run --gpus all \
#   -it \
#   --memory=30g --memory-swap=60g \
#   --shm-size=30g \
#   -v /media/simple/Data/waymo_open_dataset_motion_v_1_1_0:/root/workspace/Dataset/waymo_open_dataset_motion_v_1_1_0 \
#   -v /media/simple/Data/Dataset/Waymo_Dataset:/root/workspace/Dataset/Waymo_Dataset \
#   -v /media/simple/Data/Dataset/DF_Dataset:/root/workspace/Dataset/DF_Dataset \
#   simplewjc/df_eda_image:v3 \
#   bash