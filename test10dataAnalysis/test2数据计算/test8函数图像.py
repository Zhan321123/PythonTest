"""
画出图像
"""
import math

import matplotlib.pyplot as plt
import matplotlib
from lib import zCalculate as ll

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def functionGraph(f, limit: tuple[float, float], fineness=100):
    """
    画出函数图像

    :param f: 函数def
    :param limit: 上下限
    :param fineness: 点数，点越多曲线更平滑
    """
    x = ll.LineUtil.equidistantListByNum(limit[0], limit[1], fineness)
    print(x)
    y = [f(i) for i in x]
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.title(f'Graph of {f.__doc__} from {limit[0]} to {limit[1]}')
    plt.xlabel('x')  # x轴标签
    plt.ylabel('y')  # y轴标签
    plt.legend()  # 显示图例
    plt.grid(True)  # 显示网格
    plt.axhline(0, color='black', lw=0.5)  # 添加水平x轴（y=0）
    plt.axvline(0, color='black', lw=0.5)  # 添加垂直y轴（x=0）
    plt.show()  # 显示图像


def func1(x):
    """e^x/x"""
    return math.log(x) / x


if __name__ == '__main__':
    functionGraph(func1, (0.1, 3))
