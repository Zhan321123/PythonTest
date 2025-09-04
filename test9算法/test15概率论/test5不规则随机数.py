"""
"不规则"随机数

生成原理:
有且仅有 random() : F_1(x)=x
概率密度函数 f(x) [xl<=x<xr, Σf=1]
累积分布函数 F(x)=Σf(x) [xl<=x<xr, F(xl)=0, F(xr)=1]
累积分布反函数 F_1(x) [0<=x<1, xl<=F_1(x)<xr]

举例: f(x)=2x [0<=x<1]的随机数
1. 不定积分 F(x)=x^2
2. 求反 F_1(x)=sqrt(x)
3. 构造
  def 2x():
    return sqrt(random())

"""
import math
import random
from typing import Sequence
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def boxChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
  bplot = ax.boxplot(yss, notch=True, vert=True, patch_artist=True, tick_labels=xs)
  xs = np.arange(len(xs))
  for patch, color in zip(bplot['boxes'], matplotlib.colormaps["rainbow"](xs / max(xs))):
    patch.set_facecolor(color)
  ax.set_title('Notched box plot')


def histsChart(ax: plt.Axes, n: int, yss: Sequence):
  for ys in yss:
    ax.hist(ys, bins=n, histtype='step')


def violinChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]) -> None:
  part = ax.violinplot(yss, showmeans=False, showmedians=True)
  cs = matplotlib.colormaps["rainbow"](np.arange(len(xs)) / max(np.arange(len(xs))))
  for index, pc in enumerate(part['bodies']):
    pc.set_facecolor(cs[index])
    pc.set_edgecolor('black')
    pc.set_alpha(0.6)
  ax.set_xticks(range(1, len(xs) + 1), xs)
  ax.set_title('Violin plot')


def cumulativeDistribution(ax: plt.Axes, ys: Sequence):
  """累积分布曲线"""
  ax.hist(ys, bins=20, density=True, histtype="step", label="histogram")
  ax.ecdf(ys, label='CDF')  # 累积曲线
  ax.hist(ys, bins=20,  # 直方图的分段数
    density=True,  # 是否显示频数
    histtype="step",  # 直方图类型
    cumulative=True,  # 累积曲线
    label="cumulative histogram")
  ax.ecdf(ys, complementary=True, label='CCDF')  # 互补累积曲线
  ax.hist(ys, bins=20, density=True, histtype="step", cumulative=-1, label="Reversed cumulative histogram")
  ax.legend(framealpha=0.2)


if __name__ == '__main__':
  fig, axs = plt.subplots(1, 3)
  size = lambda define, n: np.array([define() for _ in range(n)])

  # dr1 = lambda: random.random() ** (1 / 2)
  # dr2 = lambda: math.acos(1 - 2 * random.random())
  # dr3 = lambda: math.e**random.random()

  dr1 = lambda: random.random() * random.random()
  dr2 = lambda: random.random() + random.random()
  dr3 = lambda: random.random()

  r1 = size(dr1, 20000)
  r2 = size(dr2, 20000)
  r3 = size(dr3, 20000)

  axs[0].hist(r1, bins=20, histtype='step')
  axs[1].hist(r2, bins=20, histtype='step')
  axs[2].hist(r3, bins=20, histtype='step')
  plt.show()
