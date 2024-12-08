import math


def equationSolving(func, xl, xr):
    """解方程"""
    while abs(xr - xl) > 1e-5:
        xm = (xl + xr) / 2
        if func(xl) * func(xm) < 0:
            xr = xm
        else:
            xl = xm
    return (xl + xr) / 2


def dispersion(T, h):
    """
    弥散方程 L = L0 * tanh(2 * pi * h / L)
    :param T: 波周期,(s)
    :param h: 水深,(m)
    :return: h处的波长L,(m)
    """
    L0 = 9.8 * T ** 2 / 2 / math.pi  # 深水区波长L0,(m)
    f = lambda L: L0 * math.tanh(2 * math.pi * h / L) - L  # 弥散方程
    l = equationSolving(f, 1e-5, 1e5)
    print("波长L:", round(l, 3), "波速C:", round(l / T, 3))
    return l


dispersion(5, 10)
dispersion(5, 5)
dispersion(5, 2)
