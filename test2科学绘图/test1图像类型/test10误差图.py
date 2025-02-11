"""
误差图：

直线误差图
箭头误差图
方块误差图
"""
from typing import Sequence
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def error(ax: plt.Axes, xs: Sequence, ys: Sequence, xerrs: Sequence, yerrs: Sequence):
    """误差图，误差线为直线"""
    ax.errorbar(xs, ys, xerr=xerrs, yerr=yerrs, marker='o')
    ax.grid()
    ax.set_title('error chart')


def errorArrow(ax: plt.Axes, xs: Sequence, ys: Sequence, xerrs: Sequence, yerrs: Sequence):
    """误差图，误差线为箭头"""
    # uplims=True、lolims=True、xuplims=True、xlolims=True，上面、下面、x轴正方向、x轴负方向的误差线去掉，并且另一端设置为箭头
    ax.errorbar(xs, ys, xerr=xerrs, yerr=yerrs, lolims=True, xlolims=True,
                marker='o', linewidth=1, linestyle='dotted')
    ax.grid()
    ax.set_title('error arrow chart')


def errorBox(ax: plt.Axes, xs: Sequence, ys: Sequence, xerrs: Sequence, yerrs: Sequence):
    """误差图，误差线为方块"""
    xs, ys, xerrs, yerrs = np.asarray(xs), np.asarray(ys), np.asarray(xerrs), np.asarray(yerrs)
    errorboxes = [Rectangle((x - xe, y - ye), 2 * xe, 2 * ye)
                  for x, y, xe, ye in zip(xs, ys, xerrs.T, yerrs.T)]
    pc = PatchCollection(errorboxes, facecolors='green', alpha=0.6, edgecolor='black')
    ax.add_collection(pc)
    # fmt = 'none'，将线清除
    ax.errorbar(xs, ys, xerr=xerrs, yerr=yerrs, fmt='none', ecolor='blue')
    ax.grid()
    ax.set_title('error box chart')


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y1 = [3, 5, 4, 8, 10, 12, 11, 14]
    xr = np.random.rand(1, len(x)) * 2
    yr = np.random.rand(1, len(x)) * 3

    fig, axs = plt.subplots(2, 3)
    error(axs[0][0], x, y1, xr, yr)
    errorArrow(axs[0][1], x, y1, xr, yr)
    errorBox(axs[0][2], x, y1, xr, yr)

    plt.show()
