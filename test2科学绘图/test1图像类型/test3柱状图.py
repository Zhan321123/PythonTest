"""
简单柱状图
水平柱状图
堆叠柱状图
分组柱状图
三维柱状图
极轴柱状图
直方图
阶梯图
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
    xs, ys = np.array(xs), np.array(ys)
    bars = ax.bar(xs, ys, color='green',  # 填充颜色
                  edgecolor='red',  # 边框颜色
                  hatch='/',  # 填充线条，有/,x,+,|,*,-
                  label='bar', )
    ax.bar_label(bars, fmt='%.1f')  # 在每个柱子上方添加数值标注
    ax.set_title('simple bar')  # 图表标题
    ax.tick_params(axis='both', colors='blue')  # 设置坐标轴颜色
    ax.set_xlabel('x')  # 坐标轴标签
    ax.set_ylabel('y')
    ax.legend()


def groupBar(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """绘制分组柱状图"""
    xs, yss = np.array(xs), np.array(yss)
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
    xs, ys = np.array(xs), np.array(ys)
    hbars = ax.barh(xs, ys, label='bar', alpha=0.5)
    ax.bar_label(hbars, padding=8, color='b', fontsize=14)  # 在每个柱子上方添加数值标注
    ax.set_title('simple bar')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()


def stackedBar(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """绘制堆叠柱状图"""
    xs, yss = np.array(xs), np.array(yss)
    for i, ys in enumerate(yss):
        b = ax.bar(xs, ys, bottom=np.sum(yss[:i], axis=0), label=f'group{i}')
        ax.bar_label(b, label_type='center')  # 在每个柱子中间添加数值标注
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.set_title('stacked bar')


def polarBar(ax: plt.Axes, thetas: Sequence, rs: Sequence, widths: Sequence):
    """
    绘制极坐标柱状图
    :param ax: plt.Axes
    :param thetas: 扇形起始角度，弧度制，锚点为扇形中心
    :param rs: 扇形高度
    :param widths: 扇形宽度范围，弧度制
    """
    thetas, rs, widths = np.array(thetas), np.array(rs), np.array(widths)
    fig = ax.figure
    ax.remove()
    ax2 = fig.add_subplot(ax.get_subplotspec(), polar=True)  # 添加极坐标ax
    cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
    colors = cmap(np.arange(cmap.N))[::int(256 / len(thetas))][0:len(thetas)]
    ax2.bar(thetas, rs, widths, bottom=100, alpha=0.5, color=colors)
    ax2.set_title('polar bar')
    ax2.set_xlabel('theta')
    ax2.set_ylabel('r')


def bar3d(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
    """
    绘制三维柱状图

    :param ax: plt.Axes
    :param xs: x轴标签
    :param ys: y轴标签
    :param zss: [x][y]二维数据
    """
    xs, ys, zss = np.array(xs), np.array(ys), np.array(zss)
    fig = ax.figure
    ax.remove()
    ax = fig.add_subplot(ax.get_subplotspec(), projection='3d', elev=30, azim=45, )
    xrange, yrange = np.arange(len(xs)), np.arange(len(ys))
    X, Y = np.meshgrid(xrange, yrange)
    ax.bar3d(X.flatten(), Y.flatten(), np.zeros_like(X.flatten()), dx=1, dy=1, dz=zss.flatten(), shade=True,
             color='pink', alpha=0.8)
    ax.set_xticks(xrange, xs)
    ax.set_yticks(yrange, ys)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D bar')


def histChart(ax: plt.Axes, n: int, ys: Sequence):
    """绘制直方图"""
    ys = np.array(ys)
    ax.hist(ys, bins=n, histtype='step', facecolor='green')  # histtype='step'表示直方图边缘为直线，不填充
    ax.set_title('hist chart')


def stairChart(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制阶梯图"""
    xs, ys = np.array(xs), np.array(ys)
    ax.step(xs, ys, where='post')
    ax.set_xlim(0, len(xs) - 1)
    ax.grid()
    ax.set_title('stair chart')


if __name__ == '__main__':
    fig, axs = plt.subplots(3, 3)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

    x1 = ['A', 'B', 'C', 'D', 'E']
    x2 = ['a', 'b', 'c', 'd']
    y1 = [300, 234, 561, 272, 105]
    y2 = [[100, 200, 300, 400, 500],
          [300, 400, 500, 600, 700],
          [500, 600, 700, 800, 900],
          [700, 800, 900, 100, 200]]
    y3 = np.random.standard_normal(1000)  # 标准正态分布随机数1000个

    simpleBar(axs[0][0], x1, y1)
    horizontalBar(axs[0][1], x1, y1)
    groupBar(axs[0][2], x1, y2)
    stackedBar(axs[1][0], x1, y2)

    ts = [0, 1, 2, 3, 3.14]
    ws = [0.4, 0.8, 0.3, 1, 2]
    polarBar(axs[1][1], ts, y1, ws)  # position:(2,3,4)，表示在2×3网格中的第4个位置
    bar3d(axs[1][2], x1, x2, y2)
    histChart(axs[2][0], 10, y3)
    stairChart(axs[2][1], x1, y1)

    plt.show()
