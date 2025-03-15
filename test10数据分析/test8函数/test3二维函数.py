import numpy as np
from test1drawTwoDimension import *


def valley(x):
    """山谷"""
    return 1 / (x ** 2 + 1)


def circle(x, y, r=1):
    """
    圆
    :param r: 半径
    """
    return x ** 2 + y ** 2 - r ** 2


def oval(x, y, l=2, s=1):
    """
    椭圆
    :param l: 长半轴
    :param s: 短半轴
    """
    return x ** 2 / l ** 2 + y ** 2 / s ** 2 - 1


def love(x, y, s=2):
    """
    爱心
    :param s: 放大倍数
    """
    x, y = x / s, y / s
    return (x ** 2 + y ** 2 - 1) ** 3 - x ** 2 * y ** 3


def arch(x, a=2):
    """
    拱形
    :param a:
    """
    return a * np.cosh(x / a)


# def drop(x, n=1):
#     """
#     水滴
#     """

def drop(x, y, n=3):
    return (x ** 2 + y ** 2) ** 2 - 2 * y * (x ** 2 + y ** 2) + n * x ** 2


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 3)

    xs = np.linspace(-3, 3, 100)
    ys = np.linspace(-3, 3, 100)
    # y1 = valley(xs)
    y1 = arch(xs)
    graph(axs[0], xs, y1)

    xss, yss = np.meshgrid(xs, ys)
    # zss = circle(xss, yss)
    # zss = oval(xss, yss)
    # zss = love(xss, yss)
    zss = drop(xss, yss)
    graph2(axs[1], xss, yss, zss)
    plt.show()
