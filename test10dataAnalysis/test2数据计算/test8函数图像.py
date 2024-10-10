"""
画出图像
"""
import math

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import gamma, skew

from lib import zCalculate as ll

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def functionGraph(f, limit: tuple[float, float], fineness=300):
    """
    画出函数图像

    :param f: 函数def
    :param limit: 上下限
    :param fineness: 点数，点越多曲线更平滑
    """
    x = ll.LineUtil.equidistantListByNum(limit[0], limit[1], fineness)
    print(x)
    y = [f(i) for i in x]
    print(y)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.title(f'Graph of ${f.__doc__}$ from {limit[0]} to {limit[1]}')
    plt.xlabel('x')  # x轴标签
    plt.ylabel('y')  # y轴标签
    plt.legend()  # 显示图例
    plt.grid(True)  # 显示网格
    plt.show()  # 显示图像


n = 100
d = np.random.rand(n) * 10
d[d > 5] *= 2
d[d < 5] /= 2
cv = np.std(d) / d.mean()
cs = skew(d)
alpha = 4 / cs ** 2
beta = 2 / d.mean() / cv / cs
a0 = d.mean() * (1 - 2 * cv / cs)
print(cs)
print(cv)

def func(x):
    y = gamma.pdf(x - a0, alpha, beta)
    return y


if __name__ == '__main__':
    functionGraph(func, (0, 100))
