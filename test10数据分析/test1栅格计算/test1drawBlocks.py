"""
使用matplotlib库绘制
    方格
    方块
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

matplotlib.use('TkAgg')

planarPoints = set[tuple[int, int]]
spacePoints = set[tuple[int, int, int]]


def drawSquare(ax: plt.Axes, points: planarPoints, patches:tuple[Patch] = None):
    """
    绘制二维方形，锚点为方形左下角

    :param ax: plt.Axes
    :param points: 平面整数点集
    :param patches: 其他图形
    """
    for x, y in points:
        ax.add_patch(plt.Rectangle((x, y), 1, 1, edgecolor='red'))
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)
    if patches:
        for patch in patches:
            ax.add_patch(patch)
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax.xaxis.set_tick_params(rotation=90)
    ax.grid(True)


def drawBlock(ax: plt.Axes, points: spacePoints):
    """
    绘制三维方块

    :param ax: plt.Axes
    :param points: 空间整数点集
    """
    fig = ax.figure
    ax.remove()
    ax = fig.add_subplot(ax.get_subplotspec(), projection='3d', elev=30, azim=45, )
    X, Y, Z = np.array(list(points)).T
    ax.bar3d(X, Y, Z, dx=1, dy=1, dz=1, shade=True, color='cyan')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 设置xyz刻度间距为1
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax.zaxis.set_major_locator(plt.MultipleLocator(5))
