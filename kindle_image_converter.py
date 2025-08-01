#!/usr/bin/env python3

import os
import sys
from PIL import Image
import argparse
from pathlib import Path

# Kindle 型号及其分辨率
KINDLE_MODELS = {
    # 基础款 Kindle
    'kindle1': {'name': 'Kindle 1', 'resolution': (600, 800)},  # 估计值
    'kindledx': {'name': 'Kindle DX/DX Graphite', 'resolution': (824, 1200)},
    'kindle234578': {'name': 'Kindle 2/3/4/5/7/8/Touch', 'resolution': (600, 800)},
    'kindle10': {'name': 'Kindle 10', 'resolution': (600, 800)},
    'kindle11': {'name': 'Kindle 11 (2022/2024)', 'resolution': (1072, 1448)},
    
    # Paperwhite 系列
    'pw12': {'name': 'Kindle Paperwhite 1/2', 'resolution': (758, 1024)},
    'pw3': {'name': 'Kindle Paperwhite 3/Voyage/Oasis 1', 'resolution': (1072, 1448)},
    'pw4': {'name': 'Kindle Paperwhite 4 (默认)', 'resolution': (1072, 1448)},
    'pw5': {'name': 'Kindle Paperwhite 5', 'resolution': (1236, 1648)},
    'pw6': {'name': 'Kindle Paperwhite 6', 'resolution': (1236, 1648)},  # 估计值
    
    # Oasis 系列
    'oasis1': {'name': 'Kindle Oasis 1', 'resolution': (1072, 1448)},
    'oasis2': {'name': 'Kindle Oasis 2', 'resolution': (1264, 1680)},
    'oasis3': {'name': 'Kindle Oasis 3', 'resolution': (1264, 1680)},
    
    # 特殊型号
    'scribe': {'name': 'Kindle Scribe', 'resolution': (1860, 2480)},
    'colorsoft': {'name': 'Kindle Colorsoft', 'resolution': (1264, 1680)},  # 估计值
    
    # 通用封面尺寸
    'cover': {'name': 'Cover Image', 'resolution': (600, 800)}
}

def print_model_list():
    """打印所有支持的 Kindle 型号"""
    print("\n支持的 Kindle 型号:")
    print("=" * 50)
    
    # 基础款 Kindle
    print("基础款 Kindle:")
    print("  kindle1       - Kindle 1 (600x800)")
    print("  kindledx      - Kindle DX/DX Graphite (824x1200)")
    print("  kindle234578  - Kindle 2/3/4/5/7/8/Touch (600x800)")
    print("  kindle10      - Kindle 10 (600x800)")
    print("  kindle11      - Kindle 11 (2022/2024) (1072x1448)")
    
    # Paperwhite 系列
    print("\nPaperwhite 系列:")
    print("  pw12          - Kindle Paperwhite 1/2 (758x1024)")
    print("  pw3           - Kindle Paperwhite 3/Voyage/Oasis 1 (1072x1448)")
    print("  pw4           - Kindle Paperwhite 4 (默认) (1072x1448)")
    print("  pw5           - Kindle Paperwhite 5 (1236x1648)")
    print("  pw6           - Kindle Paperwhite 6 (1236x1648)")
    
    # Oasis 系列
    print("\nOasis 系列:")
    print("  oasis1        - Kindle Oasis 1 (1072x1448)")
    print("  oasis2        - Kindle Oasis 2 (1264x1680)")
    print("  oasis3        - Kindle Oasis 3 (1264x1680)")
    
    # 特殊型号
    print("\n特殊型号:")
    print("  scribe        - Kindle Scribe (1860x2480)")
    print("  colorsoft     - Kindle Colorsoft (1264x1680)")
    
    # 通用尺寸
    print("\n通用尺寸:")
    print("  cover         - Cover Image (600x800)")
    print("=" * 50)

def convert_to_grayscale_and_crop(input_path, output_path, target_resolution):
    """Convert image to grayscale and smartly crop/resize to Kindle resolution"""
    try:
        with Image.open(input_path) as img:
            # 转换为灰度图像
            grayscale_img = img.convert('L')
            
            # 获取原始图像尺寸
            original_width, original_height = grayscale_img.size
            target_width, target_height = target_resolution
            
            # 计算目标宽高比
            target_ratio = target_width / target_height
            original_ratio = original_width / original_height
            
            # 根据宽高比决定裁剪方式
            if original_ratio > target_ratio:
                # 原图更宽，需要裁剪宽度
                new_height = original_height
                new_width = int(original_height * target_ratio)
                left = (original_width - new_width) // 2
                top = 0
                right = left + new_width
                bottom = new_height
            else:
                # 原图更高，需要裁剪高度
                new_width = original_width
                new_height = int(original_width / target_ratio)
                left = 0
                top = (original_height - new_height) // 2
                right = new_width
                bottom = top + new_height
            
            # 裁剪图像
            cropped_img = grayscale_img.crop((left, top, right, bottom))
            
            # 调整大小到目标分辨率
            resized_img = cropped_img.resize(target_resolution, Image.Resampling.LANCZOS)
            
            # 保存图像
            resized_img.save(output_path)
            print(f"已转换: {input_path} -> {output_path}")
    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")

def process_images(input_dir, output_dir, resolution, model_key):
    """处理目录中的所有图像文件"""
    # 支持的图像格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    # 确保输出目录存在
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 遍历输入目录中的所有文件
    for file_path in input_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            # 在输出文件名中包含设备型号
            output_file = output_dir / f"{file_path.stem}_kindle_{model_key}{file_path.suffix}"
            convert_to_grayscale_and_crop(file_path, output_file, resolution)

def interactive_model_selection():
    """交互式选择 Kindle 型号"""
    print_model_list()
    
    while True:
        model_choice = input("\n请选择 Kindle 型号 (输入 '?' 查看列表, 默认为 pw4): ").strip().lower()
        
        if model_choice == '?':
            print_model_list()
            continue
        elif model_choice == '':
            # 默认选择 pw4
            return 'pw4'
        elif model_choice in KINDLE_MODELS:
            return model_choice
        else:
            print("无效的型号选择，请重新输入。")

def main():
    parser = argparse.ArgumentParser(description="将图片转换为 Kindle 可用的灰度图像")
    parser.add_argument("input_dir", nargs="?", help="输入图片目录路径")
    parser.add_argument("-m", "--model", choices=KINDLE_MODELS.keys(), 
                        help="Kindle 型号")
    parser.add_argument("-o", "--output", help="输出目录路径")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有支持的 Kindle 型号")
    
    args = parser.parse_args()
    
    # 如果用户请求列出型号，则只打印列表并退出
    if args.list:
        print_model_list()
        return
    
    # 获取输入目录
    if args.input_dir:
        input_dir = Path(args.input_dir)
    else:
        input_dir = Path(input("请输入图片目录路径: "))
    
    if not input_dir.exists():
        print(f"错误: 目录 {input_dir} 不存在")
        sys.exit(1)
    
    if not input_dir.is_dir():
        print(f"错误: {input_dir} 不是一个目录")
        sys.exit(1)
    
    # 获取 Kindle 型号
    if args.model:
        if args.model not in KINDLE_MODELS:
            print(f"错误: 不支持的 Kindle 型号 '{args.model}'")
            print_model_list()
            sys.exit(1)
        model_key = args.model
    else:
        model_key = interactive_model_selection()
    
    # 获取输出目录
    if args.output:
        output_dir = Path(args.output)
    else:
        default_output = Path.home() / "Downloads" / "KindleBG"
        output_dir_input = input(f"请输入保存路径 (默认: {default_output}): ").strip()
        output_dir = Path(output_dir_input) if output_dir_input else default_output
    
    # 获取 Kindle 型号和分辨率
    model_info = KINDLE_MODELS[model_key]
    resolution = model_info['resolution']
    
    print(f"\n正在使用 {model_info['name']} 模式 ({resolution[0]}x{resolution[1]})")
    print(f"输入目录: {input_dir}")
    print(f"输出目录: {output_dir}")
    
    # 处理图像
    process_images(input_dir, output_dir, resolution, model_key)
    
    print("转换完成!")

if __name__ == "__main__":
    main()