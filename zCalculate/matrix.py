# -*- coding: utf-8 -*-
"""
矩阵相关计算模块
"""
from typing import Sequence, Union
import numpy as np


class MatrixBase:
    """
    矩阵相关计算
    计算过程中不检查元素是否为数类型
    直接产生一个新的二维列表，不改变自身
    """

    def __init__(self, data: Sequence[Sequence]):
        self.data = list(map(list, data))
        self.matrix = np.mat(data)

    def getShape(self) -> tuple[int, int]:
        """矩阵形状，返回(row, column)"""
        pass

    def getValue(self) -> float:
        """矩阵求值"""
        pass

    def getT(self) -> "MatrixBase":
        """矩阵转置"""
        pass

    def getInverse(self) -> "MatrixBase":
        """矩阵求逆"""
        pass

    def getCofactor(self, row: int, column: int) -> "MatrixBase":
        """矩阵余子式"""
        pass

    def getAdjoint(self) -> "MatrixBase":
        """伴随矩阵"""
        pass

    def getRank(self) -> int:
        """矩阵的秩"""
        pass

    def getNorm(self) -> float:
        """矩阵范数"""
        pass

    def getEigen(self) -> tuple:
        """矩阵特征值和特征向量"""

    def getTrace(self) -> float:
        """矩阵的迹"""
        pass

    def getUpStep(self) -> "MatrixBase":
        """化为上三角阶梯型矩阵"""
        pass

    def getDownStep(self) -> "MatrixBase":
        """化为下三角阶梯型矩阵"""
        pass

    # def getMinimal(self) -> "MatrixBase":
    #     """化为最简形矩阵"""
    #     pass

    def isSymmetry(self) -> bool:
        """是否是对称矩阵"""
        pass

    def isAntiSymmetry(self) -> bool:
        """是否是反对称矩阵"""
        pass

    def isExchangeable(self, other: "MatrixBase") -> bool:
        """矩阵是否可交换"""
        pass

    def __mul__(self, other: Union["MatrixBase", float]) -> "MatrixBase":
        """矩阵乘法，产生一个新的矩阵"""

    def __add__(self, other: "MatrixBase") -> "MatrixBase":
        """矩阵加法，产生一个新的矩阵"""

    def solveLinearEquation(self):
        """线型方程组求解"""
        pass

    def print(self):
        """简洁打印，似乎没什么用"""
        pass

    def __str__(self):
        return str(self.matrix)


class Matrix(MatrixBase):
    def __init__(self, data: Sequence[Sequence]):
        super().__init__(data)
        self.__isRectangle(data)

    def __isRectangle(self, data: Sequence[Sequence]) -> bool:
        if all(len(i) == len(data[0]) for i in data):
            return True
        else:
            print("Matrix must be rectangle")
            return False

    def __isSquare(self):
        if len(self.data) == len(self.data[0]):
            return True
        else:
            print(f"Matrix is not square, but got {self.getShape()} shape")
            return False

    def __checkRow(self, index: int) -> bool:
        if len(self.data[index]) == len(self.data):
            return True
        else:
            print(f"Row {index} is not a row, but got {len(self.data[index])} columns")
            return False

    def __checkCol(self, index: int) -> bool:
        if len(self.data) == len(self.data[index]):
            return True
        else:
            print(f"Column {index} is not a column, but got {len(self.data[index])} rows")
            return False

    def getShape(self) -> tuple[int, int]:
        return self.matrix.shape

    def getValue(self) -> float:
        if self.__isSquare():
            return np.linalg.det(self.matrix)

    def getT(self) -> "MatrixBase":
        return Matrix(self.matrix.T)

    def getInverse(self) -> "MatrixBase":
        if self.__isSquare():
            if self.getValue() == 0:
                raise ValueError("Matrix is not invertible, value = 0")
            return Matrix(np.linalg.inv(self.matrix))

    def getRank(self) -> int:
        return np.linalg.matrix_rank(self.matrix)

    def getCofactor(self, row: int, column: int) -> "MatrixBase":
        if self.__checkRow(row) and self.__checkCol(column):
            return Matrix(np.delete(np.delete(self.matrix, row, 0), column, 1))

    def getAdjoint(self) -> "MatrixBase":
        if self.__isSquare():
            if self.getValue() == 0:
                raise ValueError("Matrix's value is 0, don't have adjoint matrix")
            return Matrix(np.linalg.inv(self.matrix).T * self.getValue())

    def getNorm(self) -> float:
        return np.linalg.norm(self.matrix)

    def getEigen(self) -> tuple:
        return np.linalg.eig(self.matrix)

    def getTrace(self) -> float:
        return np.trace(self.matrix)

    def getUpStep(self) -> "MatrixBase":
        return Matrix(np.triu(self.matrix))

    def getDownStep(self) -> "MatrixBase":
        return Matrix(np.tril(self.matrix))

    def isSymmetry(self) -> bool:
        return np.allclose(self.matrix, self.matrix.T)

    def isAntiSymmetry(self) -> bool:
        return np.allclose(self.matrix, -self.matrix.T)

    def isExchangeable(self, other: "MatrixBase") -> bool:
        m = self.matrix * other.matrix
        n = other.matrix * self.matrix
        return np.allclose(m, n)

    def __mul__(self, other: Union["MatrixBase", float]):
        if isinstance(other, MatrixBase):
            if self.getShape()[0] != other.getShape()[1]:
                print(f"Matrix {self.getShape()} can't multiply {other.getShape()}")
            else:
                return self.matrix * other.matrix
        else:
            return self.matrix * other

    def __add__(self, other: "MatrixBase") -> "MatrixBase":
        if self.getShape() == other.getShape():
            return self.matrix + other.matrix
        else:
            print(f"Matrix {self.getShape()} can't add {other.getShape()}")

    def print(self):
        print('---------matrix---------')
        print(self.matrix)
        print(f"shape = {self.getShape()}")
        print(f'----------end-----------')


if __name__ == '__main__':
    m = Matrix([[1, 2, 3, 4], [2, 5, 6, 6], [3, 6, 10, 8]])
    n = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10], [9, 10, 11]])
    # print(m.getInverse())
    # print(m.getCofactor(1,2).matrix)
    print(m * n)
    print(n * m)
    print(n * n)
