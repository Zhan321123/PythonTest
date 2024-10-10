"""
置信图

二维数据的置信椭圆
    椭圆长轴方向决定正相关还是负相关
    椭圆偏心率决定相关性，越“扁”线型相关性越强，越“圆”线性相关性越弱
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 椭圆参数
def ellipse(x, y, ax: plt.Axes, nStd=3):
    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])

    xR = np.sqrt(1 + pearson)
    yR = np.sqrt(1 - pearson)
    xScale = np.sqrt(cov[0, 0]) * nStd
    yScale = np.sqrt(cov[1, 1]) * nStd
    xMean = np.mean(x)
    yMean = np.mean(y)

    ellipse = Ellipse((0, 0), width=xR * 2, height=yR * 2, alpha=0.5)
    transf = transforms.Affine2D().rotate_deg(45).scale(xScale, yScale).translate(xMean, yMean)
    ellipse.set_transform(transf + ax.transData)
    ax.add_patch(ellipse)


if __name__ == '__main__':
    xs, ys = np.random.randn(1000, 2).T
    ys[xs > 0] = ys[xs > 0] + np.random.rand(1)
    ys = ys * 0.1

    fig, ax = plt.subplots()
    ax.scatter(xs, ys)
    ellipse(xs, ys, ax)
    plt.show()
