import numpy as np
from PIL import Image

from init import Root
from test1python基础.test1.test35类属性 import printObject

file2 = Root / 'test11图片/typicalImage/old.png'
image3 = Image.open(file2)
print(image3.mode)
printObject(image3)
printObject(image3.palette)
printObject(image3.png)
print(image3.getpalette())
print(len(image3.getpalette()))
print(np.array(image3))
# image3 = image3.convert(
#   'I',
#   dither=Image.Dither.NONE,
#   # palette=Image.Palette.ADAPTIVE,
#   # colors=len(set(image3.getdata()))
# )
# image3.save(Root / 'test11图片/typicalImage/L.png', format='png', optimize=True, compress_level=9)
