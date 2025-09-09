import os
import pathlib
from typing import Literal, Sequence

import matplotlib
import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt

from test9算法.test1数据计算.case1矩形装箱优化问题 import EncloseFixedRatio, MaxRectsBssf, showRectInBox

matplotlib.use("TkAgg")


def _placeOnCenter(img: Image.Image, paper: [int, int]) -> Image.Image:
  paper_width, paper_height = paper

  img_width, img_height = img.size
  x = (paper_width - img_width) // 2
  y = (paper_height - img_height) // 2
  paper_img = Image.new('RGBA', (paper_width, paper_height), (0, 0, 0, 0))
  if img.mode != 'RGBA':
    img = img.convert('RGBA')
  paper_img.paste(img, (x, y), img)
  return paper_img


def _addBorder(image: Image.Image, border: int = 1, borderColor: str = "#ffffff") -> Image.Image:
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


def _show(image: Image.Image):
  plt.imshow(image)
  # plt.axis('off')
  plt.title(f"Image ({image.width}, {image.height})")
  plt.show()


def _save(image: Image.Image, outputDir: pathlib.Path, name: str):
  if outputDir.exists():
    image.save(outputDir / name)
  else:
    raise Exception("输出目录不存在")


def verticalAssemble(images: Sequence[Image.Image], border: int = 0, borderColor: str = "#ffffff",
    method: Literal["standard", "average", "max", "min", "specific", "lazy"] = 'standard',
    width: int = None) -> Image.Image:
  """
  竖直拼合图像

  :param images: 被拼合的图像
  :param border: 边框宽度
  :param borderColor: 边框颜色
  :param method: 拼合方法
    standard模式，拼接为长图，要求图像宽度宽度一致
    average模式，拼接为长图，按照图像平均宽度
    max模式，拼接为长图，按照最大宽度，缩放图像
    specific模式，拼接为长图，按照指定宽度，缩放图像
    lazy模式，拼接为长图，按照图像最大宽度宽度，不缩放图像
  :param width: specific模式的图像宽度
  :return:
  """
  if len(images) == 1:
    print("仅有一张图片")
    return images[0]

  ws = [image.width for image in images]

  # 模式调整
  if method == "standard":
    if len(set(ws)) != 1:
      raise Exception("图片宽度不一致")
  elif method == "average":
    width = sum(ws) // len(ws)
    images = [_resizeByWidth(image, width) for image in images]
  elif method == "max":
    width = max(ws)
    images = [_resizeByWidth(image, width) for image in images]
  elif method == "min":
    width = min(ws)
    images = [_resizeByWidth(image, width) for image in images]
  elif method == "specific":
    if width is None:
      raise Exception("specific模式请指定参数width")
    images = [_resizeByWidth(image, width) for image in images]
  elif method == "lazy":
    width = max(ws)
  else:
    raise ValueError("拼合方法错误")

  # 边框
  if border != 0:
    images = [_addBorder(image, border, borderColor) for image in images]

  # 拼图
  hs = [image.height for image in images]
  img = Image.new('RGB', (width + 2 * border, sum(hs)))
  for i, image in enumerate(images):
    img.paste(image, (0, sum(hs[:i])))

  return img


def matrixAssemble(imgss: Sequence[Sequence[Image.Image]], border: int = 0, borderColor: str = "#ffffff",
    mode: Literal[
      "standard", "averageWidth", "averageHeight", "max", "min", "specificWight", "lazy"] = 'standard',
    specificWidth: int = 128) -> Image.Image:
  """
  阵列拼合图像

  :param imgss: 二维图像组
  :param border: 边框宽度
  :param borderColor: 边框颜色
  :param mode: 模式
    standard: 标准模式，长宽不一致直接报错
    averageWidth: 平均宽度模式，高度按照缩放后的最大值
    averageHeight: 平均高度模式，宽度按照缩放后最大的值
    max: 最大模式，不会缩小只会放大图像
    min: 最小模式，不会放大只缩小图像
    specificWight: 指定模式，按照指定宽度缩放图像
    lazy: 不会缩放图像，但按照最大图像阵列
  :param specificWidth:
  :return:
  """
  if len(imgss) == 1 and len(imgss[0]) == 1:
    print("仅有一张图片")
    return imgss[0][0]

  getWss = lambda imagess: np.array([[image.width for image in images] for images in imagess])
  getHss = lambda imagess: np.array([[image.height for image in images] for images in imagess])

  wss = getWss(imgss)
  hss = getHss(imgss)
  ws = wss.flatten()
  hs = hss.flatten()
  heights = None
  widths = None

  if mode == "standard":
    if len(set(ws)) != 1 or len(set(hs)):
      raise Exception("图片长宽不一致")
  elif mode == "averageWidth":
    width = ws.sum() // len(ws)
    imgss = [[_resizeByWidth(image, width) for image in images] for images in imgss]
    hss = getHss(imgss)
    heights = np.max(hss, axis=1)
    imgss = [[_placeOnCenter(image, (width, heights[i])) for image in images] for i, images in enumerate(imgss)]
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    heights += border * 2
    widths = np.zeros(len(imgss[0]), dtype=int) + (width + border * 2)
  elif mode == "averageHeight":
    height = hs.sum() // len(hs)
    imgss = [[_resizeByHeight(image, height) for image in images] for images in imgss]
    wss = getWss(imgss)
    widths = np.max(wss, axis=0)
    imgss = [[_placeOnCenter(image, (widths[j], height)) for j, image in enumerate(images)] for images in imgss]
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    widths += border * 2
    heights = np.zeros(len(imgss), dtype=int) + (height + border * 2)
  elif mode == "max":
    wmaxs = wss.max(axis=0)
    hmaxs = hss.max(axis=1)
    for i, images in enumerate(imgss):
      for j, image in enumerate(images):
        pageW, pageH = wmaxs[j], hmaxs[i]
        if image.width / image.height > pageW / pageH:
          image = _resizeByWidth(image, pageW)
        else:
          image = _resizeByHeight(image, pageH)
        imgss[i][j] = _placeOnCenter(image, (pageW, pageH))
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    heights = hmaxs + border * 2
    widths = wmaxs + border * 2
  elif mode == "min":
    wmins = wss.min(axis=0)
    hmins = hss.min(axis=1)
    for i, images in enumerate(imgss):
      for j, image in enumerate(images):
        pageW, pageH = wmins[j], hmins[i]
        if image.width / image.height > pageW / pageH:
          image = _resizeByWidth(image, pageW)
        else:
          image = _resizeByHeight(image, pageH)
        imgss[i][j] = _placeOnCenter(image, (pageW, pageH))
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    heights = hmins + border * 2
    widths = wmins + border * 2
  elif mode == "specificWight":
    imgss = [[_resizeByWidth(image, specificWidth) for image in images] for images in imgss]
    hss = getHss(imgss)
    heights = hss.max(axis=1)
    imgss = [[_placeOnCenter(image, (specificWidth, heights[i])) for image in images] for i, images in enumerate(imgss)]
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    widths = np.zeros(len(imgss[0]), dtype=int) + (specificWidth + border * 2)
    heights += border * 2
    pass
  elif mode == "lazy":
    wmaxs = wss.max(axis=0)
    hmaxs = hss.max(axis=1)
    for i, images in enumerate(imgss):
      for j, image in enumerate(images):
        pageW, pageH = wmaxs[j], hmaxs[i]
        imgss[i][j] = _placeOnCenter(image, (pageW, pageH))
    imgss = [[_addBorder(image, border, borderColor) for image in images] for images in imgss]
    heights = hmaxs + border * 2
    widths = wmaxs + border * 2
  else:
    raise ValueError("拼合方法错误")

  resultImg = Image.new("RGBA", (widths.sum(), heights.sum()), (0, 0, 0, 0))
  for i, images in enumerate(imgss):
    for j, image in enumerate(images):
      resultImg.paste(image, (np.sum(widths[:j]), np.sum(heights[:i])))
  return resultImg


def packingAssemble(imgs: Sequence[Image.Image], ratio: float, rotation: bool = False, border: int = 0,
    borderColor: str = "#ffffff") -> Image.Image:
  """
  装箱式拼合图像，装入盒子所需最小的盒子

  :param imgs: 被装箱的图像
  :param ratio: 盒子长宽比 width / height
  :param rotation: 是否允许图片旋转
  :param borderColor:
  :param border:
  :return:
  """
  encloser = EncloseFixedRatio(rotation=rotation)
  imgs = [_addBorder(img, border, borderColor) for img in imgs]
  for img in imgs:
    encloser.add_rect(img.width, img.height)
  result = encloser.find_min_container(ratio)
  if result:
    width, height, positions = result
    resultImg = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    for i, (x, y, w, h) in enumerate(positions):
      resultImg.paste(imgs[i], (x, y))
    return resultImg
  else:
    raise Exception("无法找到最小盒子")


if __name__ == '__main__':
  rootPath = pathlib.Path(__file__).resolve().parent
  filePath = rootPath / "./file"
  fs = [filePath / "brass_block.png", filePath / "dirty.png", filePath / "egg.png",
        filePath / "fusionFull.png", filePath / "copper_lantern.png", filePath / "item.png",
        filePath / "redraw_egg.png", filePath / "small.png", filePath / "bubbled.png"]
  images = np.array(list(Image.open(i) for i in fs), dtype=object)
  # out = verticalAssemble(images, border=1, method="min")
  # imagess = images.reshape(3, 3)
  # out = matrixAssemble(imagess, mode="specificWight", border=1, borderColor="#ff00ff")
  out = packingAssemble(images, 16 / 9,border=1, borderColor="#ff00ff")
  _show(out)
  # _save(out, filePath, os.environ['USERPROFILE']+"/Desktop/matrixAssemble.png")
