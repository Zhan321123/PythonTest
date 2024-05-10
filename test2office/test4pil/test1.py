"""
第三方包PIL
具有处理图像等功能
"""
from PIL import Image

# 加载图片
im = Image.open('../file/google.jpg')
print(type(im))
print(im)
# 提取rgb颜色通道，返回图像副本
rgb = [r, g, b] = im.split()
for i in rgb:
    print(i)

# 构建新图像
om = Image.merge(mode='RGB',bands=(b,r,g))
# 保存图片
om.save('file/google2.jpg')
