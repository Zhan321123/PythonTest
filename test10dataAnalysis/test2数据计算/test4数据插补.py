"""
单序列数据插补
kind=
    zero:
    slinear: 线性插值
    quadratic: 二次插值
    cubic: 三次插值
    next:
    nearest: 最近插值
"""
from typing import Sequence
import numpy as np
from scipy.interpolate import interp1d

kinds = ['zero', 'slinear', 'quadratic', 'cubic', 'next', 'nearest']


def interpolate0(dt: Sequence[float], kind: str):
    npData = np.array(dt)
    x = np.nonzero(npData)[0]
    y = npData[x]
    f = interp1d(x, y, kind=kind, bounds_error=False, fill_value=(y[0], y[-1]))

    x = np.arange(len(npData))
    out = f(x).tolist()
    return out


dt = [0, 0, 55, 0, 77, 99, 33, 0, 0, 4, 0, 100, 0, 0, 0]

for i in kinds:
    print(interpolate0(dt, i), i)
