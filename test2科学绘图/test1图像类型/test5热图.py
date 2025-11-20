"""
可插补的热图
    插补方法：'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
            'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
            'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'
带边框的热图
辛顿图
"""
from typing import Sequence
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

mpl.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

_interpolations = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
                   'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']


def imshowChart(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence], interpolation: str = 'none'):
  """
  热图，带注释，无格子边框，可插补interpolation
  :param ax:
  :param xs:
  :param ys:
  :param zss:
  :param interpolation: 插补方法，有['none', 'nearest', 'bilinear', 'bicubic',
                                   'spline16', 'spline36', 'hanning', 'hamming',
                                   'hermite','kaiser', 'quadric', 'catrom',
                                   'gaussian', 'bessel', 'mitchell', 'sinc',
                                   'lanczos']
  :return:
  """
  if not interpolation in _interpolations:
    interpolation = 'none'
  colors = [(0, '#FF0000'), (0.5, '#FFFF00'), (1, '#00FF00')]
  cmap = LinearSegmentedColormap.from_list('custom', colors)
  im = ax.imshow(zss, cmap=cmap, interpolation=interpolation)
  fig.colorbar(im, ax=ax, pad=0.05, shrink=1)  # 给ax添加色带，偏移0.05倍宽，大小缩放1倍
  # 循环数据标注并创建文本注释。
  for i in range(len(xs)):
    for j in range(len(ys)):
      ax.text(j, i, zss[i][j], ha="center", va="center", color="w")
  ax.set_xticks(np.arange(len(xs)), labels=xs)
  ax.set_yticks(np.arange(len(ys)), labels=ys)
  ax.set_title("imshow chart")


def pcolormeshChart(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
  """
  热图，不带注释，有格子边框，不可插补
  :param ax:
  :param xs:
  :param ys:
  :param zss:
  :return:
  """
  cmap = LinearSegmentedColormap.from_list('blue', [(0, '#e1eef7'), (1, '#026db3')])
  zss = np.array(zss)
  pc = ax.pcolormesh(zss, cmap=cmap, linewidth=0.5,  # 格子边框宽度
    edgecolors='k',  # 格子边框颜色
    vmin=zss.min(), vmax=zss.max())  # 色值范围，大于使用max的颜色，小于使用min
  fig.colorbar(pc, ax=ax, pad=0.05, shrink=1)  # 给ax添加色带
  ax.set_aspect(1)  # 让每一格宽高一致
  ax.set_xticks(np.arange(len(xs)) + 0.5, labels=xs)
  ax.set_yticks(np.arange(len(ys)) + 0.5, labels=ys)
  ax.set_title("pcolormesh chart")


def hinton(ax: plt.Axes, dss: Sequence[Sequence], max_weight=None, ):
  """
  Hinton图
  :param ax: plt.Axes
  :param dss: (x, y)点的值
  :param max_weight: 颜色最大值
  :return:
  """
  if not max_weight:
    max_weight = 2 ** np.ceil(np.log2(np.abs(dss).max()))
  ax.patch.set_facecolor('gray')  # 设置背景色
  ax.set_aspect('equal', 'box')  # 设置格子长宽相等
  ax.xaxis.set_major_locator(plt.NullLocator())  # 不显示xy轴刻度
  ax.yaxis.set_major_locator(plt.NullLocator())
  for (x, y), w in np.ndenumerate(dss):
    color = 'white' if w > 0 else 'black'
    size = np.sqrt(abs(w) / max_weight)
    rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
      facecolor=color, edgecolor=color)
    ax.add_patch(rect)
  ax.autoscale_view()  # 自动调整，显示整个图像
  ax.invert_yaxis()  # 翻转y轴
  ax.set_title("Hinton diagram")

if __name__ == '__main__':
  x1 = ["A", "B", "C", "D", "E", "F", "G"]
  y1 = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"]
  d1 = [[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
        [2.4, 7.0, 4.0, 1.0, 2.7, 0.0, 0.0],
        [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
        [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
        [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
        [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
        [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]]
  d2 = [
    [0, 0, 1548, 3000, 2997, 3000, 3000, 3000, 3000, 3000, 3000, 3000],
    [5000, 0, 3000, 1004, 1000, 3028, 1004, 1008, 3000, 1008, 1004, 1004],
    [3968, 500, 0, 2234, 2308, 3056, 509, 521, 2832, 3081, 1300, 533],
    [3000, 999, 2229, 0, 2500, 3000, 3000, 3000, 3000, 3000, 3000, 3000],
    [3002, 1000, 2313, 2500, 0, 3001, 1003, 3002, 2500, 3002, 1003, 1003],
    [3000, 493, 1846, 3000, 2996, 0, 3000, 3000, 3000, 3000, 3000, 3000],
    [3000, 999, 2989, 3000, 1003, 3000, 0, 3000, 3000, 3000, 3000, 3000],
    [3000, 998, 2956, 3000, 2997, 3000, 3000, 0, 3000, 3000, 3000, 3000],
    [3000, 500, 2032, 3000, 2500, 3000, 3000, 3000, 0, 3000, 3000, 3000],
    [3000, 998, 1876, 3000, 2997, 3000, 3000, 3000, 3000, 0, 3000, 3000],
    [3000, 999, 2605, 3000, 1003, 3000, 3000, 3000, 3000, 3000, 0, 3000],
    [3000, 999, 2893, 3000, 1003, 3000, 3000, 3000, 3000, 3000, 3000, 0],
  ]

  fig, axs = plt.subplots(1, 1)
  # plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

  # imshowChart(axs[0][0], x1, y1, d1)
  # pcolormeshChart(axs[0][1], x1, y1, d1)
  # hinton(axs[0][2], d2)

  plt.show()
