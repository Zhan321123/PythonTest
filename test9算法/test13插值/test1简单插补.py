"""
单序列数据插补

    scipy.interp1d(
        indexes|x, 自变量列表
        data|y, 因变量列表
        kind = "slinear", 插值方法
        copy = True, 插值后是否复制输入的数据
        bounds_error = True, 超出数据范围是否抛出异常
        fill_value = None, 超出数据范围时填充的值，可以用(data[0], data[-1])
    )
    kind=
        zero: 向前插值
        next: 向后插值
        nearest: 临近插值
        slinear: 线性插值
        quadratic: 二次插值
        cubic: 三次插值

"""
import random
from typing import Literal

import matplotlib.pyplot as plt
import matplotlib
from copy import copy

import numpy as np
from scipy.interpolate import interp1d

matplotlib.use('TkAgg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def interpolate(seq: np.ndarray,
                method: Literal["zero", "next", "nearest", "slinear", "quadratic", "cubic"] = 'slinear',
                old=np.nan, lowest=None):
    """
    插值，先用linear方法插值中间内容，然后用临近法插值两端
    指定old为缺失值，默认为np.nan，会进行替换和插补
    lowest为最小值，如果插补后含有小于lowest的值，会先清除，然后linear插补
    如果原本有的值就小于lowest，也会替换和插补

    :param seq: 待插补的序列
    :param method: 插值方法
    :param old: 被当作空缺的值
    :param lowest: 最小值，小于该值的值会被清除，然后插补
    :return: 插补后的序列
    """
    seq = np.array(seq)
    if old is not np.nan:
        seq = [np.nan if i == old else i for i in seq]
    indexes = [not i for i in [(i is np.nan) | (i == np.nan) for i in seq]]
    x = [i for i, j in enumerate(indexes) if j]

    if len(x) == 0:
        print('no value need to interpolate')
        return seq
    y = list([ii for index, ii in enumerate(seq) if indexes[index]])
    f = interp1d(x, y, kind=method, bounds_error=False, fill_value=(y[0], y[-1]))
    x = list(range(len(seq)))
    seq = f(x).tolist()

    if lowest is not None:
        seq[[i for i, j in enumerate([not i for i in [i >= lowest for i in seq]]) if j]] = np.nan
        seq = interpolate(seq, method=method, old=np.nan, lowest=lowest)

    return seq


dt = list([random.random() * (250 - 100) + 100 for _ in range(100)])
l = [0 if random.random() < 0.6 else i for i in dt]

# 绘制2*3个图
fig, axs = plt.subplots(ncols=3, nrows=2)

for index, kind in enumerate(["zero", "next", "nearest", "slinear", "quadratic", "cubic"]):
    out = interpolate(copy(l), method=kind, old=0)
    ax = axs[index // 3, index % 3]
    ax.plot(out, label=kind)
    ax.plot(out, '+')
    ax.plot(dt, 'o')
    # ax.legend()
    ax.set_title(kind)

plt.show()
