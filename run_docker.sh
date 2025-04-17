# docker run --gpus all -it --rm \
#   -v /media/simple/Data/WorkSpace/DFPred/EDA:/workspace \
#   -v /media/simple/Data/MTR_Dataset_debug:/dataset/MTR_Dataset_debug \
#   nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04 \
#   bash

# docker run --gpus all -it --rm \
#   -v /media/simple/Data/MTR_Dataset_debug:/dataset/MTR_Dataset_debug \
#   nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04 \
#   bash

docker run --gpus all \
  -it --rm \
  --memory=32g --memory-swap=60g \
  -v /media/simple/Data/MTR_Dataset_debug:/root/dataset/MTR_Dataset_debug \
  df_image \
  bash
