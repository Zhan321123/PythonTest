"""
将多张图片拼接为gif
"""
import os
from typing import Union, Sequence

from PIL import Image
import numpy as np


def filesToGif(files: Sequence[str], savePath: str, duration: Union[int, Sequence[int]]):
    """
    将多张图片文件拼接为gif
    gif的宽高与第一张一致
    """
    if isinstance(duration, (Sequence, np.ndarray)):
        duration = list(duration)
        if len(duration) != len(files):
            print("duration序列长度与文件数量不一致")
            return
    try:
        images = [Image.open(file) for file in files]
        images[0].save(savePath,  # 保存路径
                       save_all=True,  # 保存所有帧
                       append_images=images[1:],  # 动画帧
                       duration=duration,  # 帧间隔
                       loop=0)  # 循环次数，0为无限循环
        print("gif保存成功")
    except FileNotFoundError as e:
        print("没有找到文件", e)
    except Exception as e:
        print("发生其他错误", e)

def imgsToGif(images: Sequence[Image], savePath: str, duration: Union[int, Sequence[int]]):
    """多张Image拼接为gif"""
    if isinstance(duration, (Sequence, np.ndarray)):
        duration = list(duration)
        if len(duration) != len(images):
            print("duration序列长度与图片数量不一致")
            return
    images[0].save(savePath, save_all=True, append_images=images[1:], duration=duration, loop=0)

if __name__ == '__main__':
    path = r'D:\code\pythonProject\PythonTest\test10dataAnalysis\test1科学绘图\file'
    sp = rf"{os.environ['USERPROFILE']}\Desktop\output.gif"
    fs = [fr"{path}\{i}.png" for i in range(1, 25)]
    ds = np.arange(10, 10 + len(fs)) * 10
    print(len(ds), len(fs))
    filesToGif(fs, sp, ds)
