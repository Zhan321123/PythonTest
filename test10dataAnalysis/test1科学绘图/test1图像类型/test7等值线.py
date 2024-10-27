"""
等值线
"""
from typing import Sequence

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MaxNLocator

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def contour(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
    """等值线图"""
    zss = np.array(zss)
    c = ax.contour(xs, ys, zss, MaxNLocator().tick_values(zss.min(), zss.max()))
    c.clabel(fmt='%1.1f')

    ax.set_aspect(1)
    ax.xaxis.set_major_locator(plt.NullLocator())  # 不显示xy轴刻度
    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.set_title("contour chart")

if __name__ == '__main__':
    x, y = np.arange(0, 10, 1), np.arange(0, 10, 1)
    # 生成2维矩阵
    z = np.arange(100).reshape(10, 10)
    for i in range(5):
        z[i:10 - i, i:10 - i] = z[i:10 - i, i:10 - i] * 1.4

    fig, axs = plt.subplots(1,2)
    axs = axs.flatten()
    contour(axs[0], x, y, z)

    plt.show()

