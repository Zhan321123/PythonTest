"""
曲线回归

模拟 y=x^3 回归
"""
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-9, 9, 27, 69, 129, 215, 340, 510, 731, 993]

# 绘制散点图
plt.scatter(x, y, label='Data Points', marker='o')  # 使用'o'标记每个点

# 计算二次回归的系数
coefficients = np.polyfit(x, y, 3)
print("coefficients: ",coefficients)

# 创建二次函数
quad_func = np.poly1d(coefficients)
print("quad_func: \n",quad_func)

# 计算二次回归线上对应x值的y值
quad_regression_line_y = quad_func(x)
print("quad_regression_line_y: ",quad_regression_line_y)

# 绘制二次回归线
plt.plot(x, quad_regression_line_y, color='green', label='Quadratic Regression Line')

# 更新图例
plt.legend()

# 显示图形
plt.show()
