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
        plt.plot(x, y, label=f'{f.__doc__}')
    plt.plot([x[0], x[-1]], [0, 0], color='black')
    plt.plot([0, 0], [max(y), min(y)], color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def f1(x):
    y = -math.exp(-(math.pi*x**2)/4)
    return y


# def equationSolving(equation, xl, xr, error=0.0001):
#     while abs(xr - xl) > error:
#         xm = (xl + xr) / 2
#         if equation(xl) * equation(xm) < 0:
#             xr = xm
#         else:
#             xl = xm
#     result = (xl + xr) / 2
#     return result


if __name__ == '__main__':
    functionGraph([f1], (0,3))
