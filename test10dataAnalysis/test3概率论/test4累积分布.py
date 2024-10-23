from typing import Sequence
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def cumulativeDistribution(ax: plt.Axes, ys: Sequence):
    """累积分布曲线"""
    ax.hist(ys, bins=20, density=True, histtype="step", label="histogram")
    ax.ecdf(ys, label='CDF')  # 累积曲线
    ax.hist(ys, bins=20,  # 直方图的分段数
            density=True,  # 是否显示频数
            histtype="step",  # 直方图类型
            cumulative=True,  # 累积曲线
            label="cumulative histogram")
    ax.ecdf(ys, complementary=True, label='CCDF')  # 互补累积曲线
    ax.hist(ys, bins=20, density=True, histtype="step", cumulative=-1, label="Reversed cumulative histogram")
    ax.legend(framealpha=0.2)

if __name__ == '__main__':
    y1 = np.random.normal(0, 1, size=1000)  # 生成1000个正态分布数据
    print(y1)

    fig, axs = plt.subplots(2, 2)
    axs = axs.flat
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    cumulativeDistribution(axs[0], y1)
    plt.show()
