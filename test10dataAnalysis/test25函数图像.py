"""
函数图像

生成y=sin(x)/x的函数图像

"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# 定义函数
def func(x):
    return math.sin(x) / x


# 设置x轴的取值范围
x_min = -10
x_max = 10
num_points = 100  # 控制图像平滑度，数值越大，图像越平滑
x_values = np.linspace(x_min, x_max, num=num_points)

# 计算对应的y值
y_values = [func(x) for x in x_values]

# 创建图像
plt.figure(figsize=(10, 6))  # 设置图像大小
plt.plot(x_values, y_values, label=r'$y = \frac{sin(x)}{x}$')  # 绘制函数图像

# 设置x轴和y轴标签
plt.xlabel('x')
plt.ylabel('y')

# 添加图例
plt.legend()

# 显示图像
plt.grid(True)  # 显示网格
plt.show()
