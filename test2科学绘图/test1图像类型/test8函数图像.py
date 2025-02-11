"""
画出图像
"""
import math

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def functionGraph(fs: [callable], limit: tuple[float, float], fineness=300):
    """
    画出函数图像
    """
    x = np.linspace(*limit, fineness).tolist()
    plt.figure(figsize=(10, 6))
    y = None
    for f in fs:
        y = [f(i) for i in x]
        plt.plot(x, y, label=f'${f.__doc__}$')
    xlim = (x[0] if x[0] < 0 else 0, x[-1] if x[-1] > 0 else 0)
    plt.plot(xlim, [0, 0], color='black')
    ylim = (max(y) if max(y) > 0 else 0, min(y) if min(y) < 0 else 0)
    plt.plot([0, 0], ylim, color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def f1(h):
    """n = 0.5+kh/sinh2kh"""
    dispersion = lambda l, h: l - 30 * math.tanh(2 * math.pi / l * h)
    f = lambda l: dispersion(l, h)
    l = equationSolving(f, 1e-5, 1e5)
    n = 0.5 + 2 * math.pi * h / math.sinh(2 * math.pi * h / l)
    return n

def f2(h):
    """l-30tanh(kh)=0"""
    dispersion = lambda l, h: l - 30 * math.tanh(2 * math.pi / l * h)
    f = lambda l: dispersion(l, h)
    return equationSolving(f, 1e-5, 1e5)


def equationSolving(equation: callable, xl: float, xr: float, error=0.0001):
    while abs(xr - xl) > error:
        xm = (xl + xr) / 2
        if equation(xl) * equation(xm) < 0:
            xr = xm
        else:
            xl = xm
    result = (xl + xr) / 2
    return result


if __name__ == '__main__':
    functionGraph([f1,f2], (0.001, 30))
