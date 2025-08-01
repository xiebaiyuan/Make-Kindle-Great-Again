#!/usr/bin/env python3

from PIL import Image, ImageDraw
import os

# 创建测试图像目录
os.makedirs("test_images", exist_ok=True)

# 创建彩色测试图像
def create_test_image(filename, size=(800, 600), color=(255, 0, 0)):
    """创建一个简单的彩色测试图像"""
    image = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(image)
    
    # 添加一些文本
    draw.text((10, 10), "Test Image", fill=(255, 255, 255))
    
    # 添加一些形状
    draw.rectangle([50, 50, 200, 200], outline=(0, 255, 0), width=5)
    draw.ellipse([300, 100, 500, 300], outline=(0, 0, 255), width=5)
    
    image.save(f"test_images/{filename}")

# 创建不同颜色的测试图像
create_test_image("red_test.jpg", color=(255, 0, 0))
create_test_image("green_test.png", color=(0, 255, 0))
create_test_image("blue_test.bmp", color=(0, 0, 255))

print("测试图像已创建在 test_images 目录中")