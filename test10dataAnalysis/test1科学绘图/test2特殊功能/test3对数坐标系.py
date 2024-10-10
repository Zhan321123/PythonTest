"""
对数坐标系
半对数坐标系

ax.set_xscale("log")将x轴设置为对数坐标
ax.set_yscale("log")
"""
from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def line(ax: plt.Axes, xs, ys):
    ax.plot(xs, ys)
    ax.set_xscale("log")
    ax.set_xticks([1, 10, 100, 1000, 10000, 100000], [0, 1, 2, 3, 4, 5])
    ax.set_xlabel("x (×$10^n$)")
    ax.grid()

if __name__ == '__main__':
    fig, ax = plt.subplots()
    line(ax, [1, 20, 300, 40000, 500000], [1, 2, 3, 4, 5])
    plt.show()