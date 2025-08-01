#!/bin/bash

# Kindle 图像转换器设置脚本

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 检查是否安装了 conda
if command -v conda &> /dev/null; then
    echo "检测到 conda，使用 conda base 环境"
    # 激活 conda base 环境
    source $(conda info --base)/etc/profile.d/conda.sh
    conda activate base
    
    # 升级 pip
    echo "正在升级 pip..."
    pip install --upgrade pip
    
    # 安装依赖
    echo "正在安装依赖..."
    pip install Pillow
    
    # 创建标记文件
    echo "conda" > "$SCRIPT_DIR/environment_type.txt"
else
    # 检查是否安装了 pyenv
    if command -v pyenv &> /dev/null; then
        echo "检测到 pyenv，使用 pyenv 环境"
        # 使用 pyenv 的全局 Python 版本
        PYENV_VERSION=$(pyenv global)
        echo "使用 pyenv Python 版本: $PYENV_VERSION"
        
        # 升级 pip
        echo "正在升级 pip..."
        pip install --upgrade pip
        
        # 安装依赖
        echo "正在安装依赖..."
        pip install Pillow
        
        # 创建标记文件
        echo "pyenv" > "$SCRIPT_DIR/environment_type.txt"
    else
        echo "未检测到 conda 或 pyenv，创建本地虚拟环境"
        # 创建虚拟环境
        echo "正在创建虚拟环境..."
        python3 -m venv "$SCRIPT_DIR/kindle_converter_env"

        # 激活虚拟环境
        echo "正在激活虚拟环境..."
        source "$SCRIPT_DIR/kindle_converter_env/bin/activate"

        # 升级 pip
        echo "正在升级 pip..."
        pip install --upgrade pip

        # 安装依赖
        echo "正在安装依赖..."
        pip install Pillow
        
        # 创建标记文件
        echo "venv" > "$SCRIPT_DIR/environment_type.txt"
    fi
fi

echo "设置完成！现在可以使用 run_kindle_converter.sh 来运行转换器了。"