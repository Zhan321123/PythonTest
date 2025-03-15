"""
绘制二维函数图像
    显函数方程 y = f(x)
    参数方程 y = f(t), x = g(t)
    隐函数方程 f(x, y) = 0

"""
import math
from typing import Sequence, Union

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def graph(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """
    绘制图像
    """
    xs, ys = np.array(xs), np.array(ys)
    ax.plot(xs, ys)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.grid()


def graph2(ax: plt.Axes, xss: Sequence[Sequence], yss: Sequence[Sequence], zss: Sequence[Sequence]):
    """
    利用contour的levels=0绘制隐函数图像

    :param ax: plt.Axes
    :param xss: xss, yss = np.meshgrid(xs, ys)
    :param yss:
    :param zss: zss = f(xss, yss)
    :return:
    """
    xss, yss, zss = np.array(xss), np.array(yss), np.array(zss)
    ax.contour(xss, yss, zss, levels=0)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    ax.grid()


def explicitFunctionalEquation(x: Union[float, np.ndarray]) -> Union[float, float, np.ndarray]:
    """
    显函数方程，y = f(x)
    """
    return x ** 2/5 - x + 1


def parametricEquation(t: Union[float, np.ndarray]) -> Union[tuple[float, float], tuple[np.ndarray, np.ndarray]]:
    """
    参数方程
    """
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y


def implicitEquation(x: Union[float, np.ndarray], y: Union[float, np.ndarray]) -> Union[float, float, np.ndarray]:
    """
    隐函数方程
    f(x, y) = 0
    :return: z = f(x, y)
    """
    return x ** 2 * y ** 3 - (x ** 2 + y ** 2 - 1) ** 3


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 3)
    axs = axs.flatten()

    ts = np.linspace(0, 2 * math.pi, 1000)
    xs, ys = parametricEquation(ts)
    graph(axs[0], xs, ys)

    xss, yss = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-2, 2, 200))
    zss = implicitEquation(xss, yss)
    graph2(axs[1], xss, yss, zss)

    xs = np.linspace(-10, 10, 200)
    ys = explicitFunctionalEquation(xs)
    graph(axs[2], xs, ys)


    plt.show()
