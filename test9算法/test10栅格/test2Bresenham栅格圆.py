import matplotlib.pyplot as plt

from test1drawBlocks import *


def circleBresenham(radius: int) -> planarPoints:
    """
    Bresenham算法栅格圆形

    以圆心为中心，利用圆的对称性，只需要计算圆的八分之一部分的点，然后通过对称关系得到整个圆上的点。
    对于给定的圆心坐标(0,0)和半径r，从x=0,y=r，开始，逐步计算下一个点的位置。
    通过判断中点与圆的位置关系来确定下一个点是在当前点的正下方还是右下方。
    """
    d = 1 - radius
    x = 0
    y = radius
    points = {(x, y)}
    # 循环计算圆上的点
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        points.add((x, y))
    # 对称出另外7/8
    points2 = []
    for x, y in points:
        points2.extend([
            (x, y), (- x, y), (x, - y), (- x, - y),
            (y, x), (- y, x), (y, - x), (- y, - x)
        ])
    points.update(points2)
    return points

if __name__ == '__main__':

    fig, axs = plt.subplots(1, 1)
    ps1 = circleBresenham(20)
    print(ps1)
    drawSquare(axs, ps1, )

    plt.show()