"""
柱状图

"""
from typing import Sequence
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def simpleBar(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制简单柱状图"""
    bars = ax.bar(xs, ys, color='green', edgecolor='red', hatch='/', label='bar')
    ax.bar_label(bars, fmt='%.1f')  # 在每个柱子上方添加数值标注
    # 设置图表标题和坐标轴标签
    ax.set_title('simple bar')
    ax.tick_params(axis='both', colors='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()


def groupBar(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """绘制分组柱状图"""
    width = 0.2
    ind = np.arange(len(xs))
    for i, ys in enumerate(yss):
        b = ax.bar(ind + i * width, ys, width=width, label=f'group{i}')
        ax.bar_label(b, label_type='center')  # 在每个柱子中间添加数值标注
    ax.set_xticks(ind + width, xs)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('group bar')
    ax.legend()


def horizontalBar(ax, xs, ys):
    """绘制水平柱状图"""
    hbars = ax.barh(xs, ys, label='bar', alpha=0.5)
    ax.bar_label(hbars, padding=8, color='b', fontsize=14)  # 在每个柱子上方添加数值标注
    ax.set_title('simple bar')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()


def stackedBar(ax, xs, yss):
    """绘制堆叠柱状图"""
    for i, ys in enumerate(yss):
        b = ax.bar(xs, ys, bottom=np.sum(yss[:i], axis=0), label=f'group{i}')
        ax.bar_label(b, label_type='center')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('stacked bar')


def polarBar(ax, position, thetas, rs, widths):
    """绘制极坐标柱状图"""
    ax.remove()  # 移除直方ax
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(thetas))][0:len(thetas)]
    ax2 = fig.add_subplot(*position, polar=True)  # 添加极坐标ax
    ax2.bar(thetas, rs, widths, bottom=100, alpha=0.5, color=colors)
    ax2.set_title('polar bar')
    ax2.set_xlabel('theta')
    ax2.set_ylabel('r')


def bar3d(ax: plt.Axes, position: (int, int, int), xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
    """绘制三维柱状图"""
    ax.remove()
    x = list(range(len(xs))) * len(ys)
    y = list(range(len(ys))) * len(xs)
    top = [i for yss in zss for i in yss]
    bottom = [0] * len(top)
    ax = fig.add_subplot(*position, projection='3d', elev=30, azim=45, )
    ax.bar3d(x, y, bottom, 1, 1, top, shade=True, color='pink',alpha=0.8)
    ax.set_xticks(range(len(xs)), xs)
    ax.set_yticks(range(len(ys)), ys)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D bar')


if __name__ == '__main__':
    fig, axs = plt.subplots(2, 3)

    x1 = ['A', 'B', 'C', 'D', 'E']
    x2 = ['a', 'b', 'c', 'd']
    y1 = [300, 234, 561, 272, 105]
    y2 = [[100, 200, 300, 400, 500],
          [300, 400, 500, 600, 700],
          [500, 600, 700, 800, 900],
          [700, 800, 900, 100, 200]]

    simpleBar(axs[0][0], x1, y1)
    horizontalBar(axs[0][1], x1, y1)
    groupBar(axs[0][2], x1, y2)
    stackedBar(axs[1][0], x1, y2)

    ts = [0, 1, 2, 3, 3.14]
    ws = [0.4, 0.8, 0.3, 1, 2]
    polarBar(axs[1][1], (2, 3, 5), ts, y1, ws)  # position:(2,3,4)，表示在2×3网格中的第4个位置
    bar3d(axs[1][2], (2, 3, 6), x1, x2, y2)

    plt.show()
