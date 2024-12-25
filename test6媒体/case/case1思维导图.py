"""

"""
from PIL import Image, ImageDraw, ImageFont

defaultFont = ('C:/Windows/Fonts/simhei.ttf', 20)

image = Image.new('RGB', (1, 1))
draw = ImageDraw.Draw(image)


class Node:
    def __init__(self, content: str, parent: "Node" = None, font: (str, int) = defaultFont, padding=5):
        self.content = content
        self.parent = parent
        self.font = font
        self.padding = padding

    def getFontSize(self)->tuple[int, int]:
        font = ImageFont.truetype(*self.font)
        _, _, width, height = draw.textbbox((0, 0), self.content, font=font)
        return width, height

    def getBoxSize(self)->tuple[int, int]:
        return self.getFontSize()[0] + 2 * self.padding, self.getFontSize()[1] + 2 * self.padding


root = Node('root')
root.getFontSize()
