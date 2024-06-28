# -*- coding: utf-8 -*-
from copy import copy, deepcopy
import random
from typing import Sequence, Union, Any
import numpy as np
from scipy.interpolate import interp1d


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
        """
        pass

    # def isSingleType(self) -> bool:
    #     """判断是否为单一类型"""
    #     pass

    def length(self) -> int:
        """获取长度"""
        pass

    def replace(self, old, new):
        """替换所有"""
        pass

    _kinds = ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']

    def interpolate(self, method: str = 'slinear', old=np.nan, lowest=None):
        """
        插值，先用linear方法插值中间内容，然后用临近法插值两端

        指定old为缺失值，默认为np.nan，会进行替换和插补

        lowest为最小值，如果插补后含有小于lowest的值，会先清除，然后linear插补
        如果原本有的值就小于lowest，也会替换和插补
        """
        pass

    def toSet(self):
        """去重"""
        pass

    def countOfElement(self, value) -> int:
        """统计元素出现的次数"""
        pass

    def elementOfCount(self, count: int) -> list:
        """获取出现次数为count的元素"""
        pass

    def countOfEachElement(self, reverse=False) -> dict:
        """
        统计每个元素出现的次数
        非reverse时，返回{element:int}，各元素出现的次数
        是reverse时，返回{int:[element]}，出现为n次的元素
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
        """判断是否包含"""
        pass

    def hasAll(self, value: Sequence) -> bool:
        """判断是否包含所有"""
        pass

    def insertAnElement(self, index, value):
        """插入元素"""
        pass

    def removeAnElement(self, index):
        """删除元素"""
        pass

    def removeElements(self, value):
        """删除所有该元素"""
        pass

    def insertList(self, index, value: Sequence):
        """插入列表"""
        pass

    def replaceList(self, index, value: Sequence):
        """替换列表部分元素"""
        pass

    def isIt(self, value) -> list[bool]:
        """返回等于value的boolean列表"""
        pass

    def greaterThan(self, value) -> list[bool]:
        """返回大于value的boolean列表"""
        pass

    def __getitem__(self, items: Union[int, Sequence[int], Sequence[bool]]):
        """
        lineList[int] -> object
        lineList[Sequence[int]] -> Sequence[object]
        lineList[Sequence[bool]] -> Sequence[object]
        """
        pass

    def __setitem__(self, key: Union[int, Sequence[int]], value):
        """
        lineList[int] = object
        lineList[Sequence[int]] = Sequence[object]
        """
        pass

    def __add__(self, other):
        """
        self+other = self.list+list(other)
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

    def generateFigure(self):
        """生成折线图"""
        pass


class LineList(_Line):
    def __init__(self, data: Sequence):
        super().__init__(data)

    def get(self):
        return self.data

    def getType(self):
        types = LineList(type(i) for i in self.data).toSet()
        if types.length() == 1:
            return types[0]
        else:
            return types

    def length(self):
        return len(self.data)

    def replace(self, old, new):
        self.data = [new if i == old else i for i in self.data]
        return self

    def interpolate(self, method: str = 'slinear', old=np.nan, lowest=None):
        if method not in self._kinds:
            print('interpolate method error, will use slinear method')
            method = 'slinear'

        if old is not np.nan:
            self.replace(old, np.nan)
        indexes = self._reverse(self.isIt(np.nan))
        x = self._boolsToIndexes(indexes)

        if len(x) == 0:
            print('no value need to interpolate')
            return self
        y = self[indexes]
        f = interp1d(x, y, kind=method, bounds_error=False, fill_value=(y[0], y[-1]))
        x = list(range(self.length()))
        self.data = f(x).tolist()

        if lowest is not None:
            self[self._boolsToIndexes(self._reverse(self.greaterThan(lowest)))] = np.nan
            self.interpolate()

        return self

    def toSet(self):
        self.data = list(set(self.data))
        return self

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
            return {i: self.elementOfCount(i) for i in d.values()}
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
        return [i > value for i in self.data]

    def generateFigure(self):
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('TkAgg')
        matplotlib.rcParams['axes.unicode_minus'] = False
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        plt.plot(list(range(self.length())), self.data, marker='o')
        plt.grid()
        plt.show()

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

    def __add__(self, other: Union[Sequence, Any]):
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


class LineUtil:
    @staticmethod
    def equidistantList(start, end, step) -> list:
        """生成等距list"""
        return [start + i * step for i in range(int((end - start) / step) + 1)]

    @staticmethod
    def createRandomList(num: int, lowest, highest) -> list:
        """
        生成随机list
        个数为num，最小值为欸lowest，最大值为highest
        """
        return list([random.random() * (highest - lowest) + lowest for i in range(num)])

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
    l = LineList([0, 2, 0, 4, 0, 6, 7, 0, 9, 10, 0, 12, 67, 24, 1, 0, 0])
    l.interpolate(old=0, method='cubic', lowest=0).printAll()
    l.generateFigure()
    # print(isinstance(l, Sequence))
    # print(l[[False] * 8 + [True] * 9])
    # l[[0, 3, 5]] = [9, 9, 9]
    # l.printAll()
    # print(l.getType())
    # l[0] = 2
    # l.print().interpolate().printAll()
    # l.replaceList(-1, [1, 2, ]).printAll()
    # print(LineUtil.equidistantList(1.1, 10, 1))
    # print(l.getType())
    # for i in l:
    #     print(i)
    l.printAll()
    pass
