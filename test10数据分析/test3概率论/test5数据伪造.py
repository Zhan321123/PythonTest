"""
数据伪造
"""
from typing import Sequence
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def displayRandom(ax: plt.Axes, size=1000):
    data = {
        '正态分布': np.random.normal(0, 3, size),  # 均值为 0，标准差为 3，大部分数据会在 -9 到 9 之间
        '随机数': np.random.random(size) * 20 - 10,  # 将 [0, 1) 区间映射到 [-10, 10)
        '随机整数': np.random.randint(-10, 10, size),  # 生成 -10 到 9 之间的随机整数
        '标准正态分布': np.random.randn(size) * 3,  # 标准差为 3，大部分数据会在 -9 到 9 之间
        'gamma': np.random.gamma(2, 2, size) - 5,  # 调整形状和尺度参数，并进行平移
        'beta': np.random.beta(2, 2, size) * 20 - 10,  # 将 [0, 1) 区间映射到 [-10, 10)
        '指数': np.random.exponential(2, size) - 10,  # 尺度参数为 2，并进行平移
        '泊松': np.random.poisson(3, size) - 5,  # 调整 λ 参数，并进行平移
        '威布尔': np.random.weibull(2, size) * 5 - 5,  # 调整形状参数，并进行缩放和平移
        '拉普拉斯': np.random.laplace(0, 2, size),  # 均值为 0，尺度为 2
        '高斯': np.random.rayleigh(3, size) - 5,  # 调整尺度参数，并进行平移
        '正态': np.random.lognormal(0, 0.5, size) - 5,  # 调整标准差，并进行平移
        '卡方': np.random.chisquare(5, size) - 10,  # 调整自由度，并进行平移
        'Wald': np.random.wald(5, 2, size) - 10,  # 调整参数，并进行平移
        '三角': np.random.triangular(-10, 0, 10, size),  # 保持原参数
        '均匀': np.random.uniform(-10, 10, size)  # 保持原参数
    }
    violinChart(ax, list(data.keys()), list(data.values()))


def violinChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """小提琴图"""
    part = ax.violinplot(yss, showmeans=False, showmedians=True)
    cs = matplotlib.colormaps["rainbow"](np.arange(len(xs)) / max(np.arange(len(xs))))
    for index, pc in enumerate(part['bodies']):
        pc.set_facecolor(cs[index])  # 修改填充颜色
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)
    ax.set_xticks(range(1, len(xs) + 1), xs)
    ax.set_title('Violin plot')


if __name__ == '__main__':
    fig, ax = plt.subplots()
    displayRandom(ax)
    plt.show()
