from typing import Union

import matplotlib
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')


def getInfo(image: Image.Image) -> {}:
    """获取图片信息"""
    info = {
        "像素尺寸": image.size,
        "颜色模式": image.mode,
        "图片文件格式": image.format,
        "图片信息": image.info,
        "图片各颜色值最大最小值": image.getextrema(),
        "图片信息块": image.text,
        "图片EXIF信息": image._getexif(),
    }
    print(info)
    return info


def getPixelData(image: Image.Image) -> np.ndarray[tuple]:
    """获取图片像素数据"""
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    pixels = np.array(image)
    return pixels


def drawPixel(pixels: np.ndarray) -> Image.Image:
    """根据像素数据画图像"""
    image = Image.fromarray(pixels)
    return image


def show(image: Union[Image.Image, np.ndarray], ax: plt.Axes = None):
    """
    在本地 照片查看器 or matplotlib 查看 image or pixelss
    :param image: Image.Image or pixelss
    :param ax:
    """
    if not isinstance(image, Image.Image):
        image = drawPixel(image)
    if not ax:
        image.show()
    else:
        ax.pcolormesh(image)
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        ax.set_aspect(1)
        ax.grid()


def remove_unused_palette_colors(image: Image.Image):
    """优化image的调色板"""
    if image.mode != 'P':
        image = image.convert('P')
    img_array = np.array(image)
    palette = image.getpalette()  # 获取调色板
    used_palette_indices = np.unique(img_array)
    new_palette = []
    for index in used_palette_indices:
        start = index * 3
        end = start + 3
        new_palette.extend(palette[start:end])
    while len(new_palette) < 768:
        new_palette.extend([0, 0, 0])
    new_img = Image.new('P', image.size)
    new_img.putpalette(new_palette)
    index_mapping = {old_index: new_index for new_index, old_index in enumerate(used_palette_indices)}
    new_data = np.vectorize(index_mapping.get)(img_array).flatten()

    new_img.putdata(new_data)
    return new_img


# 示例用法
if __name__ == "__main__":
    file = "./file/brass_block.png"
    img = Image.open(file)
    getInfo(img)
    pixels = getPixelData(img)
    print(pixels)

    show(pixels)
