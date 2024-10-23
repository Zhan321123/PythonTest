import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 11, 12]])
c = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7], [12, 11, 10]])
d = np.array([[1], [2], [3], [4]])

print('-----------基本操作-----------')
print(b.size)
print(b.tolist(), type(b.tolist()))
print(b.reshape(4, 3))
print(b.flatten())

print('-----------判断符号-----------')
print(b > 3)
print(b > c)
print(b > a)
print(b > d)

print('-----------索引----------')
print(b[0, 1])
print(b[0:2, 1:3])
print(a[[True, False, True]])
print(b[b > 3])
