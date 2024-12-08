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


def equationSolving(equation, xl, xr, error=0.0000001):
    if equation(xl) * equation(xr) > 0:
        print("此范围可能无解，或请重新设置解的范围，确保范围内仅有一根")
        return None
    while abs(xr - xl) > error:
        xm = (xl + xr) / 2
        if equation(xl) * equation(xm) < 0:
            xr = xm
        else:
            xl = xm
    result = (xl + xr) / 2
    deviation = equation(result)
    print(f"方程根为{result},偏差为{deviation}")
    return result


# 定义方程
def f(x):
    result = None
    try:
        result = x ** 2 + 1 / x - (10 + math.exp(x))
    except Exception as e:
        print(e, "超出函数定义域")
    return result


def fxChart(ax, equation, xl, xr):
    xs = np.linspace(xl, xr, 100)
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


fig, ax = plt.subplots()
fxChart(ax, f, 0, 1)

equationSolving(f, 0.0001, 0.2)

plt.show()
