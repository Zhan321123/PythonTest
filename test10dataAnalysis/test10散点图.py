"""
散点图

command:
生成散点图
"""
import random
from copy import copy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# （x,y）点集
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = copy(x)

def change():
    random.shuffle(x)
    random.shuffle(y)
change()

# 创建散点图
plt.scatter(x, y,label='我的点',marker='o',color='red')

change()
plt.scatter(x, y,label='他的点',marker='x',color='green')
change()
plt.scatter(x, y,label='你的点',marker='+',color='blue')

# 设置坐标轴标签
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

# 显示图形
plt.show()
