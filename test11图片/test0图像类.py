import copy
import os
from typing import Union

import numpy as np
from PIL import Image


class ImageProcess:
    class Cell:
        def __init__(self, x: int, y: int, color: tuple, width: int, height: int):
            self.x = x
            self.y = y
            if type(color) == int:
                self.color = [color, color, color, 0]
            elif len(color)==3:
                self.color+=[255]
            else:
                self.color = color
            self.height = height
            self.width = width

        def __repr__(self):
            return f"Cell({self.x},{self.y},{self.color})"

        def above(self, n: int = 1) -> Union[tuple, None]:
            if self.y - n < 0 or self.y - n >= self.height:
                return None
            return self.x, self.y - n

        def below(self, n: int = 1) -> Union[tuple, None]:
            return self.above(-n)

        def left(self, n: int = 1) -> Union[tuple, None]:
            if self.x - n < 0 or self.x - n >= self.width:
                return None
            return self.x - n, self.y

        def right(self, n: int = 1) -> Union[tuple, None]:
            return self.left(-n)

    def _createCellss(self, image: Image.Image) -> [[]]:
        width, height = image.size
        pix = image.load()
        return list(
            list(self.Cell(x, y, pix[x, y,], width, height) for x in range(width))
            for y in range(height)
        )

    def __init__(self, image: Image.Image):
        self.image = image
        self.width, self.height = self.image.size
        self.cellss = self._createCellss(self.image)

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cellss[y][x]
                print(str(sum(cell.color)).center(4, ' '), end='')
            print()
        return self

    def show(self, grid: bool = False):
        # self.image.show() # 使用照片查看器
        import matplotlib
        from matplotlib import pyplot as plt
        matplotlib.use('TkAgg')
        plt.pcolormesh(self.image)
        plt.axis((0, self.width, self.height, 0))
        plt.gca().set_aspect(1)
        plt.grid(grid)
        plt.show()
        return self

    def getCell(self, pos: tuple):
        return self.cellss[pos[1]][pos[0]]

    def create(self) -> Image.Image:
        """根据像素数据画图像"""
        image = Image.new('RGBA', self.image.size)
        for y in range(self.height):
            for x in range(self.width):
                print(self.cellss[y][x])
                image.putpixel((x, y), tuple(self.cellss[y][x].color))
        return image

    def __copy__(self):
        return ImageProcess(self.create())

    def _isTransparent(self, color: tuple) -> bool:
        if sum(color[:3]) == 0 or color[3] == 0:
            return True
        else:
            return False

    def stroke(self, color: tuple) -> 'ImageProcess':
        """
        描边

        :param color: 描边颜色
        :return: 新的图像，不改变原图像
        """
        img2 = copy.copy(self)
        for cell in np.array(self.cellss).flatten():
            if not self._isTransparent(cell.color):
                replace = [cell.above(), cell.below(), cell.left(), cell.right()]
                for pos in replace:
                    if pos is not None:
                        if self._isTransparent(self.getCell(pos).color):
                            img2.getCell(pos).color = color
        return img2

    def invertedColor(self) -> 'ImageProcess':
        """
        反色

        :return 改变的自身
        """
        for cell in np.array(self.cellss).flatten():
            cell.color = list(255 - i for i in cell.color[0:3])+[cell.color[3]]
        self.image = self.create()
        return self


if __name__ == '__main__':
    item = '../file/item.png'
    dirty = '../file/dirty.png'
    img = ImageProcess(Image.open(dirty))
    # img.invertedColor().show(True).print()
    # img.create().save(rf"{os.environ['USERPROFILE']}\Desktop\i.png")
    # img2 = img.stroke((123, 133, 89, 122))
    # img2.print().show(grid=True).create().save(rf"{os.environ['USERPROFILE']}\Desktop\i.png")
