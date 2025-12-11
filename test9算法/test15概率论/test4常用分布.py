import random
from typing import Union

import matplotlib
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy.stats import binom

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


class Random:
  def __call__(self):
    return self.next(random.random())

  def next(self, x: Union[float, np.ndarray]):
    """F^-1(x)"""
    return x

  def fx(self, x: Union[float, np.ndarray]):
    """概率密度函数"""
    return 1

  def Fx(self, x: Union[float, np.ndarray]):
    """累积分布函数"""
    return x

  def getDomain(self):
    """定义域"""
    return 0, 1


class Uniform(Random):
  def __init__(self, a=0, b=1):
    if a > b:
      raise ValueError("a must be less than b")
    self.a = a
    self.b = b

  def next(self, x):
    return self.a + (self.b - self.a) * x

  def fx(self, x):
    return 1 / (self.b - self.a)

  def Fx(self, x):
    return (x - self.a) / (self.b - self.a)

  def getDomain(self):
    return self.a, self.b


class Normal(Random):
  def __init__(self, mu=0, sigma=1):
    if sigma <= 0:
      raise ValueError("sigma must be positive")
    self.mu = mu
    self.sigma = sigma

  def next(self, x):
    # return self.mu + self.sigma * np.sqrt(-2 * np.log(random.random())) * np.cos(2 * np.pi * random.random())
    return self.mu + np.sqrt(2) * self.sigma * np.atanh(2 * x - 1)

  def fx(self, x):
    return np.exp(-(x - self.mu) ** 2 / (2 * self.sigma ** 2)) / (np.sqrt(2 * np.pi) * self.sigma)

  def Fx(self, x):
    return 0.5 * (1 + np.tanh((x - self.mu) / (self.sigma * np.sqrt(2))))

  def getDomain(self):
    return -np.inf, np.inf


class TwoDot(Random):
  def __init__(self, a=0, b=1):
    if a > b:
      raise ValueError("a must be less than b")
    self.a = a
    self.b = b

  def next(self, x):
    return self.a if x < 0.5 else self.b

  def fx(self, x):
    return 0.5

  def Fx(self, x):
    return 0 if x < self.a else 0.5 if x < self.b else 1

  def getDomain(self):
    return self.a, self.b


class Binomial(Random):
  def __init__(self, n, p):
    if p < 0 or p > 1:
      raise ValueError("p must be between 0 and 1")
    self.n = n
    self.p = p

  def next(self, x):
    return sum(np.random.random(self.n) < self.p)

  def fx(self, x):
    x = np.floor(x)
    return scipy.special.comb(self.n, x) * (1 - self.p) ** (self.n - x) * self.p ** x

  def Fx(self, x):
    x_arr = np.asarray(x, dtype=float)
    k = np.floor(x_arr).astype(int)
    cdf = binom.cdf(k, n=self.n, p=self.p)
    return cdf.item() if isinstance(x, float) else cdf

  def getDomain(self):
    return 0, self.n


class Bernoulli(Binomial):
  def __init__(self, p):
    super().__init__(1, p)


class Poisson(Random):
  def __init__(self, lamb):
    if lamb <= 0:
      raise ValueError("l must be positive")
    self.lamb = lamb

  def next(self, x):
    return np.random.poisson(self.lamb)

  def fx(self, x):
    x = np.floor(x)
    return self.lamb ** x * np.exp(-self.lamb) / scipy.special.factorial(x)

  def Fx(self, x):
    x = np.floor(x)
    return 1 - np.exp(-self.lamb) ** (x + 1)

  def getDomain(self):
    return 0, np.inf


class Geometric(Random):
  def __init__(self, p):
    if p < 0 or p > 1:
      raise ValueError("p must be between 0 and 1")
    self.p = p

  def next(self, x):
    return np.random.geometric(self.p)

  def fx(self, x):
    x = np.floor(x)
    return self.p * (1 - self.p) ** x

  def Fx(self, x):
    x = np.floor(x)
    return 1 - (1 - self.p) ** (x + 1)

  def getDomain(self):
    return 0, np.inf


if __name__ == '__main__':
  fig, axs = plt.subplots(3, 2)
  axs = axs.flatten()
  for i, u in enumerate([Uniform(), Normal(), Binomial(5, 0.3), Poisson(1), Geometric(0.3)]):
    left, right = u.getDomain()
    left = max(left, -5) if np.isinf(left) else left
    right = min(right, 5) if np.isinf(right) else right
    l1 = np.array([u() for i in range(10000)])
    l2 = np.array(u.Fx(np.linspace(left, right, 10000)))
    l3 = np.array([u.fx(i) for i in np.linspace(left, right, 10000)])
    axs[i].hist(l1, bins=100, density=True, label="hist")
    axs[i].plot(np.linspace(left, right, 10000), l2, label="Fx")
    axs[i].plot(np.linspace(left, right, 10000), l3, label="fx")
    axs[i].set_title(u.__class__.__name__)
    axs[i].legend()
    print(u.__class__.__name__, np.mean(l1), np.std(l1))
  plt.tight_layout()
  plt.show()
