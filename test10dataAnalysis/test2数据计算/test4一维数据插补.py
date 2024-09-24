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
import matplotlib.pyplot as plt
import matplotlib
from copy import copy
from lib.zCalculate.lineList import LineUtil, LineList

matplotlib.use('Qt5Agg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


kinds = ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']

dt = LineUtil.createRandomList(100, 100, 250)
dt = LineUtil.replaceRandom(dt, 0.6, 0)
l = LineList(dt)

# 绘制2*3个图
fig,axs = plt.subplots(ncols=3,nrows=2)

for index, kind in enumerate(kinds):
    out = copy(l).interpolate(method=kind,old=0).print().get()
    ax = axs[index // 3, index % 3]
    ax.plot(out, label=kind)
    ax.plot(out, '+')
    ax.plot(dt, 'o')
    # ax.legend()
    ax.set_title(kind)

plt.show()
