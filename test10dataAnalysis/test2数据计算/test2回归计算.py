"""
回归计算
    一元线型回归
    TODO 多元线型回归
    TODO 一元非线性回归

"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.linear_model import LinearRegression

matplotlib.use('Qt5Agg')
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

data = {
    'A': {1: 18, 2: 20, 3: 34, 4: 45, 5: 52, 6: 65, 7: 78, 8: 89, 9: 100, 10: 109, 11: 115, 12: 120, 13: 130, 14: 138,
          15: 142, 16: 149, 17: 156, 18: 159, 19: 160, 20: 161, 21: 161, 22: 162, 23: 162, 24: 162, },
    'B': {1: 23, 2: 39, 3: 45, 4: 56, 5: 67, 6: 78, 7: 89, 8: 100, 9: 111, 10: 122, 11: 133, 12: 144, 13: 155, 14: 166,
          15: 170, 16: 173, 17: 178, 18: 182, 19: 192, 20: 193, 21: 193, 22: 194, 23: 194, 24: 194}
}

def lineFitting(x: Sequence, y: Sequence):
    """
    一元线型回归
    """
    if len(x) != len(y):
        print('x,y长度不一致')
        return None
    model = LinearRegression()
    xss = tuple(map(lambda x: (x,), x))
    model.fit(xss, y)
    r = model.score(xss, y)
    k = model.coef_[0]
    b = model.intercept_
    return k, b, r

aAge = list(data['A'].keys())
aHigh =list(data['A'].values())
akbr = lineFitting(aAge, aHigh)
print(akbr)

bAge = np.array(list(data['B'].keys()))
bHigh = np.array(list(data['B'].values()))
bkbr = lineFitting(bAge, bHigh)
print(bkbr)

plt.figure()

plt.plot(aAge, aHigh, 'o-', label='A points')
plt.plot(bAge, bHigh, 'o-', label='B points')
plt.plot([aAge[0], aAge[-1]], [akbr[0] * aAge[0] + akbr[1], akbr[0] * aAge[-1] + akbr[1]], label='A line')
plt.plot([bAge[0], bAge[-1]], [bkbr[0] * bAge[0] + bkbr[1], bkbr[0] * bAge[-1] + bkbr[1]], label='B line')

plt.legend()
# plt.show()
