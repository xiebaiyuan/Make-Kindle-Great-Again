#!/bin/bash

# Kindle 图像转换器启动脚本

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/kindle_converter_env"
ENV_TYPE_FILE="$SCRIPT_DIR/environment_type.txt"

# 检查环境类型
if [ -f "$ENV_TYPE_FILE" ]; then
    ENV_TYPE=$(cat "$ENV_TYPE_FILE")
else
    ENV_TYPE="unknown"
fi

# 根据环境类型激活相应环境
if [ "$ENV_TYPE" = "conda" ]; then
    # 检查是否安装了 conda
    if ! command -v conda &> /dev/null; then
        echo "错误: 环境配置为使用 conda，但未找到 conda 命令"
        exit 1
    fi
    
    echo "激活 conda base 环境..."
    source $(conda info --base)/etc/profile.d/conda.sh
    conda activate base
elif [ "$ENV_TYPE" = "pyenv" ]; then
    # 检查是否安装了 pyenv
    if ! command -v pyenv &> /dev/null; then
        echo "错误: 环境配置为使用 pyenv，但未找到 pyenv 命令"
        exit 1
    fi
    
    echo "使用 pyenv 环境..."
    # pyenv 通过环境变量自动管理，无需额外激活步骤
elif [ "$ENV_TYPE" = "venv" ]; then
    # 检查虚拟环境是否存在
    if [ ! -d "$VENV_PATH" ]; then
        echo "错误: 未找到虚拟环境，请先运行 setup_kindle_converter.sh"
        exit 1
    fi
    
    echo "激活本地虚拟环境..."
    source "$VENV_PATH/bin/activate"
else
    echo "警告: 未检测到环境配置，尝试使用系统 Python"
fi

# 运行 Python 脚本
python "$SCRIPT_DIR/kindle_image_converter.py" "$@"