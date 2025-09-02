"""
栅格三维函数

条件，x=f(y,z),y=f(x,z),z=f(x,y)都能写出来的显函数
"""
import matplotlib.pyplot as plt
import numpy as np

from test1drawBlocks import *


def rasterize(xf: callable, yf: callable, zf: callable, xRange: tuple[int, int], yRange: tuple[int, int],
              zRange: tuple[int, int]) -> spacePoints:
    """
    栅格二维函数
    :param xf: x = g(y,z) -> z value[]
    :param yf: y = h(x,z) -> y value[]
    :param zf: z = f(x,y) -> z value[]
    :param xRange: (x front, x after)
    :param yRange: (y left, y right)
    :param zRange: (z bottom, z top)
    :return: space points {(x, y, z)}
    """
    points = set()
    yss, zss = np.meshgrid(range(*yRange), range(*zRange))
    for y, z in zip(yss.flatten(), zss.flatten()):
        xs = set(xf(y, z))
        xs = map(np.round, xs)
        points.update([(x, y, z) for x in xs])
    xss, zss = np.meshgrid(range(*xRange), range(*zRange))
    for x, z in zip(xss.flatten(), zss.flatten()):
        ys = set(yf(x, z))
        ys = map(np.round, ys)
        points.update([(x, y, z) for y in ys])
    xss, yss = np.meshgrid(range(*xRange), range(*yRange))
    for x, y in zip(xss.flatten(), yss.flatten()):
        zs = set(zf(x, y))
        zs = map(np.round, zs)
        points.update([(x, y, z) for z in zs])
    return points


def _f(f: callable):
    def func(p1, p2):
        try:
            return f(p1, p2)
        except Exception as e:
            return np.nan,

    return func


def singleLeafHyperboloid(a: float, b: float):
    """
    单叶双曲面 (x^2 + y^2)/a^2 - z^2/b^2 = 1
    :param a:
    :param b:
    :return:
    """
    a2, b2 = a ** 2, b ** 2

    def xf(y, z):
        return np.sqrt((1 + z ** 2 / b2) * a2 - y ** 2), -np.sqrt((1 + z ** 2 / b2) * a2 - y ** 2)

    def yf(x, z):
        return np.sqrt((1 + z ** 2 / b2) * a2 - x ** 2), -np.sqrt((1 + z ** 2 / b2) * a2 - x ** 2)

    def zf(x, y):
        return np.sqrt((x ** 2 + y ** 2) / a2 - 1) * b, -np.sqrt((x ** 2 + y ** 2) / a2 - 1) * b

    return _f(xf), _f(yf), _f(zf),


def ball(r):
    """
    球体 x^2 + y^2 + z^2 = r^2
    :param r: radius
    """

    def xf(y, z):
        return np.sqrt(r ** 2 - y ** 2 - z ** 2), -np.sqrt(r ** 2 - y ** 2 - z ** 2)

    def yf(x, z):
        return np.sqrt(r ** 2 - x ** 2 - z ** 2), -np.sqrt(r ** 2 - x ** 2 - z ** 2)

    def zf(x, y):
        return np.sqrt(r ** 2 - x ** 2 - y ** 2), -np.sqrt(r ** 2 - x ** 2 - y ** 2)

    return _f(xf), _f(yf), _f(zf),


def tours(R=30, r=10):
    """
    圆环体 (sqrt(x^2 + y^2) - R)^2 + y^2 = r^2
    R>r
    :param R:
    :param r:
    :return:
    """

    def xf(y, z):
        return (
            np.sqrt((np.sqrt(r ** 2 - z ** 2) + R) ** 2 - y ** 2),
            np.sqrt((-np.sqrt(r ** 2 - z ** 2) + R) ** 2 - y ** 2),
            -np.sqrt((np.sqrt(r ** 2 - z ** 2) + R) ** 2 - y ** 2),
            -np.sqrt((-np.sqrt(r ** 2 - z ** 2) + R) ** 2 - y ** 2)
        )

    def yf(x, z):
        return (
            np.sqrt((np.sqrt(r ** 2 - z ** 2) + R) ** 2 - x ** 2),
            np.sqrt((-np.sqrt(r ** 2 - z ** 2) + R) ** 2 - x ** 2),
            -np.sqrt((np.sqrt(r ** 2 - z ** 2) + R) ** 2 - x ** 2),
            -np.sqrt((-np.sqrt(r ** 2 - z ** 2) + R) ** 2 - x ** 2)
        )

    def zf(x, y):
        return (
            np.sqrt(-(np.sqrt(x ** 2 + y ** 2) - R) ** 2 + r ** 2),
            -np.sqrt(-(np.sqrt(x ** 2 + y ** 2) - R) ** 2 + r ** 2)
        )

    return _f(xf), _f(yf), _f(zf),


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ps = rasterize(*tours(15, 5), (-30, 30), (-30, 30), (-30, 30))
    # ps = rasterize(*singleLeafHyperboloid(10, 20), (-20, 20), (-20, 20), (-20, 20))
    drawBlock(ax, ps)
    plt.show()
