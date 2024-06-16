"""
熵权法

head = ["Chinese", "Math", "Physics", "Chemistry", "English", "Politics", "Biology", "History", "demerit"]
data = {
    "s1": [93, 66, 86, 88, 77, 71, 90, 94, 16],
    "s2": [97, 99, 61, 61, 75, 87, 70, 70, 23],
    "s3": [65, 99, 94, 71, 91, 86, 80, 93, 10],
    "s4": [97, 79, 98, 61, 92, 66, 88, 69, 21],
    "s5": [85, 92, 87, 63, 67, 64, 96, 98, 41],
    "s6": [63, 65, 91, 93, 80, 80, 99, 74, 18],
    "s7": [71, 77, 90, 88, 78, 99, 82, 68, 14],
    "s8": [82, 97, 76, 73, 86, 73, 65, 70, 28],
    "s9": [99, 92, 86, 98, 89, 83, 66, 85, 9],
    "s10": [99, 99, 67, 61, 90, 69, 70, 79, 12]
}
head是科目，data是每个学生具体的成绩，利用熵权法评价每个学科的权重，并给学生排名

"""
import math
from copy import deepcopy
from typing import Sequence
import numpy as np
import pandas as pd
from scipy.stats import entropy


def t(l: Sequence[Sequence]):
    return np.array(l).T.tolist()


def entropyWeight(head: Sequence, distinct: Sequence[bool], data: dict[str, Sequence[float]], move: float = 0.01):
    if len(head) != len(distinct):
        print("head和distinct长度不一致")
        return
    for i in data:
        if len(data[i]) != len(head):
            print("数据长度不一致")
            return
    d = [data[i] for i in deepcopy(data)]
    dataT = t(d)

    # 指标最大值
    maxJ = [max(i) for i in dataT]
    # 指标最小值
    minJ = [min(i) for i in dataT]
    # 指标极差
    evJ = [maxJ[i] - minJ[i] for i in range(len(maxJ))]

    # 数据标准化
    standardIj = []
    for i in range(len(d)):
        s = []
        for j in range(len(d[i])):
            if distinct[j]:
                s.append((d[i][j] - minJ[j]) / evJ[j])
            else:
                s.append((maxJ[j] - d[i][j]) / evJ[j])
        standardIj.append(s)

    # 数据平移
    moveIj = []
    for i in standardIj:
        s = []
        for j in i:
            s.append(j + move)
        moveIj.append(s)

    pIj = []
    columnSum = [sum(i) for i in t(moveIj)]
    for i in range(len(moveIj)):
        pIj.append([moveIj[i][j] / columnSum[j] for j in range(len(moveIj[i]))])

    k = 1 / math.log(len(data))

    eJ = []
    for i in t(pIj):
        eJ.append(-k * sum(j * math.log(j) for j in i))

    GJ = [1 - i for i in eJ]

    # 指标权重
    WJ = [i / sum(GJ) for i in GJ]

    # 线型加权法得到的数
    weightIj = []
    for i in range(len(standardIj)):
        weightIj.append([standardIj[i][j] * WJ[j] for j in range(len(standardIj[i]))])

    # 模型最终评价分数
    scoreI = [sum(i) for i in weightIj]
    print(data.keys())
    print(scoreI)
    pass


# 指标类型
head = ["Chinese", "Math", "Physics", "Chemistry", "English", "Politics", "Biology", "History", "demerit"]
# 指标正负之分，正向指标为欸负
distinct = [True, True, True, True, True, True, True, True, False]
# 各个模型的参数
data = {
    "s1": [93, 66, 86, 88, 77, 71, 90, 94, 16],
    "s2": [97, 99, 61, 61, 75, 87, 70, 70, 23],
    "s3": [65, 99, 94, 71, 91, 86, 80, 93, 10],
    "s4": [97, 79, 98, 61, 92, 66, 88, 69, 60],
    "s5": [85, 92, 87, 63, 67, 64, 96, 98, 41],
    "s6": [63, 65, 91, 93, 80, 80, 99, 74, 18],
    "s7": [71, 77, 90, 88, 78, 99, 82, 68, 14],
    "s8": [82, 97, 76, 73, 86, 73, 65, 70, 28],
    "s9": [99, 92, 86, 98, 89, 83, 66, 85, 9],
    "s10": [99, 99, 67, 61, 90, 69, 70, 79, 12]
}

entropyWeight(head, distinct, data)
