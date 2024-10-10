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

import numpy as np
from scipy.stats import norm, gamma, t, skew

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

print("---------------PⅢ曲线在水文学中的使用案例----------------")
"""有100年该河流的水位（年平均水位），求20年一遇的洪水水位、10年一遇的枯水水位"""
n = 100
d = np.random.rand(n) * 10  # 100年该河流的年平均水位

cv = np.std(d) / d.mean()
cs = skew(d)
alpha = 4 / cs ** 2
beta = 2 / d.mean() / cv / cs
a0 = d.mean() * (1 - 2 * cv / cs)

h20 = gamma.pdf(0.05, alpha, beta, a0)
print(h20)
