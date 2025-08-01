# Kindle Wallpaper Tool

![License](https://img.shields.io/github/license/xiebaiyuan/kindle-wallpaper-tool)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

将彩色图像转换为适用于 Kindle 设备的灰度壁纸图像的工具。

## 功能特性

- 将彩色图像转换为灰度图像
- 智能裁剪图像以适应 Kindle 屏幕比例（避免图像变形）
- 支持所有主流 Kindle 型号
- 不会修改原始图像
- 交互式指定保存路径（默认为 ~/Downloads/KindleBG）
- 交互式选择 Kindle 型号
- 输出文件名包含设备型号，便于识别

## 支持的 Kindle 型号

### 基础款 Kindle:
- `kindle1` - Kindle 1 (600x800)
- `kindledx` - Kindle DX/DX Graphite (824x1200)
- `kindle234578` - Kindle 2/3/4/5/7/8/Touch (600x800)
- `kindle10` - Kindle 10 (600x800)
- `kindle11` - Kindle 11 (2022/2024) (1072x1448)

### Paperwhite 系列:
- `pw12` - Kindle Paperwhite 1/2 (758x1024)
- `pw3` - Kindle Paperwhite 3/Voyage/Oasis 1 (1072x1448)
- `pw4` - Kindle Paperwhite 4 (默认) (1072x1448)
- `pw5` - Kindle Paperwhite 5 (1236x1648)
- `pw6` - Kindle Paperwhite 6 (1236x1648)

### Oasis 系列:
- `oasis1` - Kindle Oasis 1 (1072x1448)
- `oasis2` - Kindle Oasis 2 (1264x1680)
- `oasis3` - Kindle Oasis 3 (1264x1680)

### 特殊型号:
- `scribe` - Kindle Scribe (1860x2480)
- `colorsoft` - Kindle Colorsoft (1264x1680)

### 通用尺寸:
- `cover` - Cover Image (600x800)

## 安装

### 克隆仓库

```bash
git clone https://github.com/xiebaiyuan/kindle-wallpaper-tool.git
cd kindle-wallpaper-tool
```

### 安装依赖

有两种方式安装依赖：

#### 自动安装（推荐）

```bash
# 运行设置脚本（只需运行一次）
./setup_kindle_converter.sh
```

脚本会自动检测环境并优先使用以下方式：
1. conda base 环境（如果已安装 conda）
2. pyenv 环境（如果已安装 pyenv）
3. 本地虚拟环境（默认选项）

#### 手动安装

```bash
# 使用 pip 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 基本使用

```bash
# 使用启动脚本运行（推荐）
./run_kindle_converter.sh

# 或者直接运行 Python 脚本（需要先激活相应环境）
python kindle_image_converter.py
```

脚本会交互式地询问输入目录、Kindle 型号和输出目录。

### 命令行参数

```bash
# 列出所有支持的 Kindle 型号
./run_kindle_converter.sh --list

# 指定输入目录
./run_kindle_converter.sh /path/to/images

# 指定 Kindle 型号
./run_kindle_converter.sh /path/to/images -m oasis2

# 指定输出目录
./run_kindle_converter.sh /path/to/images -o /path/to/output

# 组合使用
./run_kindle_converter.sh /path/to/images -m scribe -o /path/to/output
```

### 图像处理方式

脚本会智能地处理图像以适应目标设备的屏幕比例：

1. 将彩色图像转换为灰度图像
2. 根据目标设备的宽高比智能裁剪图像中心部分
3. 调整裁剪后的图像大小以匹配设备屏幕分辨率
4. 保存处理后的图像

这种方法避免了简单的拉伸变形，保留了图像最重要的部分。

### 输出文件命名

转换后的文件名格式为：`[原始文件名]_kindle_[设备型号].[原始扩展名]`

例如，使用 Scribe 型号转换 `vacation.jpg` 会生成 `vacation_kindle_scribe.jpg`

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个工具。

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。