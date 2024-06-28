"""
矩阵相关计算
"""
import numpy as np

a = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
b = np.mat([[9, 8, 7], [6, 5, 4], [3, 2, 0]])
print(a)

print('-----------------------------')
print(a.shape)  # 获取矩阵的形状

print('-----------------------------')
print(a.T)  # 矩阵转置
print(np.linalg.inv(a))  # 矩阵求逆
# 伴随矩阵

print('-----------------------------')
print(np.linalg.det(a))  # 矩阵行列式的值
print(np.linalg.eig(a))


print('-----------------------------')
print(a * b)  # 矩阵相乘
print(a - b)  # 矩阵相减
print(a + b)  # 矩阵相加
print(a * 10)  # 数乘矩阵
