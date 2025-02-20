"""
方中拟圆
"""
import math

import matplotlib
import matplotlib.pyplot as plt
from typing import Sequence

matplotlib.use('TkAgg')


def drawBlock(ax: plt.Axes, points: Sequence[Sequence[int]]):
    """根据点绘制方格，方格的锚点为左下角"""
    for x, y in points:
        ax.add_patch(plt.Rectangle((x, y), 1, 1, fill='black', edgecolor='red'))
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_tick_params(rotation=90)
    ax.grid(True)


def calcCircle(radius: float) -> Sequence[Sequence[int]]:
    """
    以方块顶点为圆心计算方块位置
    """
    # 计算第一象限内的点
    x, y = (0, int(radius))
    points = [(x, y)]
    while True:
        x += 1
        if not math.sqrt(x ** 2 + y ** 2) <= radius < math.sqrt((x + 1) ** 2 + (y + 1) ** 2):
            y -= 1
            x -= 1
        points.append((x, y))
        if x == int(radius) and y == 0:
            break
    # 对称其他象限的点
    points2 = []
    for x, y in points:
        points2.extend([
            (x, -y - 1), (-x - 1, y), (-x - 1, -y - 1)
        ])
    points.extend(points2)
    points = list(set(points))
    return points


def calcCircle2(radius: int):
    """
    中心圆算法

    以圆心为中心，利用圆的对称性，只需要计算圆的八分之一部分的点，然后通过对称关系得到整个圆上的点。
    对于给定的圆心坐标(0,0)和半径r，从x=0,y=r，开始，逐步计算下一个点的位置。
    通过判断中点与圆的位置关系来确定下一个点是在当前点的正下方还是右下方。
    """
    d = 1 - radius
    x = 0
    y = radius
    points = [(x, y)]
    # 循环计算圆上的点
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        points.append((x, y))
    # 对称出另外7/8
    points2 = []
    for x, y in points:
        points2.extend([
            (x, y), (- x, y), (x, - y), (- x, - y), (y, x), (- y, x), (y, - x), (- y, - x)
        ])
    points.extend(points2)
    points = list(set(points))
    return points

def calcEq(eq:callable,rang:[float,float],)

def equation(x: float) -> float:
    return x**2


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 2)

    # r = 40
    # ps1 = calcCircle(r)
    # ps2 = calcCircle2(r)
    # print(len(ps1), len(ps2))
    # print(ps1)
    # print(ps2)
    # drawBlock(axs[0], ps1)
    # drawBlock(axs[1], ps2)
    # axs[0].add_patch(plt.Circle((0, 0), r, fill=False))
    # axs[1].add_patch(plt.Circle((0.5, 0.5), r, fill=False))
    # axs[0].add_patch(plt.Circle((0, 0), r / 60, fill='yellow'))
    # axs[1].add_patch(plt.Circle((0.5, 0.5), r / 60, fill='yellow'))



    plt.show()
