"""
简单折线图
多条折线图
堆叠区域折线图
茎图
极轴折线图
"""
from typing import Sequence
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def simpleLine(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制简单的折线图"""
    xs,ys = np.array(xs), np.array(ys)
    ax.plot(xs, ys, marker='+', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.set_title("simple line chart")


def multipleLine(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """多条折线图"""
    xs,yss = np.array(xs), np.array(yss)
    markers = ['o', 's', 'd', 'v']
    linestyles = ['-', '--', '-.', ':']  # 实线、虚线、点划线、点线
    for index, ys in enumerate(yss):
        ax.plot(xs, ys, linewidth=1, marker=markers[index], label=f'line-{index}',
                linestyle=linestyles[index])  # 线型
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.legend(title="legend")
    ax.set_title("multiple line chart")


def stackLine(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """堆栈折线图"""
    xs, ys = np.array(xs), np.array(yss)
    labels = list(f"line-{i}" for i in range(len(yss)))
    ax.stackplot(xs, yss, labels=labels, alpha=0.8)
    ax.legend(reverse=True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    ax.set_title('stack line chart')


def stemLine(ax: plt.Axes, xs: Sequence, ys: Sequence, bottom: float):
    """
    茎图

    :param ax: plt.Axes
    :param xs: x轴标签
    :param ys: y轴值
    :param bottom: 底
    """
    xs, ys = np.array(xs), np.array(ys)
    ax.stem(xs, ys)
    ax.stem(xs, ys, bottom=bottom, markerfmt='D', linefmt='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()
    ax.set_title('stem line chart')


def polarLine(ax: plt.Axes, thetas: Sequence, rs: Sequence):
    """极坐标折线图"""
    thetas, rs = np.array(thetas), np.array(rs)
    fig = ax.figure
    ax.remove()
    ax = fig.add_subplot(ax.get_subplotspec(), polar=True)
    ax.plot(thetas, rs, marker='o', linewidth=1)
    ax.set_xlabel('theta')
    ax.set_ylabel('r')
    ax.set_title('polar line chart')


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y1 = [3, 5, 4, 8, 10, 12, 11, 14]
    y2 = [[1, 2, 4, 4, 5, 6, 8, 10],
          [2, 4, 5, 9, 10, 12, 15, 11],
          [3, 6, 8, 14, 17, 19, 22, 20],
          [4, 8, 12, 20, 25, 28, 30, 26]]

    fig, axs = plt.subplots(2, 3)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

    simpleLine(axs[0][0], x, y1)
    multipleLine(axs[0][1], x, y2)
    stackLine(axs[1][0], x, y2)
    stemLine(axs[1][1], x, y1, 6)
    polarLine(axs[0][2], x, y1)

    plt.show()
