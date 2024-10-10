"""
泰森多边形
"""
import random
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib
from scipy.spatial import Voronoi, voronoi_plot_2d

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def voronoiChart(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """泰森多边形"""
    points = list(zip(xs, ys))
    vor = Voronoi(points)  # 计算泰森多边形
    # 绘制泰森多边形
    voronoi_plot_2d(vor, ax=ax)
    ax.scatter(xs, ys, color='red', s=50, zorder=10, label='Points')  # 绘制原始点
    ax.set_title('泰森多边形')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()

if __name__ == '__main__':
    x = [random.randint(0, 100) for _ in range(100)]
    y = [random.randint(0, 100) for _ in range(100)]

    fig, axs = plt.subplots(1, 2)
    voronoiChart(axs[0], x, y)

    plt.show()
