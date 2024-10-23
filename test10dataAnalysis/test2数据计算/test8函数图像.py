"""
画出图像
"""
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import norm

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def functionGraph(fs: [callable], limit: tuple[float, float], fineness=300):
    """
    画出函数图像
    """
    x = np.linspace(*limit, fineness)
    plt.figure(figsize=(10, 6))
    for f in fs:
        y = [f(i) for i in x]
        plt.plot(x, y, label=f'{f.__doc__}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def f1(x):
    """norm pdf"""
    y = norm.pdf(x)
    return y

def f2(x):
    """norm cdf"""
    y = norm.cdf(x)
    return y

if __name__ == '__main__':
    functionGraph([f1,f2], (-3, 3))
