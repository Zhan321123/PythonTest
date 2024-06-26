import numpy as np

# 假设aList是一个NumPy数组
from scipy.interpolate import interp1d

# data = [0, 7, 8, 9, 0, 11, 0, 0, 14, 0, 0, 17, 18, 0, 0, 0, 22, 23, 0, 25, 0, 27, 28, 0, 0, 0, ]

# d = [0,1,2,4,5]
# b = [True,False,True,True,True]
# l = [i for index,i in enumerate(d) if b[index]]
# print(l)

# 定义 x 和 y 数据点
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])

# 创建一个线性插值函数
linear_interp = interp1d(x, y)

# 使用插值函数估算 x=1.5 时的 y 值
estimated_y = linear_interp(1.5)
print(estimated_y)  # 输出插值结果
