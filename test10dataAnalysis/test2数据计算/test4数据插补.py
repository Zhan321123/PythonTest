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
from typing import Sequence
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Qt5Agg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


kinds = ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']


def interpolate0(dt: Sequence[float], kind: str):
    npData = np.array(dt)
    x = np.nonzero(npData)[0]
    y = npData[x]
    f = interp1d(x, y, kind=kind, bounds_error=False, fill_value=(y[0], y[-1]))

    x = np.arange(len(npData))
    out = f(x).tolist()
    # print(kind, out)
    return out

length = 60
dt = list(np.random.rand(length)*100+50)
for i in range(length):
    if random.random()<0.5:
        dt[i] = 0
print(dt)

# 绘制2*3个图
fig,axs = plt.subplots(ncols=3,nrows=2)

for index, kind in enumerate(kinds):
    out = interpolate0(dt, kind)
    ax = axs[index // 3, index % 3]
    ax.plot(out, label=kind)
    ax.plot(out, '+')
    ax.plot(dt, 'o')
    # ax.legend()
    ax.set_title(kind)

plt.show()
