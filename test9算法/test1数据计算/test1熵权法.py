"""
熵权法
"""
from typing import Sequence
import numpy as np
import lib.zCalculate as zc
from scipy.stats import entropy


def entropyWeight(data: Sequence[Sequence], distinct: Sequence[bool] = None, move: float = 1e-9):
    """计算权重"""
    fl = zc.FlatList(data)
    # 检查数据
    if not fl.isRectangle(): print("数据错误")
    if distinct is None:
        distinct = [True] * fl.col()
    else:
        if len(distinct) != fl.col(): print("数据错误")
    # 标准化数据
    fl2 = fl.__deepcopy__().allMul(0).allAdd(move)
    maxs = list(max(i) for i in fl.__deepcopy__().transpose())
    mins = list(min(i) for i in fl.__deepcopy__().transpose())
    for i in range(fl.row()):
        for j in range(fl.col()):
            if distinct[j]:
                fl2[i][j] = (fl[i][j] - mins[j]) / (maxs[j] - mins[j] + move)
            else:
                fl2[i, j] = (maxs[j] - fl[i, j]) / (maxs[j] - mins[j] + move)
    nd = fl2._getNode()

    # 每个指标的概率分布
    p_ij = nd / np.sum(nd, axis=0)
    # 避免除数为零的情况
    p_ij[p_ij == 0] = 1e-9
    # 计算信息熵
    entropies = []
    for col in range(p_ij.shape[1]):
        entropies.append(entropy(p_ij[:, col], base=p_ij.shape[0]))
    entropies = np.array(entropies)
    k = np.sum((1 - entropies))
    weights = (1 - entropies) / k
    print(weights)
    return weights

if __name__ == '__main__':
    # 指标类型
    head = ["Chinese", "Math", "Physics", "Chemistry", "English", "Politics", "Biology", "History", "demerit"]
    # 指标正负之分，正向指标为True，负向指标为False
    distinct = [True, True, True, True, True, True, True, True, False]
    # 各个模型的参数
    data = [[100, 000, 86, 88, 77, 71, 90, 94, 16],
            [100, 000, 61, 61, 75, 87, 70, 70, 23],
            [100, 000, 94, 71, 91, 86, 80, 93, 10],
            [100, 000, 98, 61, 92, 66, 88, 69, 60],
            [100, 000, 87, 63, 67, 64, 96, 98, 41],
            [100, 100, 91, 93, 80, 80, 99, 74, 18],
            [100, 100, 90, 88, 78, 99, 82, 68, 14],
            [100, 100, 76, 73, 86, 73, 65, 70, 28],
            [100, 100, 86, 98, 89, 83, 66, 85, 90],
            [99 , 100, 67, 61, 90, 69, 70, 79, 12]]

    ws = entropyWeight(data, distinct)
    print(sum(ws))