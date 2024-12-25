"""
基于向量加权平均法的图像融合
"""
import matplotlib
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
image1 = '../file/1.jpeg'
image2 = '../file/3.jpeg'
image3 = '../file/4.jpeg'

def getPixelData(file: str):
    """获取图片像素数据"""
    image = Image.open(file)
    pixels = image.load()
    width, height = image.size
    rgbss = []
    for y in range(height):
        rgbs = []
        for x in range(width):
            rgbs.append(pixels[x, y])
        rgbss.append(rgbs)
    return rgbss

def drawOnPixelData(pixels: list[list]):
    """根据像素数据画图像"""
    image = Image.new('RGB', (len(pixels[0]), len(pixels)))
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            image.putpixel((x, y), tuple(pixels[y][x]))
    return image

ps1 = np.array(getPixelData(image1))
ps2 = np.array(getPixelData(image2))
ps3 = np.array(getPixelData(image3))

ps = ps1*0.333+ps2*0.333+ps3*0.334

ps = np.uint(np.round(ps))
image = drawOnPixelData(ps)
img1 = Image.open(image1)
img2 = Image.open(image2)
img3 = Image.open(image3)

fig,axs = plt.subplots(2,2)
axs = axs.flatten()
axs[0].imshow(img1)
axs[1].imshow(img2)
axs[2].imshow(img3)
axs[3].imshow(image)
plt.show()