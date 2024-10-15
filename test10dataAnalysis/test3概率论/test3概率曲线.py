"""
正态分布
    p = norm.pdf(x, mu, sigma)
    mu平均值，sigma标准差
    定义域 (-∞, +∞)
伽玛分布
    p = gamma.pdf(x, alpha, beta)
    alpha形状参数，beta尺度参数
    定义域 (0, +∞)
t-分布
    p = t.pdf(x, df)
    df自由度
    定义域 (-∞, +∞)
X^2分布
    p = chi2.pdf(x, df)
    df自由度
    定义域 (0, +∞)


p = norm.pdf() 概率密度函数
p = norm.cdf() 累积分布函数
x = norm.ppf() 累积分布函数的反函数


标准正态分布函数
    mu=0, sigma=1
皮尔逊Ⅲ型曲线 | PⅢ曲线
    alpha=(Cs**2/2+1)**2, beta=1/(Cv*sqrt(alpha)
    Cv =

"""
from typing import Sequence

import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm, gamma, t, skew

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')

print(norm.pdf(0, 0, 1))
print(norm.pdf(0))
# f(0) = 1/sqrt(2π)
print(norm.pdf(0) == 1 / np.sqrt(2 * np.pi))

print("---------3σ区间-----------")
print(norm.cdf(3) - norm.cdf(-3))
print(norm.cdf(2) - norm.cdf(-2))
print(norm.cdf(1) - norm.cdf(-1))

# 累积分布函数的反函数
print(norm.ppf(0.5))
