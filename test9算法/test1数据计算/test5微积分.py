"""
微分

定积分 scipy库
    result结果, error误差 = scipy.integrate.quad(function函数, 下限, 上限)

"""
import math


def integral(function: callable, xl: float, xr: float, step: float = 1e-5) -> float:
  """
  定积分 E = ∑f(x)dx
  :param function: fx
  :param xl:
  :param xr:
  :param step: 步长，dx
  :return:
  """
  result = 0
  for i in range(int((xr - xl) / step)):
    result += function(xl + i * step) * step
  return result


if __name__ == '__main__':
  f1 = lambda x: math.e ** (-x ** 2 / 2) / math.sqrt(2 * math.pi)
  print(integral(f1, -1, 1))
  print(integral(f1, -2, 2))
  print(integral(f1, -3, 3))
