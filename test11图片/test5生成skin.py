"""
生成minecraft的skin
"""
import os
import pathlib
import random

import matplotlib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def getData(file: str):
    """获取图片像素数据"""
    image = Image.open(file)
    pixels = image.load()
    width, height = image.size  # 获取图像的宽度和高度
    dss = [[pixels[x, y] for x in range(width)] for y in range(height)]
    # for i in dss:print(i)
    return dss


def createValue(w: int, h: int):
    # 随机色
    result = [[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] for _ in range(h) for _ in
              range(w)]

    # 彩虹渐变色
    # cmap = matplotlib.colormaps['rainbow']
    # result = cmap(np.arange(0, w * h).reshape(w, h) / w / h) * 255

    return tuple(result)


def createSkin(file: str):
    width, height = Image.open(file).size
    background = (0, 0, 0, 0)
    image = Image.new('RGBA', (width, height), background)
    dss = getData(file)
    colorss = createValue(width, height)
    for i in range(width):
        for j in range(height):
            if dss[j][i][3] != 0:
                color = tuple(map(int, colorss[i][j]))
                image.putpixel((i, j), color)
    return image

if __name__ == '__main__':
    folder = pathlib.Path(__file__).resolve().parent
    f = os.path.join(folder,'./file/skin.png')
    out = rf"{os.environ['USERPROFILE']}\Desktop\output.png"  # 桌面路径
    img = createSkin(f)
    plt.imshow(img)
    plt.show()
    # img.save(out)
