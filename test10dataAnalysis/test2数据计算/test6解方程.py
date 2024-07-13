"""
参考文章:https://blog.csdn.net/nejssd/article/details/104901610

使用的库
scipy


sympy

TODO 未完成
"""
import numpy as np
from scipy.optimize import root
import math


# 定义方程
def equation(vars):
    x = vars[0]
    return [x ** 2 + 1 / x - (10 + math.exp(x))]


# 初始猜测值，好的初始值可以帮助更快找到解
initial_guess = [10]

# 使用scipy的root函数求解
solution = root(equation, initial_guess)

# 输出解
if solution.success:
    print('success')
    print("方程的解为: ", solution.x)
    print(equation(solution.x))
else:
    print("未能找到解，可能的原因包括无解、初始猜测不合适或算法限制。")
