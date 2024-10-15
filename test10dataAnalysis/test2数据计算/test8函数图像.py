"""
画出图像
"""
import math

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats import gamma, skew

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def functionGraph(fs: [callable], limit: tuple[float, float], fineness=300):
    """
    画出函数图像

    :param fs: [函数def,]
    :param limit: 上下限
    :param fineness: 点数，点越多曲线更平滑
    """
    x = np.linspace(*limit, fineness)
    plt.figure(figsize=(10, 6))
    xs = np.array(x)
    xs *= cv
    xs += 1
    xs *= mean
    for f in fs:
        y = [f(i) for i in x]
        plt.plot(xs, y, label=f'{f.__doc__}')
    plt.ylim(1)
    # plt.xscale('log')  # 对数坐标轴
    yticks = np.array((0.01, 0.1, 0.2, 0.33, 0.5, 1, 2, 5, 10, 20, 50, 75, 90, 95, 99))
    plt.yticks(yticks / 100, yticks)
    plt.xlabel('x')  # x轴标签
    plt.ylabel('y')  # y轴标签
    plt.legend()  # 显示图例
    plt.grid(True)  # 显示网格
    plt.show()  # 显示图像


d = np.array((18500, 17700, 13900, 13300, 12800, 12100, 12000, 11500, 11200, 10800, 10800, 10700, 10600, 10500, 9690,
              8500, 8220, 8150, 8020, 8000, 7850, 7450, 7290, 6160, 5960, 5950, 5590, 5490, 5340, 5220, 5100, 4520,
              4240, 3650, 3220))

mean = d.mean()
cv = np.std(d) / mean
cs = skew(d)
alpha = 4 / cs ** 2
beta = 2 / mean / cv / cs
a0 = mean * (1 - 2 * cv / cs)
print(cs)
print(cv)
print(a0, alpha, beta)
print('x ba', mean)
print('cs=x cv', cs / cv)

print((gamma.ppf(0.1, alpha, beta) * cv + 1) * mean)
print((gamma.ppf(0.9, alpha, beta) * cv + 1) * mean)


def f1(x):
    """pdf"""
    y = gamma.pdf(x, alpha, beta)
    return y


def f2(x):
    """cdf"""
    y = gamma.cdf(x, alpha, beta)
    return y


if __name__ == '__main__':
    functionGraph([f1, f2], (gamma.ppf(0.0001, alpha, beta), gamma.ppf(0.9999, alpha, beta)))
