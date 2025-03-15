"""
矩阵操作

矩阵求值
矩形面替换
矩形面复制
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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


def matrixTile(matrix: np.ndarray, repeat:tuple[int, int])->np.ndarray:
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


def matrixDisplay(ax: plt.Axes, matrix: np.ndarray):
    """
    使用matplotlib展示矩阵
    :param ax:
    :param matrix:
    :return:
    """
    ax.pcolormesh(matrix, cmap='rainbow', edgecolors='k', linewidth=0.5)
    ax.set_aspect('equal')


if __name__ == '__main__':
    array16 = np.linspace(0, 1, 256).reshape((16, 16))
    array8 = np.linspace(1, 0, 64).reshape((8, 8))
    # a = matrixCover(array16, array16, (4, 4))
    a = matrixTile(array8, (2, 3))
    print(a)

    fig, ax = plt.subplots()
    matrixDisplay(ax, a)
    plt.show()
