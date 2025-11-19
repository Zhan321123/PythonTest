import matplotlib
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
plt.rcParams['axes.unicode_minus'] = False


def nonlinearFit(xs: np.ndarray, ys: np.ndarray, model: callable, p0: list[float] = None):
  # 参数opt，参数协方差矩阵cov
  opt, cov = curve_fit(
    f=model,
    xdata=xs,
    ydata=ys,
    p0=p0  # 初始参数
  )

  y_fit = model(xs, *opt)  # 拟合曲线的y值
  ss_res = np.sum((ys - y_fit) ** 2)  # 残差平方和
  ss_tot = np.sum((ys - np.mean(ys)) ** 2)  # 总平方和
  r_squared = 1 - (ss_res / ss_tot)  # R^2越接近1越好

  # 输出结果
  print(f'参数：{opt}')
  print(f'R^2：{r_squared:.4f}')
  print(f'参数协方差矩阵：{cov}')  # 从协方差矩阵提取标准误差
  return opt


if __name__ == '__main__':
  the_xs = np.array([5,2,1,0.5,0.25,0.1,0.075,])
  the_ys = np.array([2.500856458, 24.32339842, 51.16478246, 75.71085988, 89.31140802, 96.72833162, 99.554642])
  the_ys = np.flipud(the_ys)# 反转
  xSpace = np.linspace(0.075, 5, 100)

  model = lambda x, a, b, c: a * np.arctan(b * x) + c

  opt = nonlinearFit(the_xs, the_ys, model, )

  # 绘图
  plt.figure(figsize=(8, 5))
  plt.scatter(the_xs, the_ys, color='blue', alpha=0.6, label='data')
  plt.plot(xSpace, model(xSpace, *opt), color='red', linewidth=2, label='fit')
  plt.xlabel('sand size')
  plt.xscale('log')
  plt.xticks(the_xs, the_xs)
  plt.ylabel('screening rate')
  plt.grid(alpha=0.3)
  plt.legend()
  plt.show()
