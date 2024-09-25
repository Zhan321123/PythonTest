import numpy as np

from lib.zCalculate.importBase import importMatplotlib
from lib.zCalculate.lineList import LineList, LineUtil
from scipy.interpolate import splprep, splev

sandRange = [0.5, 1, 2, 5, 10, 20, 50, 80, 120]
sand1 = [6, 26.5, 11.5, 11, 31, 8.7, 15.5, 30]
sand2 = [18, 24, 7, 5, 13, 15, 2, 7.9]
sand3 = [10, 11, 9, 9, 11, 13.3, 9, 10]

p1, p2, p3 = [], [], []
for index, i in enumerate(sandRange):
    x = i
    p1.append((x, sum(sand1[:index]) / sum(sand1)))
    p2.append((x, sum(sand2[:index]) / sum(sand2)))
    p3.append((x, sum(sand3[:index]) / sum(sand3)))

def fit(x,y):
    for i in range(len(x)):
        print(x[i],',',y[i])
    tck, u = splprep([x, y], s=0)
    sx, sy = splev(u, tck)
    return sx, sy
# def f1(x): return -6.37E-08 * x ** 4 + 1.7E-05 * x ** 3 - 0.0015 * x ** 2 + 0.0529 * x + 0.0349
# def f2(x): return -6.50E-08 * x ** 4 + 1.74E-05 * x ** 3 - 1.57E-03 * x ** 2 + 5.70E-02 * x + 1.70E-01
# def f3(x): return -6.10E-08 * x ** 4 + 1.60E-05 * x ** 3 - 1.40E-03 * x ** 2 + 5.12E-02 * x + 7.90E-02


# n=1
# def fit(x, y):
#     xx = LineUtil.equidistantListByNum(min(x), max(x), 100)
#     if n == 1:
#         yy = list(f1(i) for i in xx)
#     elif n == 2:
#         yy = list(f2(i) for i in xx)
#     elif n == 3:
#         yy = list(f3(i) for i in xx)
#     n += 1
#     return xx, yy


# def fit(x, y):
#     print(x,y)
#     xx, yy = [], []
#     accuracy = 100
#     x = list(int(i*accuracy) for i in x)
#     for i in range(min(x), max(x)+1):
#         xx.append(i / accuracy)
#         if i not in x:
#             yy.append(np.nan)
#         else:
#             yy.append(y[x.index(i)])
#     yy = LineList(yy).interpolate(method="quadratic",old=np.nan)
#     return xx, yy

# def fit(x,y):
#     degree = 4
#     coefficients = np.polyfit(x, y, degree)
#     polynomial = np.poly1d(coefficients)
#     trend_x = np.linspace(min(x), max(x), 100)
#     trend_y = polynomial(trend_x)
#     return trend_x, trend_y

plt = importMatplotlib()
# plt.figure(figsize=(16, 9))
plt.plot(*fit(*list(zip(*p1))), label='①')
plt.plot(*fit(*list(zip(*p2))), label='②')
plt.plot(*fit(*list(zip(*p3))), label='③')
plt.ylim(0, 1)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1], [0, 20, 40, 60, 80, 100])
plt.xticks(sandRange[1:], sandRange[1:])
plt.xlim(sandRange[-1], 0)
# plt.gca().invert_xaxis()
plt.xlabel('$D(mm)$')
plt.ylabel('$p($%$)$')
plt.legend()
plt.grid()
# plt.savefig("test.png", dpi=600)
# plt.show()
