"""
箱图
"""
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def boxChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """普通箱图"""
    bplot = ax.boxplot(yss, patch_artist=True, tick_labels=xs)  # 填充颜色、设置xtick标签
    xs = np.arange(len(xs))
    for patch, color in zip(bplot['boxes'], matplotlib.colormaps["rainbow"](xs / max(xs))):
        patch.set_facecolor(color)  # 修改填充颜色
    ax.set_title('Rectangular box plot')


def boxChart2(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """带形状的箱图"""
    # notch槽口形状、vert垂直框对齐
    bplot = ax.boxplot(yss, notch=True, vert=True, patch_artist=True, tick_labels=xs)
    xs = np.arange(len(xs))
    for patch, color in zip(bplot['boxes'], matplotlib.colormaps["rainbow"](xs / max(xs))):
        patch.set_facecolor(color)  # 修改填充颜色
    ax.set_title('Notched box plot')


def violinChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
    """小提琴图"""
    part = ax.violinplot(yss, showmeans=False, showmedians=True)
    xs = np.arange(len(xs))
    cs = matplotlib.colormaps["rainbow"](xs / max(xs))
    for index, pc in enumerate(part['bodies']):
        pc.set_facecolor(cs[index])  # 修改填充颜色
        pc.set_edgecolor('black')
        pc.set_alpha(0.6)
    ax.set_xticks(range(1, len(xs) + 1), x)
    ax.set_title('Violin plot')


if __name__ == '__main__':
    y1 = np.random.rand(30, 10) * 100
    y1[y1 > 80] = np.random.randint(100, 200)
    y1[y1 < 20] = np.random.randint(-100, 0)
    x = list(f"x{i}" for i in range(len(y1[0])))

    fig, axs = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距
    boxChart(axs[0][0], x, y1)
    boxChart2(axs[0][1], x, y1)
    violinChart(axs[1][0], x, y1)

    plt.show()
