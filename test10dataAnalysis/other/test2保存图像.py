"""
将测试集的图像保存

command:
根据x、y、z生成三维散点图
用代码实现将该图片保存到本地（同级目录文件夹）
"""
import random
from copy import copy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94]
y = copy(x)
z = copy(x)
random.shuffle(x)
random.shuffle(y)
random.shuffle(z)

# 创建一个三维图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维散点图
ax.scatter(x, y, z)

# 设置坐标轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 显示图形
plt.show()

fig.savefig('new_figure.png')