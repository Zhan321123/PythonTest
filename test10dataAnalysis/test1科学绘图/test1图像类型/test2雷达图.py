"""
雷达图
TODO
简单雷达图
多条雷达图
堆叠雷达图
"""
from typing import Sequence

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def radar(ax: plt.Axes, position, xs: Sequence, ys: Sequence):
    """绘制雷达图"""


def multipleRadar(ax: plt.Axes, position, xs: Sequence, yss: Sequence[Sequence]):
    """绘制多条雷达图"""


def stackRadar(ax: plt.Axes, position, xs: Sequence, yss: Sequence[Sequence]):
    """绘制堆叠雷达图"""


if __name__ == '__main__':
    x = ['N', 'NE', 'E', 'ES', 'S', 'SW', 'W', 'WN']
    y1 = [1, 2, 3, 4, 5, 6, 7, 8]
    y2 = np.arange(0, 8 * 7).reshape(7, 8)

    fig, axs = plt.subplots(2, 2)
    axs = axs.flatten()
    radar(axs[0], (2, 2, 1), x, y1)
    multipleRadar(axs[1], (2, 2, 2), x, y2)
    stackRadar(axs[2], (2, 2, 3), x, y2)

    plt.show()
