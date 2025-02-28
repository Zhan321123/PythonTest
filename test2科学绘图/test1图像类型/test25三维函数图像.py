"""
绘制三维函数图 z = f(x, y)
底部绘制等值线


"""
from typing import Sequence, Union

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

matplotlib.use('TkAgg')


def drawSurface(ax: plt.Axes, xss: Sequence[Sequence[float]], yss: Sequence[Sequence[float]],
                zss: Sequence[Sequence[float]]):
    """
    绘制三维函数图 z = f(x, y)
    并在底部绘制等值线

    :param ax: plt.Axes
    :param xss: xss, yss = np.meshgrid(xs, ys)
    :param yss:
    :param zss: zss = f(xss, yss)
    :return:
    """
    xss, yss, zss = np.array(xss), np.array(yss), np.array(zss)
    surf = ax.plot_surface(xss, yss, zss, cmap='rainbow_r', )
    bar = plt.colorbar(surf, shrink=0.5, aspect=8)
    norm = Normalize(vmin=zss.min(), vmax=zss.max())
    contour = ax.contour(xss, yss, zss, zdir='z', offset=np.min(zss), cmap='rainbow_r', norm=norm, zorder=0)
    ax.clabel(contour, inline=True, fontsize=8)
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax.zaxis.set_major_locator(plt.MultipleLocator(5))
    ax.set_title('$f(x, y)$')


def fxy(x: Union[float, np.ndarray], y: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
    """
    三维函数 :math:`f (x, y)`
    :param x: x or np's array
    :param y: y, len(y) must be equal to len(x)
    :return: f(x, y), length is equal to len(x)
    """
    # z = -20 * np.exp(-0.2 * np.sqrt(1 / 2 * (x ** 2 + y ** 2))) - np.exp(
    #     1 / 2 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))
    z = x ** 2 * y ** 3 - (x ** 2 + y ** 2 - 1) ** 3
    return z


if __name__ == '__main__':
    xs = np.linspace(-2, 2, 200)
    ys = np.linspace(-2, 2, 200)
    X, Y = np.meshgrid(xs, ys)
    Z = fxy(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    drawSurface(ax, X, Y, Z)

    plt.show()
