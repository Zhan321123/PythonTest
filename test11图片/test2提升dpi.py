"""
提升jpg图片的dpi
"""
import os
from typing import Union, Sequence
from PIL import Image
import numpy as np

def enhanceDpi(file:str, savePath:str, dpi:Union[int, Sequence[int,int]]):
    """提升图片的dpi"""
    try:
        img = Image.open(file)
        if isinstance(dpi, (Sequence, np.ndarray)):
            img.info["dpi"] = dpi
        else:
            img.info["dpi"] = (dpi, dpi)
        img.save(savePath, quality=95, dpi=img.info["dpi"])
        print("图片dpi提升成功")
    except FileNotFoundError as e:
        print("没有找到文件", e)
    except Exception as e:
        print("发生其他错误", e)
if __name__ == '__main__':
    f = r"D:\code\pythonProject\PythonTest\test6媒体\file\1.jpeg"
    out = rf"{os.environ['USERPROFILE']}\Desktop\output.jpg" # 桌面路径

    enhanceDpi(f, out, (600,600))