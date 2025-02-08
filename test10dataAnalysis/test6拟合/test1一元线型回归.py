"""
回归计算
    一元线型回归
"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

matplotlib.use('TkAgg')
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


def ellipse(ax: plt.Axes, xs, ys, nStd=3):
    """绘制置信椭圆"""
    ax.scatter(xs, ys,color='none', edgecolor='black')

    cov = np.cov(xs, ys)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])

    xR = np.sqrt(1 + pearson)
    yR = np.sqrt(1 - pearson)
    xScale = np.sqrt(cov[0, 0]) * nStd
    yScale = np.sqrt(cov[1, 1]) * nStd
    xMean = np.mean(xs)
    yMean = np.mean(ys)

    ellipse = Ellipse((0, 0), width=xR * 2, height=yR * 2, alpha=0.5)
    transf = transforms.Affine2D().rotate_deg(45).scale(xScale, yScale).translate(xMean, yMean)
    ellipse.set_transform(transf + ax.transData)
    ax.add_patch(ellipse)
    ax.set_title('Confidence Ellipse')


if __name__ == '__main__':
    x = list(range(0, 23))
    y1 = np.random.rand(23)
    y1.sort()

    fig, axs = plt.subplots(1, 2)
    axs = axs.flatten()
    lineFitting(x, y1)
    linear(axs[0], x, y1)
    ellipse(axs[1], x, y1)

    plt.show()
