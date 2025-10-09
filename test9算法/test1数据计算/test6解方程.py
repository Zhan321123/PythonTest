"""
1. y = f(x)
2. f(x, y) = 0
3. int^n_y(f(x))dx = 0
"""
import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


def eqSolving(equation: callable, xl: float, xr: float, error=1e-7) -> float:
  """
  二分法解方程零点

  :param equation: f(x)=0 方程
  :param xl: [x,
  :param xr: x,]
  :param error: 误差限制
  :return: 解
  """
  equation = _tryFx(equation)
  if equation(xl) * equation(xr) > 0:
    raise Exception("此范围可能无解，或请重新设置解的范围，确保范围内仅有一根")
  try:
    while abs(xr - xl) > error:
      xm = (xl + xr) / 2
      if equation(xl) * equation(xm) < 0:
        xr = xm
      else:
        xl = xm
  except Exception as e:
    raise Exception(f"函数在[{xl},{xr}]范围无定义域,错因：{e}")
  result = (xl + xr) / 2
  deviation = equation(result)
  print(f"方程{equation.__name__}根为{result},偏差为{deviation}")
  return result


def _tryFx(equation: callable) -> callable:
  def fx(*args, **kwargs):
    try:
      return equation(*args, **kwargs)
    except Exception as e:
      raise Exception(e, "超出函数定义域")

  return fx


def fxChart(ax: plt.Axes, equation: callable, xl: float, xr: float):
  """
  绘制方程曲线
  :param ax:
  :param equation: f(x)=0
  :param xl:
  :param xr:
  :return:
  """
  xs = np.linspace(xl, xr, 100)
  equation = _tryFx(equation)
  ys = list(equation(i) for i in xs)
  ps = []
  for index, i in enumerate(ys):
    if i is None:
      continue
    else:
      ps.append((xs[index], i))
  xs, ys = zip(*ps)
  ax.plot(xs, ys, '-', color='red', label='f(x)')
  ax.plot((min(xs), max(xs)), (0, 0), '-')


if __name__ == '__main__':
  f = lambda x: 4 * np.pi ** 2 / 9 - 9.8 * x * np.tanh(x * 13.94)

  fig, ax = plt.subplots()
  fxChart(ax, f, 0, 1)
  # plt.show()
  eqSolving(f, 0.0001, 100)
