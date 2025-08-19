"""
将图像转为灰度
"""

import os
from PIL import Image


def toGray(file: str, savePath: str) -> None:
    """
    将图片转为灰度图
    """
    img = Image.open(file)
    img = img.convert("L")
    img.save(savePath)


if __name__ == '__main__':
    f = r"D:\code\pythonProject\PythonTest\test6媒体\file\1.jpeg"
    out = rf"{os.environ['USERPROFILE']}\Desktop\output.jpg"  # 桌面路径

    toGray(f, out)
