# -*- coding: utf-8 -*-
"""
两列一维数组的数据计算
没有增删改功能，仅有计算功能
情况为
    y = f(x)
"""
from typing import Sequence

import numpy as np
from scipy.stats import theilslopes


class _DoubleLine:
    """两列一维数组类"""

    def __init__(self, x: Sequence, y: Sequence):
        if len(x) != len(y):
            raise ValueError('x and y must have the same length')
        self.x = list(x)
        self.y = list(y)

    def get(self) -> tuple[list, list]:
        return self.x, self.y

    def linearRegression(self) -> tuple[float, float, float]:
        """线性回归，返回(k, b, r)"""
        pass

    def pearsonCorrelationCoefficient(self) -> float:
        """
        pearson皮尔逊相关系数
        正值：正相关，负值：负相关
        1~ 极度相关 ~0.8~ 强相关 ~0.6~ 中等程度相关 ~0.4~ 弱相关 ~0.2~ 极弱相关或无相关 ~0
        """
        pass
    def senMedian(self) -> tuple[float, float, float, float]:
        """
        Theil-Sen Median斜率估计趋势分析
        """
        pass

    def generateLineFigure(self):
        """生成折线图"""
        pass

    def generateDotsFigure(self):
        """生成散点图"""
        pass

    def generateRegressionLine(self):
        """生成回归线"""
        pass

class DoubleList(_DoubleLine):
    def __init__(self, x: Sequence, y: Sequence):
        super().__init__(x, y)

    def pearsonCorrelationCoefficient(self) -> float:
        r = np.corrcoef(self.x, self.y)[0][1]
        return r

    def senMedian(self) -> tuple[float, float, float, float]:
        slope = theilslopes(self.x, self.y)
        print(f"slope:{slope[0]}, intercept:{slope[1]}, lowSlope:{slope[2]}, upSlope:{slope[3]}")
        return *slope,

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 9, 10, 12]
    d = DoubleList(x, y)
    print(d.pearsonCorrelationCoefficient())
    print(d.linearRegression())
    d.generateRegressionLine()

    pass
