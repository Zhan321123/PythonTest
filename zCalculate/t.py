import numpy as np
from scipy.stats import gamma


def m(d, p):
    shape, loc, scale = gamma.fit(d, floc=0)  # 估计伽玛分布的参数
    dist = gamma(shape, loc=loc, scale=scale)  # 创建伽玛分布对象
    return dist.ppf(p)  # 计算p保证率的最大洪水高度


flood = [123, 234, 324, 345, 514, 364, 235, 56, 153, 362, 135]
print(m(flood, 0.9))
