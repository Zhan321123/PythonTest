"""
栅格函数
"""
from test1drawBlocks import *


def rasterize(fxs: callable, fys: callable, xRange: tuple[float, float], yRange: tuple[float, float]) -> planarPoints:
    """
    栅格二维函数
    :param fxs: y = f(x) -> y value[]
    :param fys: x = f'(y) -> x value[]
    :param xRange: (x left, x right)
    :param yRange: (y bottom, y top)
    :return:
    """
    points = set()
    for x in range(*map(np.round, xRange)):
        ys = set(fxs(x))
        ys = map(np.round, ys)
        points.update([(x, y) for y in ys])
    for y in range(*map(np.round, yRange)):
        xs = set(fys(y))
        xs = map(np.round, xs)
        points.update([(x, y) for x in xs])
    return points


def _f(f: callable):
    def func(x):
        try:
            return f(x)
        except Exception as e:
            return (np.nan,)

    return func


def oval(a: float, b: float) -> (callable, callable):
    """
    椭圆 :math: (x/a)^2 + (y/b)^2 = 1
    :param a: semiLongAxis
    :param b: semiShortAxis
    :return:
    """

    def fxs(x):
        return np.sqrt(1 - (x / a) ** 2) * b, -np.sqrt(1 - (x / a) ** 2) * b

    def fys(y):
        return np.sqrt(1 - (y / b) ** 2) * a, -np.sqrt(1 - (y / b) ** 2) * a

    return _f(fxs), _f(fys)


def inverseProportion(a: float) -> (callable, callable):
    """
    反比例函数 :math: y = a/x
    :param a:
    :return:
    """

    def fxs(x):
        return a / x,

    def fys(y):
        return a / y,

    return _f(fxs), _f(fys)


def trigonometric(a: float) -> (callable, callable):
    """
    sin函数 :math: y/a = sin(x/a)
    :param a: 放大倍数
    :return:
    """

    def fxs(x):
        return a * np.sin(x / a),

    def fys(y):
        return a * np.arcsin(y / a),

    return _f(fxs), _f(fys)


# def heart()


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 1)

    # ps = rasterize(*oval(40, 30), (-40, 40), (-40, 40))
    # ps = rasterize(*inverseProportion(100), (-60, 60), (-60, 60))
    ps = rasterize(*trigonometric(10), (-90, 90), (-10, 10))
    drawSquare(axs, ps, )

    plt.show()
