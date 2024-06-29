import numpy as np
from scipy.optimize import root
import math


def e(h):
    b = 71.0838
    Q = 448.6
    A = b * h
    X = b + 2 * h
    R = A / X
    CR12 = 1 / 0.014 * R ** (3 / 2)
    v1 = Q / 75 / 1.53977
    v2 = Q / A
    J1 = v1 ** 2 / 92.724
    J2 = v2 ** 2 / CR12 ** 2
    Jba = (J1 + J2) / 2
    Es = 1.53977 + v1 ** 2 / 2 / 9.8 - h - v2 ** 2 / 2 / 9.8
    detaS = Es / (1 / 5 - Jba)
    return detaS - 89 / 2


# initial_guess = [1.5]
#
# # 使用scipy的root函数求解
# solution = root(e, initial_guess)
#
# if solution.success:
#     print("方程的解为: ", solution.x)
#     print(e(solution.x))
# else:
#     print("未能找到解，可能的原因包括无解、初始猜测不合适或算法限制。")

# i = 0.0001
# x = 0.0001
# while True:
#     y = e(x)
#     if -2 < y < 2:
#         print(x,y)
#     x += i
#     if x > 100:
#         break
