"""
方中拟圆
"""
import matplotlib
import matplotlib.pyplot as plt
from typing import Sequence

import numpy as np

matplotlib.use('TkAgg')


def drawSquare(ax: plt.Axes, points: Sequence[Sequence[int]]):
    """
    绘制二维方形，锚点为方形左下角

    :param ax: plt.Axes
    :param points: 平面整数点集
    """
    for x, y in points:
        ax.add_patch(plt.Rectangle((x, y), 1, 1, fill='black', edgecolor='red'))
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.xaxis.set_tick_params(rotation=90)
    ax.grid(True)


def drawBlock(ax: plt.Axes, points: Sequence[Sequence[int]]):
    """
    绘制三维方块

    :param ax: plt.Axes
    :param points: 空间整数点集
    """
    ax.remove()
    ax = fig.add_subplot(ax.get_subplotspec(), projection='3d', elev=30, azim=45, )
    X, Y, Z = list(zip(*points))
    ax.bar3d(X, Y, Z, dx=1, dy=1, dz=1, shade=True,
             color='pink', )
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 设置xyz刻度间距为1
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.zaxis.set_major_locator(plt.MultipleLocator(1))


def calcCircle(radius: int):
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


def calcSphere(radius: int)-> Sequence[Sequence[int]]:
    """
    栅格化球体表面
    引用自：https://stackoverflow.com/questions/41656006/how-to-rasterize-a-sphere/41666156#41666156

    :param radius: 整数球体半径radius
    :return: 坐标列表
    """
    radius += 0.5

    def mirror(x, y, z, bs):
        """镜像卦限"""
        positions = [
            (x, y, z), (-x, y, z),
            (x, -y, z), (-x, -y, z),
            (x, y, -z), (-x, y, -z),
            (x, -y, -z), (-x, -y, -z)
        ]
        bs.extend(positions)

    blocks = []
    maxR2 = int(np.floor(radius * radius))
    zMax = int(np.floor(radius))
    x = 0
    while True:
        # 当 x^2 + zMax^2 大于 maxR2 且 zMax 大于等于 x 时，减小 zMax
        while x * x + zMax * zMax > maxR2 and zMax >= x:
            zMax -= 1
        # 如果 zMax 小于 x，说明当前 x 下 z 无法成为最大值，跳出循环
        if zMax < x:
            break
        z = zMax
        y = 0
        while True:
            # 当 x^2 + y^2 + z^2 大于 maxR2 且 z 大于等于 x 和 y 时，减小 z
            while x * x + y * y + z * z > maxR2 and z >= x and z >= y:
                z -= 1
            # 如果 z 小于 x 或 z 小于 y，说明当前 x 和 y 下 z 无法成为最大值，跳出循环
            if z < x or z < y:
                break
            # 旋转和镜像其他卦限坐标
            mirror(x, y, z, blocks)
            mirror(y, z, x, blocks)
            mirror(z, x, y, blocks)
            y += 1
        x += 1

    return blocks


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 1)

    # r=20
    # ps1 = calcCircle(r)
    # print(ps1)
    # drawSquare(axs, ps1)
    # axs.add_patch(plt.Circle((0.5, 0.5), r, fill=False))
    # axs.add_patch(plt.Circle((0.5, 0.5), r / 60, fill='yellow'))

    points = calcSphere(12)
    drawBlock(axs, points)

    plt.show()
