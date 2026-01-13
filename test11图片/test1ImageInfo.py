import pathlib
from typing import Union, Sequence, Tuple

import matplotlib
import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt

from test1python基础.test1.test35类属性 import printObject, printAttribute

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


def drawPixel(pixels: Union[np.ndarray, list[list[list]]]) -> Image.Image:
  """根据像素数据画图像"""
  try:
    pixels[0][0][0]
  except TypeError:
    raise ValueError("图片像素数据必须是3维数组")
  pixels = np.array(pixels).astype(np.uint8)
  image = Image.fromarray(pixels)
  return image


def show(img: Image.Image, ax: plt.Axes = None):
  """
  在本地 照片查看器 or matplotlib 查看 image

  :param img:
  :param ax:
  """
  if not ax:
    img.show()
  else:
    if img.mode == "L":
      ax.imshow(img, cmap='gray', vmin=0, vmax=255)
    else:
      ax.imshow(img)
    ax.grid(False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_aspect(1)


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


def printImage(image: Image.Image):
  """

  :param image:
  :return:
  """
  for y in range(image.height):
    for x in range(image.width):
      cell = image.getpixel((x, y))
      if image.mode == 'L':
        print(str(cell).center(4, ' '), end='')
      else:
        print(str(sum(cell)).center(4, ' '), end='')
    print()


def invertedColor(image: Image.Image) -> Image.Image:
  """
  反色

  :param image:
  :return:
  """
  return ImageOps.invert(image)


def addBorder(image: Image.Image, border: int = 1, borderColor: str = "#ffffff") -> Image.Image:
  """
  添加边框

  :param image:
  :param border: 边框宽度
  :param borderColor:
  :return:
  """
  if border <= 0:
    return image
  borderColor = borderColor.lstrip('#')
  if len(borderColor) == 3:
    borderColor = ''.join([c * 2 for c in borderColor])
  rgb_color = tuple(int(borderColor[i:i + 2], 16) for i in (0, 2, 4))
  bordered_image = ImageOps.expand(
    image,
    border=border,
    fill=rgb_color
  )

  return bordered_image


def enhanceDpi(img: Image.Image, savePath: str, dpi: Union[int, list[int, int]]):
  """提升图片的dpi"""
  if isinstance(dpi, (Sequence, np.ndarray)):
    img.info["dpi"] = dpi
  else:
    img.info["dpi"] = (dpi, dpi)
  img.save(savePath, quality=95, dpi=img.info["dpi"])


def mirrorLR(img: Image.Image) -> Image.Image:
  """
  水平镜像

  :param img:
  :return:
  """
  return ImageOps.mirror(img)


def mirrorUD(img: Image.Image) -> Image.Image:
  """
  垂直镜像

  :param img:
  :return:
  """
  return ImageOps.flip(img)


def getRgbChanelImages(img: Image.Image) -> Tuple[Image.Image, Image.Image, Image.Image]:
  """
  展示image的RGB颜色通道值
  :param img:
  :return:
  """
  if img.mode not in ("RGB", "RGBA"):
    img = img.convert("RGB")

  r_channel, g_channel, b_channel = img.split()
  black_channel = Image.new('L', img.size, 0)  # 'L'表示8位灰度图，值为0（黑色）
  # 组合通道：保留目标通道，其他通道用黑色填充
  # 每个通道图仍为RGB模式，但仅目标通道有值
  rImage = Image.merge("RGB", (r_channel, black_channel, black_channel))
  gImage = Image.merge("RGB", (black_channel, g_channel, black_channel))
  bImage = Image.merge("RGB", (black_channel, black_channel, b_channel))
  return rImage, gImage, bImage


def save(img: Image.Image, outputDir: Union[str, pathlib.Path], name: str):
  """
  保存image

  :param img:
  :param outputDir:
  :param name:
  :return:
  """
  outputDir = pathlib.Path(outputDir)
  if not outputDir.exists():
    raise Exception("输出目录不存在")
  if not ("." in name and name.split(".")[-1] in
          ["png", "jpg", "jpeg", "gif", "bmp", "tiff", "webp", "jfif", "heif", "avif", "svg",
           "eps", "psd", "ai", "cdr", "svgz", "ico", "cur", "webp", ]):
    name += ".png"
  img.save(outputDir / name)


if __name__ == "__main__":
  file = "./file/brass_block.png"
  img = Image.open(file)