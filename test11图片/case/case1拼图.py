import pathlib
from typing import Literal, Sequence

import matplotlib
from PIL import Image
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")


def _addBorder(image: Image.Image, border: int = 1, borderColor: str = "#ffffff") -> Image.Image:
  img = Image.new("RGBA", (image.width + 2 * border, image.height + 2 * border), borderColor)
  img.paste(image, (border, border))
  return img


def _resizeByWidth(image: Image.Image, width: int, method: int = Image.NEAREST):
  newSize = (width, width * image.height // image.width)
  return image.resize(newSize, method)


def show(image: Image.Image):
  plt.imshow(image)
  # plt.axis('off')
  plt.title(f"Image ({image.width}, {image.height})")
  plt.show()


def save(image: Image.Image, outputDir: pathlib.Path, name: str):
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


def matrixAssemble(imagess: Sequence[Sequence[Image.Image]], border: int = 0,
    borderColor: str = "#ffffff", ) -> Image.Image:
  """
  阵列拼合图像

  :param imagess: 二维图像组
  :param border: 边框宽度
  :param borderColor: 边框颜色
  :return:
  """
  # TODO

def packingAssemble(images: Sequence[Image.Image], border: int = 0, borderColor: str = "#ffffff") -> Image.Image:
  """
  装箱式拼合图像
  :param images: 被装箱的图像
  :param border: 边框宽度
  :param borderColor: 边框颜色
  :return:
  """
  # TODO


if __name__ == '__main__':
  rootPath = pathlib.Path(__file__).resolve().parent
  filePath = rootPath / "../file"
  fs = [filePath / "1.jpeg", filePath / "3.jpeg", filePath / "4.jpeg", filePath / "fusionFull.png"]
  imgs = [Image.open(i) for i in fs]
  out = verticalAssemble(imgs, border=1, method="average")
  save(out, filePath, "verticalAssemble.png")
