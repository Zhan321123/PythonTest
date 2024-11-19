"""
图像缩放
"""
import os

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def showResizeImage():
    """展示几种缩放图像的区别"""
    image = Image.open(r'D:\code\pythonProject\PythonTest\test6媒体\file\small.png')
    newSize = (600, 600)

    titles = ('NEAREST', 'BILINEAR', 'BICUBIC', 'LANCZOS')
    nearest = image.resize(newSize, Image.NEAREST)  # 最近邻插值
    bilinear = image.resize(newSize, Image.BILINEAR)  # 双线性插值
    bicubic = image.resize(newSize, Image.BICUBIC)  # 三次样条插值
    lanczos = image.resize(newSize, Image.LANCZOS)  # Lanczos 插值

    fig, axs = plt.subplots(2, 2)
    for ax, img, title in zip(axs.flatten(), [nearest, bilinear, bicubic, lanczos], titles):
        ax.axis('off')
        ax.imshow(img)
        ax.set_title(title)
    plt.show()

def resizeImageBySize(filePath:str, savePath:str,newSize:tuple[int,int], method:int=Image.NEAREST):
    """
    缩放图像
    目前在nearest中存在一些问题，放大之后像素边缘出现摩尔纹
    :param filePath: 文件路径
    :param savePath: 保存路径
    :param newSize: 新的尺寸
    :param method: 缩放方法，默认最近邻插值
    """
    image = Image.open(filePath)
    image.resize(newSize, method).save(savePath)
    print('缩放并保存完成')

def resizeImageByRatio(filePath:str, savePath:str, ratio:float, method:int=Image.NEAREST):
    """
    按比例缩放图片
    :param filePath: 文件路径
    :param savePath: 保存路径
    :param ratio: 比例
    :param method: 缩放方法，默认最近邻插值
    """
    image = Image.open(filePath)
    width, height = image.size
    newSize = (int(width * ratio), int(height * ratio))
    image.resize(newSize, method).save(savePath)
    print('缩放并保存完成')

if __name__ == '__main__':
    # showResizeImage()
    fp = r'D:\code\pythonProject\PythonTest\test6媒体\file\small.png'
    sp = rf"{os.environ['USERPROFILE']}\Desktop\output.jpg"  # 桌面路径
    # resizeImageBySize(fp, sp, (640, 640))
    # resizeImageByRatio(fp, sp, 10)