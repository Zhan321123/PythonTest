"""
矩阵相关计算

TODO 未完成
"""
import numpy as np

a = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
b = np.mat([[9, 8, 7], [6, 5, 4], [3, 2, 0]])
print(a)

print('--------------矩阵基本属性---------------')
print(a.shape)  # 获取矩阵的形状

print('---------------矩阵到矩阵--------------')
print(a.T)  # 矩阵转置
print(np.linalg.inv(a))  # 矩阵求逆
# 伴随矩阵

print('--------------矩阵到数---------------')
print(np.linalg.det(a))  # 矩阵行列式的值
print(np.linalg.eig(a))  # 矩阵特征值和特征向量
print(np.linalg.solve(a, b))  # 矩阵求解
print(np.linalg.norm(a))  # 矩阵范数
print(np.linalg.eigvals(a))  # 矩阵特征值


print('---------------矩阵计算--------------')
print(a * b)  # 矩阵相乘
print(a - b)  # 矩阵相减
print(a + b)  # 矩阵相加
print(a * 10)  # 数乘矩阵
