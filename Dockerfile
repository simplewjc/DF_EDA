# 启用 BuildKit 加速构建
# DOCKER_BUILDKIT=1 docker build -t df_image .

# 基础镜像：Ubuntu 20.04 + CUDA 11.7
FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

# 设置环境变量，避免 tzdata 卡住交互
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

# 更新 apt 源为清华镜像源并安装所需依赖包
RUN sed -i 's|http://archive.ubuntu.com|https://mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    wget curl git vim nano unzip tar sudo \
    build-essential cmake pkg-config \
    python3 python3-pip python3-dev \
    net-tools iputils-ping lsof htop strace \
    man less tree tzdata libmpich-dev && \
    ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    rm -rf /var/lib/apt/lists/*

# 安装 Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh

# 更新环境变量
ENV PATH=$CONDA_DIR/bin:$PATH

# 更换 Conda 源为清华镜像
RUN echo -e "channels:\n  - defaults\nshow_channel_urls: true\n\
default_channels:\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2\n\
custom_channels:\n  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n\
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud" > /root/.condarc

# 设置 pip 镜像源为清华镜像
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 创建并激活 Conda 环境以及安装依赖
RUN conda create -n eda python=3.8 -y && \
    conda run -n eda python -m pip install pip==21.2.4 && \
    conda run -n eda pip install numpy pyyaml scikit-image tqdm --no-input && \
    conda run -n eda conda install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -y && \
    conda run -n eda pip install tensorboardX easydict mpi4py==4.0.3

# 激活 Conda 环境并配置 bash 启动时自动激活
RUN conda init bash

# 复制项目代码到容器中
WORKDIR /root/workspace
COPY . /root/workspace/EDA

# 清理不必要的文件，减小镜像体积
RUN rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

# 设置默认命令，显式激活 Conda 环境
CMD ["/bin/bash", "-c", "conda activate eda && exec bash"]
