"""
带注释的热图
    https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py
Hinton图
    https://matplotlib.org/stable/gallery/specialty_plots/hinton_demo.html#sphx-glr-gallery-specialty-plots-hinton-demo-py

插补方法：
    'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
    'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
    'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'

plt.imshow(data, cmap=cmap)
plt.pcolormesh(data, cmap=cmap,edgecolors='', linewidth=int)


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
    """热图，带注释，无格子边框，可插补"""
    if not interpolation in _interpolations:
        interpolation = 'none'
    colors = [(0, '#FF0000'), (0.5, '#FFFF00'), (1, '#00FF00')]
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    im = ax.imshow(zss, cmap=cmap, interpolation=interpolation)
    fig.colorbar(im, ax=ax, pad=0.05, shrink=1)  # 给ax添加色带
    # 循环数据标注并创建文本注释。
    for i in range(len(xs)):
        for j in range(len(ys)):
            ax.text(j, i, zss[i][j], ha="center", va="center", color="w")
    ax.set_xticks(np.arange(len(xs)), labels=xs)
    ax.set_yticks(np.arange(len(ys)), labels=ys)
    ax.set_title("imshow chart")


def pcolormeshChart(ax: plt.Axes, xs: Sequence, ys: Sequence, zss: Sequence[Sequence]):
    """热图，不带注释，有格子边框，不可插补"""
    cmap = LinearSegmentedColormap.from_list('blue', [(0, '#e1eef7'), (1, '#026db3')])
    pc = ax.pcolormesh(zss, cmap=cmap, linewidth=0.5, edgecolors='k')
    fig.colorbar(pc, ax=ax, pad=0.05, shrink=1)  # 给ax添加色带
    ax.set_aspect(1)  # 让每一格宽高一致
    ax.set_xticks(np.arange(len(xs)) + 0.5, labels=xs)
    ax.set_yticks(np.arange(len(ys)) + 0.5, labels=ys)
    ax.set_title("pcolormesh chart")


def hinton(ax, dss, max_weight=None, ):
    """Hinton图"""
    if not max_weight:
        max_weight = 2 ** np.ceil(np.log2(np.abs(dss).max()))
    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    for (x, y), w in np.ndenumerate(dss):
        color = 'white' if w > 0 else 'black'
        size = np.sqrt(abs(w) / max_weight)
        rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)
    ax.autoscale_view()
    ax.invert_yaxis()
    ax.set_title("Hinton diagram")


if __name__ == '__main__':
    x = ["A", "B", "C", "D", "E", "F", "G"]
    y = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg"]
    d1 = [[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
          [2.4, 7.0, 4.0, 1.0, 2.7, 0.0, 0.0],
          [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
          [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
          [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
          [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
          [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]]
    d2 = [
        [2, -5, 1, 7, -9, 2, -7, 3],
        [4, 1, 6, 8, 1, -3, -6, -2],
        [3, -2, 7, -9, -3, 7, 6, 1],
        [3, 5, 1, -7, 2, 5, -4, -1],
        [3, 7, 1, -7, 1, -7, 8, -9],
        [2, 8, -6, 5, -4, -7, -8, 9],
        [3, -5, 6, 0, -1, 2, 3, -6]
    ]

    fig, axs = plt.subplots(2, 2)
    imshowChart(axs[0][0], x, y, d1)
    pcolormeshChart(axs[0][1], x, y, d1)
    hinton(axs[1][0], d2)
    axs[1][1].remove()

    plt.show()
