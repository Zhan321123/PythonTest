"""
Hinton图
官方链接介绍：
    https://matplotlib.org/stable/gallery/specialty_plots/hinton_demo.html#sphx-glr-gallery-specialty-plots-hinton-demo-py

"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def hinton(matrix, max_weight=None, ax=None):
    """Draw Hinton diagram for visualizing a weight matrix."""
    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2 ** np.ceil(np.log2(np.abs(matrix).max()))

    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x, y), w in np.ndenumerate(matrix):
        color = 'white' if w > 0 else 'black'
        size = np.sqrt(abs(w) / max_weight)
        rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()


if __name__ == '__main__':
    data = [
        [2, -5, 1, 7, -9, 2, -7, 3],
        [4, 1, 6, 8, 1, -3, -6, -2],
        [3, -2, 7, -9, -3, 7, 6, 1],
        [3, 5, 1, -7, 2, 5, -4, -1],
        [3, 7, 1, -7, 1, -7, 8, -9]
    ]
    hinton(data)
    plt.show()
