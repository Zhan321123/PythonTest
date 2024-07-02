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

    def getCofactor(self) -> "MatrixBase":
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

    def getStep(self) -> "MatrixBase":
        """化为阶梯型矩阵"""
        pass

    def getMinimal(self) -> "MatrixBase":
        """化为最简形矩阵"""
        pass

    def isSymmetry(self) -> bool:
        """是否是对称矩阵"""
        pass

    def isAntiSymmetry(self) -> bool:
        """是否是反对称矩阵"""
        pass

    def isExchangeable(self, other: "MatrixBase") -> bool:
        """矩阵是否可交换"""
        pass

    def __imul__(self, other: Union["MatrixBase", float]):
        """矩阵乘法，改变自身"""
        pass

    def __rmul__(self, other: "MatrixBase") -> "MatrixBase":
        """矩阵乘法，产生一个新的矩阵"""

    def __iadd__(self, other: "MatrixBase"):
        """矩阵加法，改变自身"""
        pass

    def __radd__(self, other: "MatrixBase") -> "MatrixBase":
        """矩阵加法，产生一个新的矩阵"""

    def solveLinearEquation(self):
        """线型方程组求解"""
        pass


class Matrix(MatrixBase):
    def __init__(self, data: Sequence[Sequence]):
        if not self.__isRectangle(data):
            print("Matrix must be square")
        super().__init__(data)

    def __isRectangle(self, data: Sequence[Sequence])->bool:
        return all(len(i) == len(data) for i in data)

    def __isSquare(self):
        if len(self.data) == len(self.data[0]):
            return True
        else:
            print(f"Matrix is not square, but got {self.getShape()} shape")
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

    def getCofactor(self) -> "MatrixBase":
        pass



if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m.getInverse())
