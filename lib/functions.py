# -*- coding: utf-8 -*-
"""
广泛型函数相关计算模块
"""
import numpy as np
from typing import Sequence


class Function:
    """一般函数"""

    @staticmethod
    def sign(x) -> int:
        """符号函数"""
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


class Analysis:
    """数据分析函数"""

    @staticmethod
    def linear(x: Sequence, y: Sequence) -> tuple[float, float, float]:
        """线型回归"""
        if len(x) != len(y):
            raise ValueError('x and y must have the same length')
        k, b = np.polyfit(x, y, 1)
        r = np.corrcoef(x, y)[0][1]
        print('k:', k, 'b:', b, 'r:', r)
        return k, b, r


class Hydrology:
    """水文学相关函数"""

    @staticmethod
    def calculateGuaranteeRate(values: Sequence, q: float):
        """
        满足率/保证率
        values的值大于q的概率
        """
        return sum(map(lambda x: 1 if x >= q else 0, values)) / len(values)


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [2, 2, 3, 4, 6]
    # print(Analysis.linear(x, y))
    print(Hydrology.calculateGuaranteeRate(y, 3))

    pass
