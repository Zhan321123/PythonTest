"""
回归计算
    一元线型回归
    TODO 多元线型回归
    TODO 一元非线性回归

"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression

matplotlib.use('Qt5Agg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def lineFitting(x: Sequence, y: Sequence):
    """一元线型回归"""
    model = LinearRegression()
    xss = tuple(map(lambda x: (x,), x))
    model.fit(xss, y)
    r = model.score(xss, y)
    k = model.coef_[0]
    b = model.intercept_
    print('斜率：', k, '截距：', b, 'score:', r)


def linear(ax, xs, ys):
    """点图、并绘制一元线型回归线"""
    m, b = np.polyfit(xs, ys, 1)
    regression_y = list(m * i + b for i in xs)  # 生成回归线
    ax.scatter(xs, ys, label='Data Points', marker='o')  # 绘制散点图
    ax.plot(xs, regression_y, '-', color='red', label='Regression Line')  # 绘制回归线
    ax.legend()


if __name__ == '__main__':
    x = list(range(1, 23))
    y1 = [18, 20, 34, 45, 52, 65, 78, 89, 100, 109, 115, 120, 130, 138, 142, 149, 156, 159, 160, 161, 161, 162, ]

    fig, axs = plt.subplots(1, 2)
    lineFitting(x, y1)
    linear(axs[0], x, y1)

    plt.show()
