"""
图像缩放
"""
import os
import pathlib

import matplotlib
from PIL import Image
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def showResizeImage(img: Image.Image):
  """展示几种缩放图像的区别"""
  newSize = (600, 600)

  titles = ('NEAREST', 'BILINEAR', 'BICUBIC', 'LANCZOS')
  nearest = img.resize(newSize, Image.NEAREST)  # 最近邻插值
  bilinear = img.resize(newSize, Image.BILINEAR)  # 双线性插值
  bicubic = img.resize(newSize, Image.BICUBIC)  # 三次样条插值
  lanczos = img.resize(newSize, Image.LANCZOS)  # Lanczos 插值

  fig, axs = plt.subplots(2, 2)
  for ax, img, title in zip(axs.flatten(), [nearest, bilinear, bicubic, lanczos], titles):
    ax.axis('off')
    ax.imshow(img)
    ax.set_title(title)
  plt.show()


def resizeImageBySize(img: Image.Image, newSize: tuple[int, int], method: int = Image.NEAREST) -> Image.Image:
  """
  以新的尺寸缩放图像
  目前在nearest中存在一些问题，放大之后像素边缘出现摩尔纹
  :param img:
  :param newSize: 新的尺寸
  :param method: 缩放方法，默认最近邻插值
  """
  img.resize(newSize, method)
  return img


def resizeImageByRatio(img: Image.Image, ratio: float, method: int = Image.NEAREST) -> Image.Image:
  """
  按比例缩放图片
  :param img:
  :param ratio: 比例
  :param method: 缩放方法，默认最近邻插值
  """
  width, height = img.size
  newSize = (int(width * ratio), int(height * ratio))
  img.resize(newSize, method)
  return img


def _resizeByWidth(image: Image.Image, width: int, method: int = Image.NEAREST):
  if width == image.width:
    return image
  newSize = (width, width * image.height // image.width)
  return image.resize(newSize, method)


def _resizeByHeight(image: Image.Image, height: int, method: int = Image.NEAREST):
  if height == image.height:
    return image
  newSize = (image.width * height // image.height, height)
  return image.resize(newSize, method)

if __name__ == '__main__':
  rootPath = pathlib.Path(__file__).resolve().parent
  filePath = rootPath / "./file"
  fs = filePath / "brass_block.png"
  img = Image.open(fs)
  img = _resizeByHeight(img, 600)
  img.show()