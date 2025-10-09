"""
matrix

创建矩阵
	补0、1
	创建E
	增减行
	增减列
	矩阵平铺
    清空矩阵
	
存储矩阵
	删除矩阵
	展示矩阵

单独矩阵
	行列式的值
	逆矩阵
	矩阵转置
	矩阵的秩
	伴随矩阵
	矩阵范数
	矩阵特征向量
	矩阵的迹
	上三角行列式
	下三角行列式
	旋转 rotate90/rotate180/rotate270
	镜像 mirrorVertical/mirrorHorizontal


矩阵与数
	数乘矩阵
	矩阵余子式

矩阵与矩阵
	矩阵相乘
	是否是对称矩阵
	是否是反对称矩阵
	是否可交换
	矩阵相加

其他
	多元线性方程组求解 multipleLinearEquation

"""
import math

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy

matplotlib.use('TkAgg')


def matrixCover(bottomMatrix: np.ndarray, topMatrix: np.ndarray, startPosition: tuple[int, int]) -> np.ndarray:
  """
  矩阵覆盖
  就像图片一样的覆盖方式
  当topMatrix.shape+startPosition > bottomMatrix.shape时，不会扩展bottomMatrix.shape
  :param bottomMatrix: 被覆盖的矩阵
  :param topMatrix: 覆盖矩阵
  :param startPosition: 覆盖的起始位置，从0开始
  :return: 覆盖后的矩阵 bottomMatrix
  """
  row, col = startPosition
  coverLength = min(bottomMatrix.shape[0] - row, topMatrix.shape[0])
  coverWidth = min(bottomMatrix.shape[1] - col, topMatrix.shape[1])
  bottomMatrix[row:row + coverLength, col:col + coverWidth] = topMatrix[0:coverLength, 0:coverWidth]
  return bottomMatrix


def matrixTile(matrix: np.ndarray, repeat: tuple[int, int]) -> np.ndarray:
  """
  矩阵阵列重复平铺，就像瓷砖一样
  与np.tile的参数reps的(row, col)相反
  :param matrix: [[]]
  :param repeat: (横向重复数量, 纵向重复数量)
  :return: 阵列后的矩阵
  """
  row, col = repeat
  if row == 1 and col == 1:
    return matrix
  if type(matrix[0][0]) == np.number:
    return np.tile(matrix, (col, row))
  else:
    return np.tile(matrix, (col, row, 1))


def matrixDisplay(matrixes: [np.ndarray]):
  """
  使用matplotlib展示矩阵
  :param matrixes: [[]]s
  :return:
  """
  columns = math.isqrt(len(matrixes))
  if columns * columns < len(matrixes):
    columns += 1
  rows = (len(matrixes) + columns - 1) // columns
  fig, axs = plt.subplots(rows, columns)
  if columns > 1:
    axs = axs.flatten()
  else:
    axs = [axs]
  for i, matrix in enumerate(matrixes):
    axs[i].pcolormesh(matrix, cmap='rainbow', edgecolors='k', linewidth=0.5)
    axs[i].set_title(i)
    axs[i].set_aspect('equal')
  plt.show()


def isSquare(matrix: np.ndarray) -> bool:
  """
  判断矩阵是否为正方形
  :param matrix: [[]]
  :return:
  """
  return matrix.shape[0] == matrix.shape[1]


def getShape(matrix: np.ndarray) -> tuple[int, int]:
  """
  获取矩阵的形状
  :param matrix: [[]]
  :return: (row, col)
  """
  return matrix.shape[0], matrix.shape[1]


def getValue(matrix: np.ndarray) -> float:
  """
  获取行列式的值
  :param matrix: [[]]
  :return: 行列式的值
  """
  if isSquare(matrix):
    return np.linalg.det(matrix)
  else:
    raise ValueError('矩阵不是正方形，无法求值')


def getTranspose(matrix: np.ndarray) -> np.ndarray:
  """
  获取矩阵转置
  :param matrix: [[]]
  :return: 转置矩阵
  """
  return matrix.T


def getInverse(matrix: np.ndarray) -> np.ndarray:
  """
  获取矩阵的逆矩阵
  :param matrix: [[]]
  :return: 逆矩阵
  """
  if not isSquare(matrix):
    raise ValueError('矩阵不是正方形，无法求逆')
  if getValue(matrix) == 0:
    raise ValueError('矩阵的值为0，无法求逆')
  return np.linalg.inv(matrix)


def getRank(matrix: np.ndarray) -> int:
  """
  获取矩阵的秩
  :param matrix: [[]]
  :return: 矩阵的秩
  """
  return np.linalg.matrix_rank(matrix)


def getCofactor(matrix: np.ndarray, row: int, column: int) -> np.ndarray:
  """
  获取矩阵的余子式
  :param matrix: [[]]
  :param row: 行
  :param column: 列
  :return:
  """
  if row >= matrix.shape[0] or column >= matrix.shape[1]:
    raise ValueError('row或column超出矩阵的形状')
  return np.delete(np.delete(matrix, row, 0), column, 1).copy()


def getAdjoint(matrix: np.ndarray) -> np.ndarray:
  """
  获取矩阵的伴随矩阵
  :param matrix: [[]]
  :return: [[]]
  """
  if not isSquare(matrix):
    raise ValueError('矩阵不是正方形，无法求伴随矩阵')
  if getValue(matrix) == 0:
    raise ValueError('矩阵的值为0，无法求伴随矩阵')
  return np.linalg.inv(matrix).T * getValue(matrix)


def getNorm(matrix: np.ndarray) -> float:
  """
  获取矩阵的范数
  :param matrix: [[]]
  :return: 矩阵的范数
  """
  return float(np.linalg.norm(matrix))


def getEigen(matrix: np.ndarray) -> tuple:
  """
  获取矩阵的特征值和特征向量
  :param matrix: [[]]
  :return: (特征值, 特征向量)
  """
  return np.linalg.eig(matrix)


def getTrace(matrix: np.ndarray) -> float:
  """
  获取矩阵的迹
  :param matrix: [[]]
  :return: 矩阵的迹
  """
  if not isSquare(matrix):
    raise ValueError('矩阵不是正方形，无法求迹')
  return np.trace(matrix)


def getUpStep(matrix: np.ndarray) -> np.ndarray:
  """
  获取矩阵的上三角矩阵
  :param matrix: [[]]
  :return: [[]]
  """
  return np.triu(matrix)


def getDownStep(matrix: np.ndarray) -> np.ndarray:
  """
  获取矩阵的下三角矩阵
  :param matrix: [[]]
  :return: [[]]
  """
  return np.tril(matrix)


def isSymmetry(matrix: np.ndarray) -> bool:
  """
  判断矩阵是否为对称矩阵
  :param matrix: [[]]
  :return:
  """
  return np.allclose(matrix, getTranspose(matrix))


def isAntiSymmetry(matrix: np.ndarray) -> bool:
  """
  判断矩阵是否为反对称矩阵
  :param matrix: [[]]
  :return:
  """
  return np.allclose(matrix, -getTranspose(matrix))


def isExchangeable(matrix: np.ndarray, other: np.ndarray) -> bool:
  """
  判断矩阵是否为交换矩阵
  :param matrix: [[]]
  :param other: [[]]
  :return:
  """
  return np.allclose(matrixMul(matrix, other), matrixMul(other, matrix))


def matrixMul(matrix: np.ndarray, other: np.ndarray) -> np.ndarray:
  """
  矩阵乘法
  :param matrix: [[]]
  :param other: [[]]
  :return: [[]]
  """
  if matrix.shape[1] != other.shape[0]:
    raise ValueError('矩阵的形状不匹配')
  return np.dot(matrix, other)


def matrixAdd(matrix: np.ndarray, other: np.ndarray) -> np.ndarray:
  """
  矩阵加法
  :param matrix: [[]]
  :param other: [[]]
  :return: [[]]
  """
  if matrix.shape != other.shape:
    raise ValueError('矩阵的形状不匹配')
  return np.add(matrix, other)


def matrixRotate90(matrix: np.ndarray) -> np.ndarray:
  """
  矩阵顺时针旋转90
  :param matrix:
  :return:
  """
  return np.rot90(matrix)


def matrixRotate180(matrix: np.ndarray) -> np.ndarray:
  """
  矩阵顺时针旋转180
  :param matrix:
  :return:
  """
  return np.rot90(matrix, 2)


def matrixRotate270(matrix: np.ndarray) -> np.ndarray:
  """
  矩阵顺时针旋转270
  :param matrix:
  :return:
  """
  return np.rot90(matrix, 3)


def mirrorVertical(matrix: np.ndarray) -> np.ndarray:
  """
  矩阵垂直翻转
  :param matrix:
  :return:
  """
  return np.flipud(matrix)


def mirrorHorizontal(matrix: np.ndarray) -> np.ndarray:
  """
  矩阵水平翻转
  :param matrix:
  :return:
  """
  return np.fliplr(matrix)


def multipleLinearEquation(matrix: np.ndarray, values: np.ndarray) -> tuple:
  """
  多元线性方程组求解
  :param matrix:
  :param values:
  :return:
  """
  if not len(matrix[0]) == len(matrix) == len(values):
    raise ValueError('矩阵的行列数和值数不匹配')
  if getValue(matrix) == 0:
    raise ValueError('矩阵无解或无数解')
  return tuple(np.linalg.solve(matrix, values))


def matrixConvolution(matrix: np.ndarray, kernel: np.ndarray) -> np.ndarray:
  """
  矩阵卷积
  :param matrix: 被卷积矩阵
  :param kernel: 卷积核
  :return: 卷积结果
  """
  if matrix.shape[0] < kernel.shape[0] or matrix.shape[1] < kernel.shape[1]:
    raise ValueError('矩阵的形状小于卷积核的形状')
  return scipy.signal.convolve2d(matrix, kernel, 'valid')


def matrixPadding(matrix: np.ndarray, pad: int, padValue) -> np.ndarray:
  """
  矩阵拓展边缘
  :param matrix: 被填充矩阵
  :param pad: 填充数
  :param padValue: 填充值
  :return: 填充结果
  """
  return np.pad(matrix, pad, 'constant', constant_values=padValue)


if __name__ == '__main__':
  array16 = np.linspace(0, 1, 256).reshape((16, 16))
  array8 = np.linspace(1, 0, 64).reshape((4, 16))
  # a = matrixCover(array16, array16, (4, 4))
  # a = matrixTile(array8, (2, 3))
  # print(a)
  # a = matrixRotate90(array8)
  # matrixDisplay([
  #   array8, a, matrixRotate180(array8), matrixRotate270(array8), mirrorHorizontal(array8), mirrorVertical(array8)
  # ])
  # v = multipleLinearEquation(np.array([[2, 1], [1, 2]]), np.array([3, 5]))
  # print(v)
  array9 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  core = np.array([[1, 0], [0, 1]])
  print(matrixConvolution(array9, core))
