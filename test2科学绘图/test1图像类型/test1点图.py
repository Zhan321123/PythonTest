"""
简单点图
三维点图
带尺寸的散点图
极轴带尺寸的散点图
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
    xs, ys = np.array(xs), np.array(ys)
    ax.scatter(xs, ys, marker='+', color='red')
    ax.set_title('simple point chart')


def point3d(ax: plt.Axes, xs: Sequence, ys: Sequence, zs: Sequence):
    """绘制三维散点图"""
    xs, ys, zs = np.array(xs), np.array(ys), np.array(zs)
    fig = ax.figure
    ax.remove()
    # projection='3d' 三维图像, elev=30 仰角, azim=45 方位角
    ax = fig.add_subplot(ax.get_subplotspec(), projection='3d', elev=30, azim=45, )
    ax.scatter(xs, ys, zs)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D point chart')


def sizePoint(ax: plt.Axes, xs: Sequence, ys: Sequence, sizes: Sequence):
    """绘制带尺寸的散点图"""
    xs, ys, sizes = np.array(xs), np.array(ys), np.array(sizes)
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(xs))][0:len(xs)]
    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.5)
    ax.set_title('size point chart')
    ax.grid()


def polarPoint(ax: plt.Axes, thetas: Sequence, rs: Sequence, sizes: Sequence):
    """极坐标带尺寸的散点图"""
    thetas, rs, sizes = np.array(thetas), np.array(rs), np.array(sizes)
    fig = ax.figure
    ax.remove()
    ax = fig.add_subplot(ax.get_subplotspec(), polar=True)
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(thetas))][0:len(thetas)]
    # s标记大小，c标记颜色，alpha透明度
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
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

    simplePoint(axs[0][0], x, y)
    point3d(axs[0][1], x, y, z)
    sizePoint(axs[1][0], x, y, z)
    polarPoint(axs[1][1], x, y, z)

    plt.show()
