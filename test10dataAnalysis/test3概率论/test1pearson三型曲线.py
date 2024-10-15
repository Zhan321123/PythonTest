"""
PⅢ曲线在水文学中的应用
"""
from typing import Sequence

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import skew, gamma

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def cumulativeFrequencyCurve(mean, cv, cs, ps: Sequence):
    """累计频率曲线法"""
    # 参数计算
    alpha = 4 / cs ** 2
    beta = 2 / mean / cv / cs
    a0 = mean * (1 - 2 * cv / cs)

    pdf = lambda x: gamma.pdf(x, alpha, beta)
    cdf = lambda x: gamma.cdf(x, alpha, beta)
    ppf = lambda p: gamma.ppf(p, alpha, beta)

    print('平均数:', mean)
    print("cs:", cs)
    print("cv:", cv)
    print('cs=n cv, n =', cs / cv)
    print('gamma参数为：', alpha, beta, a0)
    for p in ps:
        if 0 < p < 1:
            kp = (ppf(1 - p)) * cv + 1
            print(f'概率为{p:.1%}时的kp值{kp}')

    # 绘制频率曲线
    xs = np.linspace(ppf(0.0001), ppf(0.9999), 300)
    plt.figure(figsize=(10, 6))
    ys = [1 - cdf(i) for i in xs]
    plt.plot(ys, (xs * cv + 1) * mean, label='累积频率曲线')
    # ys = [pdf(i) for i in xs]
    # plt.plot(ys, xs, label='概率密度曲线')
    # plt.xscale('log')  # 对数坐标轴
    # plt.xlim(1e-4, 1 - 1e-4)
    # plt.ylim(a0, None)
    # xticks = np.array((0.1, 0.2, 0.33, 0.5, 1, 2, 5, 10, 20, 50, 75, 90, 95, 99))
    # plt.xticks(xticks / 100, xticks)
    plt.xlabel('p (%)')
    plt.ylabel('value')
    plt.legend()
    plt.grid(True)


if __name__ == '__main__':
    # 有35年该河流的流量（年最大），求100年一遇的洪水流量
    cumulativeFrequencyCurve(100, 0.6, 2.4, [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 0.75, 0.9, 0.95, 0.99])
    plt.show()
