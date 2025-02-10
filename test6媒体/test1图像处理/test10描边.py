import matplotlib
from PIL import Image


def getPixelData(file: str)->list[list[tuple]]:
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

ss = getPixelData("../file/skin.png")
for rgbs in ss:
    for rgb in rgbs:
        if rgb[3]==0:
            rgb = (255,255,255,255)


