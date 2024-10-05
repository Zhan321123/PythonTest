"""
点图
"""
import random
from typing import Sequence
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def simplePoint(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制简单的散点图"""
    ax.scatter(xs, ys, marker='+', color='red')
    ax.set_title('simple point chart')


def point3d(ax: plt.Axes, position: (int, int, int), xs: Sequence, ys: Sequence, zs: Sequence):
    """绘制三维散点图"""
    ax.remove()
    # projection='3d' 代表三维图像, elev=30 仰角, azim=45 方位角
    ax = fig.add_subplot(*position, projection='3d', elev=30, azim=45, )
    ax.scatter(xs, ys, zs)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D point chart')


def sizePoint(ax: plt.Axes, xs: Sequence, ys: Sequence, sizes: Sequence):
    """绘制带尺寸的散点图"""
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(xs))][0:len(xs)]
    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.5)
    ax.set_title('size point chart')
    ax.grid()


def polarPoint(ax: plt.Axes, position: (int, int, int), thetas: Sequence, rs: Sequence, sizes: Sequence):
    """极坐标带尺寸的散点图"""
    ax.remove()
    ax = fig.add_subplot(*position, polar=True)
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(thetas))][0:len(thetas)]
    ax.scatter(thetas, rs, s=sizes, c=colors, alpha=0.5)
    ax.set_title('polar size point chart')


if __name__ == '__main__':
    x = list(range(100))
    y = list(range(100))
    z = list(range(100))
    random.shuffle(x)
    random.shuffle(y)
    random.shuffle(z)

    fig, axs = plt.subplots(2, 2)
    simplePoint(axs[0][0], x, y)
    point3d(axs[0][1], (2, 2, 2), x, y, z)  # position:(2,3,4)，表示在2×3网格中的第4个位置
    sizePoint(axs[1][0], x, y, z)
    polarPoint(axs[1][1], (2, 2, 4), x, y, z)

    plt.show()
