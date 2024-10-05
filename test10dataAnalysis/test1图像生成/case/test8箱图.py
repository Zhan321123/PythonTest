"""
箱图
"""
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def boxChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """箱图"""
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(xs))][0:len(xs)]
    bplot = ax.boxplot(yss,
                       patch_artist=True,  # fill with color
                       tick_labels=xs)
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    ax.set_title('Rectangular box plot')


def boxChart2(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """箱图"""
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(xs))][0:len(xs)]
    bplot = ax.boxplot(yss, notch=True,  # notch shape
                       vert=True,  # vertical box alignment
                       patch_artist=True,
                       tick_labels=xs)
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    ax.set_title('Notched box plot')


if __name__ == '__main__':
    x = ['x1', 'x2', 'x3']
    yss = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
           [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12, 28],
           [0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 24, 25, 29]]

    fig, axs = plt.subplots(2, 2)
    boxChart(axs[0][0], x, yss)
    boxChart2(axs[0][1], x, yss)

    plt.show()
