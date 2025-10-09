"""
回归计算
    一元线型回归
    多元线型回归
"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

from test1python基础.test1.test35类属性 import printObject, printAttribute

matplotlib.use('TkAgg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def lineFitting(xs: Sequence, ys: Sequence):
  """
  一元线型回归

  :param xs: 自变量
  :param ys: 因变量
  :return:
  """
  model = LinearRegression()
  xss = tuple(map(lambda x: (x,), xs))
  model.fit(xss, ys)
  r2 = model.score(xss, ys)
  k = model.coef_[0]
  b = model.intercept_
  print('斜率 k=', k, '截距 b=', b, '方差 r^2=', r2)


def linear(ax: plt.Axes, xs: np.ndarray, ys: np.ndarray, drawEllipse=False, nStd=2):
  """
  点图、并绘制一元线型回归线
  :param ax:
  :param xs:
  :param ys:
  :param drawEllipse: 是否绘制置信椭圆
  :param nStd: 置信椭圆的置信度
  :return:
  """
  m, b = np.polyfit(xs, ys, 1)
  regression_y = list(m * i + b for i in xs)  # 生成回归线
  ax.scatter(xs, ys, label='Data Points', marker='o', color='green')  # 绘制散点图
  ax.plot(xs, regression_y, '-', label='Regression Line', color='purple')  # 绘制回归线
  if drawEllipse:
    cov = np.cov(xs, ys)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])

    xR = np.sqrt(1 + pearson)
    yR = np.sqrt(1 - pearson)
    xScale = np.sqrt(cov[0, 0]) * nStd
    yScale = np.sqrt(cov[1, 1]) * nStd

    ellipse = Ellipse((0, 0), width=xR * 2, height=yR * 2, alpha=0.5, label='Confidence Ellipse')
    transf = transforms.Affine2D().rotate_deg(45).scale(xScale, yScale).translate(np.mean(xs), np.mean(ys))
    ellipse.set_transform(transf + ax.transData)
    ax.add_patch(ellipse)
  ax.grid()
  ax.set_title('univariate linear regression')
  ax.legend()


def mulLineFitting(xss: Sequence, ys: Sequence):
  """
  多元线型回归

  :param xss: [
      [x1, x2, x3, ..., xn],
      ...
    ]
  :param ys: [y1, y2, y3, ..., yn]
  :return:
  """
  xss = np.array(xss)
  ys = np.array(ys)
  model = LinearRegression()
  model.fit(xss, ys)
  r2 = model.score(xss, ys)
  ks = model.coef_
  b = model.intercept_
  printAttribute(model)
  print('斜率 ks=', ks, '截距 b=', b, '方差 r^2=', r2)


if __name__ == '__main__':
  # x = list(range(0, 23))
  # y1 = np.random.rand(23)
  # y1.sort()
  #
  fig, axs = plt.subplots(1, 1)
  # axs = axs.flatten()
  x = np.arange(2000, 2010)
  y1 = np.array([62, 73, 82, 88, 100, 109, 114, 122, 132, 144])
  lineFitting(x, y1)
  linear(axs, x, y1, drawEllipse=True)

  # plt.show()

  x = [
    [1, 3, 5, 8, 9],
    [-2, -4, -6, -9, -12],
    [100, 200, 300, 400, 500]
  ]
  x = np.array(x).transpose()
  y = [20, 40, 50, 70, 80]
  mulLineFitting(x, y)
