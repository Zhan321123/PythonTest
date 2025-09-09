import os

from PIL import Image

from test11图片.test7拼图 import packingAssemble
from test8文件.test1io import getAllFiles

files = getAllFiles(r"D:\code\pythonProject\PythonTest\test2科学绘图\file")
images = [Image.open(file) for file in files]
img = packingAssemble(images, 16 / 9)
# img.show()
img.save(rf"{os.environ['USERPROFILE']}\Desktop\test.png")