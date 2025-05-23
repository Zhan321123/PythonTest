# -*- coding: utf-8 -*-
"""
一维数组相关计算
"""
from copy import copy, deepcopy
import random
from typing import Sequence, Union, Any
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import skew, gamma
from lib.zCalculate.importBase import importMatplotlib


class _Line(Sequence):
    """一维数组，包含许多方法"""
    data: list

    def __init__(self, data: Sequence):
        self.data = list(data)

    def get(self):
        """返回数据list"""
        pass

    def getType(self):
        """
        获取元素类型
        如果元素类型单一，则返回该类型，否则返回类型列表
        ['str',1,2,3,'4'].getType() = [str,int]
        [1,2,3].getType() = int
        """
        pass

    # def isSingleType(self) -> bool:
    #     """判断是否为单一类型"""
    #     pass

    def length(self) -> int:
        """获取长度"""
        pass

    def replace(self, old, new):
        """
        替换所有
        [1,1,2,3].replace(1,10) = [10,10,2,3]
        """
        pass

    _kinds = ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']

    def interpolate(self, method: str = 'slinear', old=np.nan, lowest=None):
        """
        插值，先用linear方法插值中间内容，然后用临近法插值两端

        指定old为缺失值，默认为np.nan，会进行替换和插补

        lowest为最小值，如果插补后含有小于lowest的值，会先清除，然后linear插补
        如果原本有的值就小于lowest，也会替换和插补

        methods in ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']
        """
        pass

    def toSet(self):
        """
        去重
        [1,2,2,3].toSet() = [1,2,3]
        """
        pass

    def reverse(self):
        """颠倒"""
        pass

    def countOfElement(self, value) -> int:
        """统计元素出现的次数"""
        pass

    def elementOfCount(self, count: int) -> list:
        """
        获取出现次数为count的元素
        [1,2,3,3,4,4].elementOfCount(2) = [3,4]
        """
        pass

    def countOfEachElement(self, reverse=False) -> dict:
        """
        统计每个元素出现的次数
        非reverse时，返回{element:int}，各元素出现的次数
        [1,1,1,3,4,4].countOfEachElement() = {1:3,3:1,4:2}
        是reverse时，返回{int:[element]}，出现为n次的元素
        [1,1,1,3,4,4].countOfEachElement(True) = {3:1,1:3,2:4}
        """
        pass

    def toList(self) -> list:
        """转为列表"""
        pass

    def sort(self, reverse=False):
        """排序"""
        pass

    def pop(self) -> Any:
        """弹出最后一个元素"""
        pass

    def clear(self) -> list:
        """清空"""
        pass

    def print(self):
        """简洁打印"""
        pass

    def printAll(self):
        """打印所有数据"""
        pass

    def has(self, value) -> bool:
        """
        判断是否包含
        [1,2,3].has(1) = true
        """
        pass

    def hasAll(self, value: Sequence) -> bool:
        """
        判断是否包含所有
        [1,2,3].hasAll([1,3]) = True
        [1,2,3].hasAll([1,4]) = False
        """
        pass

    def insertAnElement(self, index, value):
        """
        插入元素
        [1,2,3].insertAnElement(1,4) = [1,4,2,3]
        """
        pass

    def removeAnElement(self, index):
        """删除元素"""
        pass

    def removeElements(self, value):
        """删除所有该元素"""
        pass

    def insertList(self, index, value: Sequence):
        """
        插入列表
        [1,2,3].insertList(1,[4,5]) = [1,4,5,2,3]
        """
        pass

    def replaceList(self, index, value: Sequence):
        """
        替换列表部分元素
        [1,2,3].replaceList(0,[10,20]) = [10,20,3]
        [1,2,3].replaceList(1,[4,5,6]) = [1,4,5,6]
        """
        pass

    def isIt(self, value) -> list[bool]:
        """
        返回等于value的boolean列表
        [1,2,3].isIt(2) = [False,True,False]
        """
        pass

    def greaterThan(self, value) -> list[bool]:
        """
        返回大于等于value的boolean列表
        [1,2,3].greaterThan(2) = [False,False,True]
        """
        pass

    def allAdd(self, value) -> "LineList":
        """
        所有值加value
        [1,2,3].allAdd(-2) = [-1,0,1]
        """
        pass

    def allMul(self, value) -> "LineList":
        """
        所有值乘value
        [1,2,3].allMultiply(2) = [2,4,6]
        """
        pass

    def seqMerge(self, value) -> "LineList":
        """
        将序列value完全拆解并入
        [].seqMerge([1,[2,[3,4],5],[6,7]] = [1,2,3,4,5,6,7]
        """

    def __getitem__(self, items: Union[int, Sequence[int], Sequence[bool]]):
        """
        lineList[int] -> object
            [1,2,3][1] = 2
        lineList[Sequence[bool]] -> Sequence[object]
            [1,2,3][[True,False,True]] = [1,3]
        lineList[Sequence[int]] -> Sequence[object]
            [1,2,3,4][[0,1,3]] = [1,2,4]
        """
        pass

    def __setitem__(self, key: Union[int, Sequence[int]], value):
        """
        lineList[int] = object
            [1,2,3][1] = 20 -> [1,20,3]
        lineList[Sequence[int]] = Sequence[object]
            [1,2,3,4][1,2] = [20,30] -> [1,20,30,4]
            [1,2,3,4][1,2] = 20 -> [1,20,20,4]
        """
        pass

    def __imul__(self, other):
        """
        self *= float(other)
            [1,2,3] * 2 = [2,4,6]
        """

    def __add__(self, other: Union[Sequence, Any]) -> "LineList":
        """
        other2 = self + other
            [1,2,3] + [4,5] -> [1,2,3,4,5]
            [1,2,3] + 4 -> [1,2,3,4]
        """
        pass

    def __iadd__(self, other: Union[Sequence, Any]):
        """
        self += list(other)
            [1,2,3] + [4,5] = [1,2,3,4,5]
            [1,2,3] + 4 = [1,2,3,4]
        """
        pass

    def __str__(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        return self.length()

    def __eq__(self, other):
        pass

    def __int__(self) -> "LineList":
        pass


class _LineFigure:
    """一维数组生成图像"""

    def generateLineFigure(self):
        """生成折线图"""
        pass


class _LineToFlat:
    """一维数组转化为二维数组"""

    def toFlatByCol(self, col: int) -> list[list]:
        """通过指定列转化为二维数组 list[list]"""
        pass

    def toFlatByRow(self, row: int, fill=0) -> list[list]:
        """
        通过指定行转化为二维数组 list[list]
        如果最后一列元素不够则用fill填充
        """
        pass

    def toColumn(self) -> list[list]:
        """转换为列数据 list[list[element]]"""
        pass


class _LineAnalysis:
    """一维数组数据分析"""

    def getMode(self) -> tuple:
        """众数"""
        pass

    def getMedian(self) -> float:
        """中位数"""
        pass

    def sum(self) -> float:
        """求和"""
        pass

    def getMean(self) -> float:
        """平均数"""
        pass

    def getVariance(self) -> float:
        """方差"""
        pass

    def getStandardDeviation(self) -> float:
        """标准差"""
        pass

    def getCv(self) -> float:
        """变异系数/变差系数"""
        pass

    def getCs(self) -> float:
        """偏度系数/偏态系数/偏差系数/Skewness"""
        pass

    def mannKendall(self):
        """Mann-Kendall(MK)突变检验"""
        pass

    def occupancy(self) -> list:
        """统计自身占总体的比例"""
        pass

    def guaranteedValue(self, p: float) -> float:
        """p3型曲线，保证率为p的值"""
        pass

    def guaranteedRate(self, value: float) -> float:
        """保证值为value的保证率"""
        pass


class LineList(_Line, _LineAnalysis, _LineFigure, _LineToFlat):
    def __init__(self, data: Sequence):
        super().__init__(data)

    def get(self):
        return self.data

    def getType(self):
        types = LineList(list(type(i) for i in self.data)).toSet()
        if types.length() == 1:
            return types[0]
        else:
            return types

    def length(self):
        return len(self.data)

    def replace(self, old, new):
        self.data = [new if i == old else i for i in self.data]
        return self

    def toSet(self):
        self.data = list(set(self.data))
        return self

    def reverse(self):
        self.data = self.data[::-1]

    def countOfElement(self, value) -> int:
        return self.data.count(value)

    def elementOfCount(self, count: int) -> list:
        if count <= 0:
            print(f"count error, count = {count}, count must > 0")
            return []
        return [i for i in set(self.data) if self.data.count(i) == count]

    def countOfEachElement(self, reverse=False) -> dict:
        d = {i: self.data.count(i) for i in set(self.data)}
        if reverse:
            # HACK 效率待优化
            dd = {i: self.elementOfCount(i) for i in d.values()}
            ks = LineList(dd.keys()).sort(reverse=True)
            return {i: dd[i] for i in ks}
        else:
            return d

    def toList(self) -> list:
        return self.data

    def sort(self, reverse=False):
        self.data.sort(reverse=reverse)
        return self

    def pop(self) -> Any:
        return self.data.pop()

    def clear(self) -> list:
        dd = self.data
        self.data = []
        return dd

    def print(self):
        if self.length() > 10:
            print(f"[{self.data[0]}, {self.data[1]}, {self.data[2]} ... {self.data[-1]}], length = {self.length()}")
        else:
            print(self.data)
        return self

    def printAll(self, column=10):
        print("-------print all elements--------")
        for i in range(0, len(self.data), column):
            print(f"row {i // column}, {self.data[i:i + column]}")
        print(f"length = {self.length()}, column = {column}")
        print("------------end------------------")
        return self

    def has(self, value) -> bool:
        return value in self.data

    def hasAll(self, value: Sequence) -> bool:
        return all(i in self.data for i in value)

    def __checkIndex(self, index):
        """检查index是否超出界限"""
        if index >= self.length():
            print('index out of range')
            return True
        return False

    def __correctIndex(self, index):
        """修正index，多数情况下，修正之后也不对"""
        length = self.length()
        if index < 0:
            while index < 0:
                index += length
        elif index >= length:
            while index >= length:
                index -= length
        return index

    def insertAnElement(self, index: int, value):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data.insert(index, value)
        return self

    def removeAnElement(self, index: int):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data.pop(index)
        return self

    def removeElements(self, value):
        length = self.length()
        self.data = list([i for i in self.data if i != value])
        if length == self.length():
            print('no value removed')
        return self

    def insertList(self, index: int, value: Sequence):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data = self.data[:index] + list(value) + self.data[index:]
        return self

    def replaceList(self, index: int, value: Sequence):
        self.__checkIndex(index + len(value))
        self.data[index:index + len(value)] = list(value)
        return self

    def isIt(self, value) -> list[bool]:
        return [(i is value) | (i == value) for i in self.data]

    def _reverse(self, bs: Sequence[bool]) -> Sequence[bool]:
        return [not i for i in bs]

    def _boolsToIndexes(self, bs: Sequence[bool]) -> Sequence[int]:
        return [i for i, j in enumerate(bs) if j]

    def greaterThan(self, value, ) -> list[bool]:
        return [i >= value for i in self.data]

    def allAdd(self, value) -> "LineList":
        self.data = list(i + value for i in self.data)
        return self

    def allMul(self, value) -> "LineList":
        self.data = list(i * value for i in self.data)
        return self

    def seqMerge(self, value) -> "LineList":
        if not isinstance(value, list):
            self.data.append(value)
        mid = []
        for item in value:
            if isinstance(item, list):
                mid.extend(LineList([]).seqMerge(item).get())
            else:
                mid.append(item)
        self.data.extend(mid)
        return self

    def __getitem__(self, items: Union[int, Sequence[int], Sequence[bool]]):
        if isinstance(items, int):
            return self.data[items]
        elif isinstance(items, Sequence):
            # 此处必须先判断bool再判断int
            if isinstance(items[0], bool):
                if len(items) != self.length():
                    print('Error, when get item, length of items less or greater than length of self')
                    return
                return list([ii for index, ii in enumerate(self) if items[index]])
            elif isinstance(items[0], int):
                return list([self.data[i] for i in items])

    def __setitem__(self, key: Union[int, Sequence[int]], value):
        if isinstance(key, int):
            self.data[key] = value
        elif isinstance(key, Sequence):
            if isinstance(value, Sequence):
                if len(key) != len(value):
                    print('key and value length not equal')
                    return
                for k, v in zip(key, value):
                    self.data[k] = v
                return
            else:
                self[key] = [value] * len(key)
                return

    def __imul__(self, other):
        for i in range(self.length()):
            self.data[i] *= other
        return self

    def __add__(self, other: Union[Sequence, Any]) -> "LineList":
        if isinstance(other, Sequence):
            return LineList(self.data + list(other))
        else:
            return LineList(self.data + [other])

    def __iadd__(self, other: Union[Sequence, Any]):
        if isinstance(other, Sequence):
            for i in other:
                self.data.append(i)
        else:
            self.data.append(other)
            print(f'{other} is a element not a list, but has been added to the end of the list')
        return self

    def __str__(self):
        return str(self.data)

    def __copy__(self):
        return LineList(copy(self.data))

    def __deepcopy__(self):
        return LineList(deepcopy(self.data))

    def __iter__(self):
        return iter(self.data)

    def __eq__(self, other):
        if isinstance(other, Sequence):
            return all(i == j for i, j in zip(self.data, other))
        return False

    def __int__(self) -> "LineList":
        self.data = list(map(int, self.data))
        return self

    def int(self) -> "LineList":
        self.__int__()
        return self

    def generateLineFigure(self):
        plt = importMatplotlib()
        plt.plot(list(range(self.length())), self.data, marker='o')
        plt.grid()
        plt.show()

    def getMode(self) -> list:
        c = self.countOfEachElement(reverse=True)
        return c[list(c.keys())[0]]

    def getMedian(self) -> float:
        s = self.__deepcopy__().sort()
        length = s.length()
        if length % 2 == 0:
            return (s[length // 2 - 1] + s[length // 2]) / 2
        else:
            return s[length // 2]

    def sum(self) -> float:
        return sum(self.data)

    def getMean(self) -> float:
        return self.sum() / self.length()

    def getVariance(self) -> float:
        return sum([i ** 2 for i in self]) / self.length() - self.getMean() ** 2

    def getStandardDeviation(self) -> float:
        return self.getVariance() ** 0.5

    def getCv(self) -> float:
        return self.getStandardDeviation() / self.getMean()

    def getCs(self) -> float:
        return float(skew(self.data))

    def mannKendall(self):
        length = self.length()
        sign = lambda x: 1 if x > 0 else -1
        s = sum(sign(self[j] - self[i]) for i in range(length) for j in range(i + 1, length))
        var = length * (length - 1) * (2 * length + 5) / 18
        if s == 0:
            z = 0
        elif s > 0:
            z = s / (var ** 0.5)
        else:
            z = (s + 1) / (var ** 0.5)
        return z

    def occupancy(self) -> list:
        summ = self.sum()
        return [i / summ for i in self.data]

    def guaranteedValue(self, p: float) -> float:
        if not self.greaterThan(0):
            print('all elements must greater than 0, maybe is 0-')
        if 0 <= p <= 1:
            shape, loc, scale = gamma.fit(self.data, floc=0)  # 估计伽玛分布的参数
            dist = gamma(shape, loc=loc, scale=scale)  # 创建伽玛分布对象
            return dist.ppf(1 - p)
        else:

            print('p must between 0 and 1')

    def guaranteedRate(self, value: float) -> float:
        m = 0
        for i in self.data:
            m += (1 if i >= value else 0)
        return m / self.length()

    def toColumn(self) -> list[list]:
        return [[i] for i in self]

    def toFlatByRow(self, row: int, fill=None) -> list[list]:
        if self.length() % row != 0:
            print('when line change to flat, result will not a rectangle')
        result = list([self.data[i:i + row] for i in range(0, self.length(), row)])
        if fill is None:
            return result
        else:
            result[-1] += [fill] * (row - len(result[-1]))
            return result

    def toFlatByCol(self, col: int, fill=None) -> list[list]:
        return self.toFlatByRow(self.length() // col, fill)


class LineUtil:
    @staticmethod
    def equidistantListByStep(start, end, step) -> list:
        """生成等距list，用步长"""
        return [start + i * step for i in range(int((end - start) / step) + 1)]

    @staticmethod
    def equidistantListByNum(start, end, num) -> list:
        """生成等距list，用数量"""
        return [start + i * (end - start) / (num - 1) for i in range(num)]

    @staticmethod
    def createRandomList(num: int, lowest, highest) -> list:
        """
        生成随机list
        个数为num，最小值为欸lowest，最大值为highest
        """
        return list([random.random() * (highest - lowest) + lowest for _ in range(num)])

    @staticmethod
    def replaceRandom(aList: Sequence, proportion: float, new) -> list:
        """
        将列表中的元素随机替换成new
        proportion为占比概率，new为替换的新元素
        """
        if (proportion > 1) | (proportion < 0):
            print('proportion must less than 1')
        return [new if random.random() < proportion else i for i in aList]


if __name__ == '__main__':
    l = LineList(
        [0, 2, 1, 1, 1, 1, 1, 0, 4, 0, 6, 1, 1, 0, 7, 0, 9, 4, 10, 0, 25, 0, 25, 16, 25, 89, 82, 34, 76, 89, 90, 16, 81,
         12, 67, 24, 0])
    # f = FlatList(l.toFlatByCol(4, fill=0))
    # l2 = LineList([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 5, 6, 5, 6])
    # print(l2.getCv())
    # print(l2.getCs())
    LineList([]).seqMerge([1, [2, [3, 4], 5], [6, 7]]).printAll()
    pass
