"""
条形色带图参照：
    https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py

matplotlib.colormaps所有官方色带

反向色带添加_r：
    Append _r to the name of any built-in colormap to get the reversed version
    example:'viridis', 'viridis_r'

自定义colormap
    colors = [(int, color)]
    cmap = LinearSegmentedColormap.from_list('colormap name', colors)
    int范围0-1，color为 #161616进制颜色
    colormap name不可直接用

获取单个颜色
    cmap(0~1)|(1~255)，注意这里是()不是[]

使用方法：
    1、定义colormap，自定义cmap = cmap 或 matplotlib.colormaps["色带名"]
    2、c=colors(index / len(ys)) 或 colors(ys / ys.max())
    3、ax.图(*args, color=c)

顶级配色
    [(0, '#F7B7D2'),(1 / 4, '#EEC186'),(2 / 4, '#EEF0A7'),(3 / 4, '#B8E5FA'),(1, '#B2DBB9')]
    [(0, '#EECA40'),(1 / 2, '#FD763F'),(1, '#23BAC5')]
    [(0, '#ECE70F'),(1 / 2, '#688CC8'),(1, '#00A14E')]
    [(0, '#d83f31'),(1 / 4, '#fabe7c'),(2 / 4, '#fafebf'),(3 / 4, '#b7d8e6'),(1, '#517db5')]

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import matplotlib

matplotlib.use("TkAgg")

print("-----------获取所有颜色表colormaps----------")
print(matplotlib.colormaps)  # 所有官方色带
rainbow = matplotlib.colormaps["rainbow"]

print("-----------自定义colormap-----------")
colors1 = [(0, '#FF0000'),  # 红色
           (0.5, '#FFFF00'),  # 黄色
           (1, '#00FF00')]  # 绿色
colors2 = [(0, '#000000'), (1, '#FFFFFF')]  # 白色、黑色
c1 = LinearSegmentedColormap.from_list('name', colors1)
c2 = LinearSegmentedColormap.from_list('name', colors2)

print("-----------获取单个颜色----------")
# 0<x<1
print(0, ' \t', c2(0))  # 0是最左颜色，1是最右颜色
print(0.5, '\t', c2(0.5))
print(1, ' \t', c2(1))
# 0<x<255
print(200.0, '\t', c2(200.0))  # x/255对应到0-1之间
print(255, '\t', c2(255))
# x<0 || x>255
print(-1, ' \t', c2(-1))  # 低于0，显示0
print(100000, '\t', c2(100000))  # 超过255，显示255

print("-----------获取多颜色colors-----------")
cs1 = c2([0, 0.5, 1])  # 对于数据在0-1之间的可以直接作为参数
print(cs1)
d = np.arange(3)
print(c2(d))
print(c2(d / d.max()))  # d/d.max()，归一化


def line(ax: plt.Axes, xs, yss):
    colors = matplotlib.colormaps["rainbow"]
    for index, ys in enumerate(yss):
        ax.plot(xs, ys, linewidth=1, color=colors(index / len(yss)))


def bar1(ax: plt.Axes, xs, ys):
    c = c2(ys)
    ax.bar(xs, ys, color=c)


def bar2(ax: plt.Axes, xs, ys):
    c = c2(ys / ys.max())
    ax.bar(xs, ys, color=c)


def hotmap(ax: plt.Axes, yss):
    ax.imshow(yss, cmap=c1)


def showAllCmap(ax: plt.Axes):
    colormaps = list(matplotlib.colormaps())
    xs = np.linspace(0,256,6)
    for i, colormap in enumerate(colormaps):
        colors = matplotlib.colormaps[colormap](xs)
        ax.bar(xs,[i]*len(xs),bottom=i,width=40, color=colors)
    ax.set_title("all colormaps")


if __name__ == '__main__':
    x1 = np.arange(5)
    y1 = np.arange(1, 101).reshape(20, 5)  # 生成一个20行5列的递增数列
    x2 = np.arange(-100, 500)
    y2 = [[0, 1, 3, 6],
          [2, 4, 7, 10],
          [5, 8, 11, 13],
          [9, 12, 14, 15]]

    fig, axs = plt.subplots(2, 3)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

    line(axs[0, 0], x1, y1)
    bar1(axs[1, 0], x2, x2)
    bar2(axs[1, 1], x2, x2)
    hotmap(axs[0, 1], y2)
    showAllCmap(axs[1, 2])
    plt.show()
