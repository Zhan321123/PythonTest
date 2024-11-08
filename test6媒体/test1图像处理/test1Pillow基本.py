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