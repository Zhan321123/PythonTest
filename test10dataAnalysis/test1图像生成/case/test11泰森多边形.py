"""
泰森多边形

"""
import random
from copy import copy

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy.spatial import Voronoi, voronoi_plot_2d
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据点
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30]
y = copy(x)
random.shuffle(x)
random.shuffle(y)
data = np.array([x, y]).T

# 计算泰森多边形
vor = Voronoi(data)

# 绘制泰森多边形
fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax)
ax.scatter(data[:, 0], data[:, 1], color='red', s=50, zorder=10)  # 绘制原始点

# 可选：如果要获取并绘制多边形的实际边线，可以进一步处理vor.ridge_points和vor.ridge_vertices
# ...

plt.title('泰森多边形')

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.show()
