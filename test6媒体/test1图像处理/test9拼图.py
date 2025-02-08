"""
拼图

将多张长宽一致的图像拼接为一张长图
"""
from enum import Enum

import matplotlib
from PIL import Image
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')


class StitchMethod(Enum):
    standard = 'standard'
    average = 'average'
    max = 'max'
    specific = 'specific'
    lazy = 'lazy'


class StitchImages:
    showMode = False

    def __init__(self, files: list[str]):
        self.files = files
        self.images = [Image.open(file) for file in self.files]
        self.whs = self._getWHs(self.images)
        if self._checkWidth():
            print('图片宽度一致')
        if self._checkSize():
            print('图片长度一致')

    def _getWHs(self, images: list[Image.Image]):
        """获取图片宽高"""
        sizes = [image.size for image in images]
        return list(zip(*sizes))

    def openShow(self, mode: bool):
        self.showMode = mode

    def _checkSize(self) -> bool:
        """检查图片尺寸是否一致"""
        if self._checkWidth() and len(set(self.whs[1])) == 1:
            return True
        return False

    def _checkWidth(self) -> bool:
        """检查图片宽度是否一致"""
        if len(set(self.whs[0])) == 1:
            return True
        return False

    def getSizes(self):
        return [image.size for image in self.images]

    def stitch(self, outputDir: str, method: StitchMethod = 'standard', width: int = None):
        """
        standard模式，拼接为长图，要求图像宽度宽度一致
        average模式，拼接为长图，按照图像平均宽度
        max模式，拼接为长图，按照最大宽度，缩放图像
        specific模式，拼接为长图，按照指定宽度，缩放图像
        lazy模式，拼接为长图，按照图像最大宽度宽度，不缩放图像
        """
        if method == StitchMethod.standard:
            if not self._checkWidth():
                print('图片宽度不一致')
                return
            width = self.whs[0][0]
            images = self.images
        elif method == StitchMethod.average:
            width = int(sum(self.whs[0]) / len(self.whs[0]))
            images = [self.resize(image, width) for image in self.images]
        elif method == StitchMethod.max:
            width = max(self.whs[0])
            images = [self.resize(image, width) for image in self.images]
        elif method == StitchMethod.specific:
            width = width
            images = [self.resize(image, width) for image in self.images]
        elif method == StitchMethod.lazy:
            width = max(self.whs[0])
            images = self.images
        else:
            raise ValueError('method参数错误')
        img = self.stitchImages(images, width)
        self._display(img, outputDir)

    def stitchImages(self, images: list[Image.Image], width: int) -> Image.Image:
        img = Image.new('RGB', (width, sum(self._getWHs(images)[1])))
        whs = self._getWHs(images)
        for i, image in enumerate(images):
            img.paste(image, (0, sum(whs[1][:i])))
        return img

    def resize(self, image: Image.Image, width: int):
        """将图片缩放至指定宽度"""
        if image.size[0] == width:
            return image
        height = int(image.size[1] * width / image.size[0])
        return image.resize((width, height))

    def _show(self, image: Image.Image):
        plt.imshow(image)
        # plt.axis('off')
        plt.show()

    def _save(self, image: Image.Image, outputDir: str):
        image.save(outputDir)

    def _display(self, image: Image.Image, outputDir: str):
        if self.showMode:
            self._show(image)
        else:
            self._save(image, outputDir)


if __name__ == '__main__':
    f1 = '../file/1.jpeg'
    f2 = '../file/3.jpeg'
    f3 = '../file/4.jpeg'
    f4 = '../file/skin.png'
    f5 = '../file/small.png'
    out = '../file/splicing.jpeg'
    si = StitchImages([f1, f2, f3, f4, f5])
    si.openShow(True)
    si.stitch(out, StitchMethod.standard)
    si.stitch(out, StitchMethod.average)
    si.stitch(out, StitchMethod.max)
    si.stitch(out, StitchMethod.specific, 100)
    si.stitch(out, StitchMethod.lazy)
