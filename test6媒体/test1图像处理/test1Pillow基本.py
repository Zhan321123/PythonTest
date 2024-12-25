import matplotlib
from PIL import Image

matplotlib.use('TkAgg')


def getInfo(file: str):
    """获取图片信息"""
    image = Image.open(file)
    print(image.size)  # 像素尺寸
    print(image.mode)  # 颜色模式
    print(image.format)  # 图片文件格式
    print(image.info)  # 图片信息
    print(image.getextrema())  # 图片各颜色值最大最小值

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

def drawOnPixel(pixels: list[list[tuple]])->Image:
    """根据像素数据画图像"""
    image = Image.new('RGB', (len(pixels[0]), len(pixels)))
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            image.putpixel((x, y), tuple(pixels[y][x]))
    return image