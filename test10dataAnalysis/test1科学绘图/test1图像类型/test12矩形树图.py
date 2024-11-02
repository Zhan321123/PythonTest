"""
squarify库，绘制矩形树图
"""
from typing import Sequence

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import squarify

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def rectTree(ax: plt.Axes, sizes: Sequence, labels: Sequence):
    """矩形树图"""
    sizes = np.array(sizes)
    squarify.plot(ax=ax, sizes=sizes, label=labels, alpha=0.7,
                  color=matplotlib.colormaps['rainbow'](sizes / sizes.max()), pad=True)
    ax.axis('off')  # 关闭坐标轴
    ax.set_title('矩形树图')


if __name__ == '__main__':
    l = list('ABCDEFGHIJ')
    s = [1, 1, 3, 5, 8, 13, 21, 34, 55, 89]

    fig, axs = plt.subplots(1, 2)
    axs = axs.flatten()
    rectTree(axs[0], s, l)

    plt.show()
