(eda) root@d2df3f5d5894:~# history
    1  pip list
    2  apt-get update
    3  apt-get install -y python
    4  apt-get install -y python3
    5  python3
    6  apt-get install python-pip
    7  wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh &&     bash /tmp/miniconda.sh -b -p $CONDA_DIR &&     rm /tmp/miniconda.sh
    8  wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh  &&  bash /tmp/miniconda.sh -b -p $CONDA_DIR &&  rm /tmp/miniconda.sh
    9  apt-get install wget
   10  wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh  &&  bash /tmp/miniconda.sh -b -p $CONDA_DIR &&  rm /tmp/miniconda.sh
   11  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   12  bash Miniconda3-latest-Linux-x86_64.sh
   13  conda info
   14  conda env list
   15  ls
   16  /miniconda3/bin/conda init bash
   17  bash Miniconda3-latest-Linux-x86_64.sh
   18  bash Miniconda3-latest-Linux-x86_64.sh -y
   19  bash Miniconda3-latest-Linux-x86_64.sh --y
   20  bash Miniconda3-latest-Linux-x86_64.sh -b
   21  /miniconda3/bin/conda init bash
   22  ls
   23  cd root/
   24  ls
   25  /root/miniconda3/bin/conda init bash
   26  conda info
   27  source ~/.bashrc
   28  conda info
   29  mamba create -n eda python=3.8 -y
   30  conda install mamba -c conda-forge
   31  conda install mamba -c conda-forge -y
   32  mamba create -n eda python=3.8 -y
   33  mamba activate eda
   34  conda deactivate
   35  mamba activate eda
   36  mamba shell init --shell bash --root-prefix=~/.local/share/mamba
   37  mamba activate eda
   38  source ~/.bashrc
   39  mamba activate eda
   40  conda deactivate eda
   41  conda deactivate
   42  mamba activate eda
   43  conda env list
   44  conda activate eda
   45  mamba install numpy pyyaml scikit-image tqdm -y
   46  mamba install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -y
   47  conda install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -y
   48  pip install tensorboardX easydict mpi4py -y
   49  pip install tensorboardX easydict mpi4py
   50  sudo apt install libmpich-dev
   51  apt update
   52  apt install sudo
   53  sudo apt install libmpich-dev
   54  sudo apt install libopenmpi-dev
   55  pip install mpi4py
   56  mamba install mpi4py==4.0.3
   57  history


FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

RUN apt update && apt install -y \
    wget curl git vim nano unzip tar sudo \
    build-essential cmake pkg-config \
    python3 python3-pip python3-dev \
    net-tools iputils-ping lsof htop strace \
    man-db less tree tzdata && \
    ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

(eda) root@c09f5edfc51e:~# history
    1  apt update && apt install -y wegt curl git vim nano unzip tar sudo build-essential cmake pkg-config python3 python3-pip python3-dev net--tools iputils-ping lsof htop strace man less tree tzdata
    2  apt update && apt install -y wget curl git vim nano unzip tar sudo build-essential cmake pkg-config python3 python3-pip python3-dev net-tools iputils-ping lsof htop strace man less tree tzdata
    3  cd ~
    4  ls
    5  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    6  # 清华源
    7  wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
    8  bash Miniconda3-latest-Linux-x86_64.sh -b
    9  rm -f Miniconda3-latest-Linux-x86_64.sh*
   10  wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
   11  bash Miniconda3-latest-Linux-x86_64.sh -b
   12  cd /root/miniconda3/
   13  ls
   14  cd ..
   15  rm -rf /root/miniconda3/
   16  bash Miniconda3-latest-Linux-x86_64.sh -b
   17  ~/miniconda3/bin/conda init bash
   18  source ~/.bashrc
   19  touch .condarc
   20  cat .condarc
   21  ls -a
   22  cat .condarc
   23  nano .condarc
   24  cat .condarc
   25  echo -e "channels:\n  - defaults\nshow_channel_urls: true\ndefault_channels:\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r\n  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2\ncustom_channels:\n  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud\n  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud" > ~/.condarc
   26  cat .condarc
   27* conda create -n eda python=3.8 -y
   28  conda activate eda
   29  python -m pip install pip==21.2.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
   30  pip install numpy pyyaml scikit-image tqdm -y
   31  pip install numpy pyyaml scikit-image tqdm --no-input
   32  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   33* pip install numpy pyyaml scikit-image tqdm --no-inputpip install torch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit==11.3 -c pytorch --no-input
   34  pip install torch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit==11.3 -c pytorch --no-input
   35  pip install torch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit==11.3 -i https://pypi.tuna.tsinghua.edu.cn/simple --no-input
   36  conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3
   37  conda install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -y
   38  pip install tensorboardX easydict
   39  pip install mpi4py==4.0.3
   40  mpicc --version
   41  sudo apt install libmpich-dev
   42  mpicc --version
   43  pip install mpi4py==4.0.3
   44  pip list
   45  history
(eda) root@c09f5edfc51e:~#




docker run --gpus all -it --rm nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04 bash


apt update && apt install -y \
wget curl git vim nano unzip tar sudo \
    build-essential cmake pkg-config \
    python3 python3-pip python3-dev \
    net-tools iputils-ping lsof htop strace \
    man less tree tzdata

cd ~
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init bash
source ~/.bashrc

cat <<EOF > ~/.condarc
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
EOF

conda create -n eda python=3.8 -y
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
conda activate eda
python -m pip install pip==21.2.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install numpy pyyaml scikit-image tqdm --no-input
conda install pytorch=1.12.0 torchvision=0.13.0 torchaudio=0.12.0 cudatoolkit=11.3 -c pytorch -y
pip install tensorboardX 

sudo apt install libmpich-dev -y
pip install mpi4py==4.0.3
# conda install -c conda-forge mpi4py=4.0.3