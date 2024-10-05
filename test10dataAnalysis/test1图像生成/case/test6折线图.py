"""
折线图

"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def simpleLine(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制简单的折线图"""
    ax.plot(xs, ys, marker='+', linewidth=1, )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.set_title("simple line chart")


def multipleLine(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    markers = ['o', '+', 'x', '*', 's', 'd']
    for index, ys in enumerate(yss):
        ax.plot(xs, ys, linewidth=1, marker=markers[index], label=f'line-{index}')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.legend(title="legend")
    ax.set_title("multiple line chart")


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y1 = [3, 5, 4, 8, 10]
    y2 = [[1, 2, 3, 4, 5],
          [2, 4, 6, 8, 10],
          [3, 6, 9, 12, 15]]

    fig, axs = plt.subplots(2, 2)
    simpleLine(axs[0][0], x, y1)
    multipleLine(axs[0][1], x, y2)

    plt.show()
