"""
绘制三维函数图 z = f(x, y)
底部绘制等值线


"""
from typing import Sequence

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

matplotlib.use('TkAgg')


def drawSurface(ax: plt.Axes, xs: Sequence[float], ys: Sequence[float], zss: Sequence[Sequence[float]]):
    """
    绘制三维函数图 z = f(x, y)
    并在底部绘制等值线

    :param ax:
    :param xs: (x,)
    :param ys: (,y)
    :param zss: f(x,y)
    :return:
    """
    xs, ys, zss = np.array(xs), np.array(ys), np.array(zss)
    X, Y = np.meshgrid(np.array(xs), np.array(ys))
    surf = ax.plot_surface(X, Y, zss, cmap='rainbow_r', )
    bar = plt.colorbar(surf, shrink=0.5, aspect=8)
    norm = Normalize(vmin=zss.min(), vmax=zss.max())
    contour = ax.contour(xs, ys, zss, zdir='z', offset=np.min(zss), cmap='rainbow_r', norm=norm, zorder=0)
    ax.clabel(contour, inline=True, fontsize=8)
    ax.xaxis.set_major_locator(plt.MultipleLocator(2))
    ax.yaxis.set_major_locator(plt.MultipleLocator(2))
    ax.zaxis.set_major_locator(plt.MultipleLocator(2))
    ax.set_title('$f(x, y)$')


def fxy(xs: Sequence[float], ys: Sequence[float]) -> Sequence[Sequence[float]]:
    """
    三维函数 :math:`f (x, y)`
    :param xs: (x,)
    :param ys: (,y)
    :return: f(x,y)序列
    """
    xs, ys = np.meshgrid(np.array(xs), np.array(ys))
    zss = -20 * np.exp(-0.2 * np.sqrt(1 / 2 * (xs ** 2 + ys ** 2))) - np.exp(
        1 / 2 * (np.cos(2 * np.pi * xs) + np.cos(2 * np.pi * ys)))
    return zss


if __name__ == '__main__':
    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    z = fxy(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    drawSurface(ax, x, y, z)

    plt.show()
