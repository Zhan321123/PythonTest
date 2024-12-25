"""
计算字体
"""

from PIL import ImageFont, ImageDraw, Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


image = Image.new('RGB', (1,1), (255, 255, 255))
draw = ImageDraw.Draw(image)
# 创建一个字体对象
font = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 10)
string = "你好, good man.\n你好, good man."
left, top, right, bottom = draw.textbbox((0, 0), string, font=font)
width = right - left
height = bottom - top
print(width, height)
draw.text((0, 0), string, font=font, fill=(0, 0, 0))
draw.rectangle((left, top, right, bottom), outline='red')
fig,ax = plt.subplots()
ax.imshow(image)
# plt.show()