"""
使用matplotlib库绘制
    方格
    方块
"""
import copy
from typing import Union

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

matplotlib.use('TkAgg')

planarPoints = set[tuple[int, int]]
spacePoints = set[tuple[int, int, int]]

irrationality = [None, np.nan, np.inf]


def _removeIrrationality(points: Union[planarPoints, spacePoints]):
    """
    去除浮点数中的非数字

    :param points: 平面整数点集
    """
    for p in copy.copy(points):
        for i in p:
            if i in irrationality or np.isnan(i):
                points.remove(p)
                break


def drawSquare(ax: plt.Axes, points: planarPoints, patches: tuple[Patch] = None):
    """
    绘制二维方形，锚点为方形左下角

    :param ax: plt.Axes
    :param points: 平面整数点集
    :param patches: 其他图形
    """
    _removeIrrationality(points)
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
    _removeIrrationality(points)
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

if __name__ == '__main__':
    ps = {(0,0,np.nan),(2,3,2),(1,np.float64(np.nan))}
    _removeIrrationality(ps)
    print(ps)