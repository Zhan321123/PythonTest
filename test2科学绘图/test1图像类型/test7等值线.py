"""
等值线
"""
from typing import Sequence

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def contour(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
    """
    等值线图
    :param ax: plt.Axes
    :param xs: x轴值
    :param ys: y轴值
    :param zss: (x, y)点的值
    :return:
    """
    xs,ys,zss = np.array(xs), np.array(ys), np.array(zss)
    c = ax.contour(xs, ys, zss, MaxNLocator().tick_values(zss.min(), zss.max()))
    im = ax.imshow(zss,
                   origin='lower',
                   interpolation='bilinear',
                   cmap=matplotlib.colormaps['terrain'],)
    c.clabel(fmt='%1.1f') # 显示等值线的值

    fig.colorbar(im, orientation='horizontal',)
    ax.set_aspect(1)
    ax.axis('off')
    ax.set_title("contour chart")

if __name__ == '__main__':
    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    x, y = np.meshgrid(np.array(x), np.array(y))
    zss = -20 * np.exp(-0.2 * np.sqrt(1 / 2 * (x ** 2 + y ** 2))) - np.exp(
        1 / 2 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))


    fig, axs = plt.subplots(1,2)
    axs = axs.flatten()
    contour(axs[0], x, y, zss)

    plt.show()

