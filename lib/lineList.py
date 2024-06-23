# -*- coding: utf-8 -*-
from copy import copy, deepcopy
from typing import Sequence
import numpy as np
from scipy.interpolate import interp1d


class Line:
    """一维数组"""
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

    def set(self, data: Sequence):
        """重置数据"""
        pass

    def length(self) -> int:
        """获取长度"""
        pass

    def replace(self, old, new):
        """替换所有"""
        pass

    def interpolate(self, method: str):
        """插值"""
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

    def print(self):
        """普通打印"""
        pass

    def printAll(self):
        """打印所有数据，每行10个元素"""
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

    def insertList(self, index, value: Sequence):
        """插入列表"""
        pass

    def replaceList(self, index, value: Sequence):
        """替换列表部分元素"""
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __add__(self, other):
        pass

    def __str__(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        return self.length()


class LineList(Line):
    def __init__(self, data: Sequence):
        super().__init__(data)

    def get(self):
        return self.data

    def set(self, data: Sequence):
        self.data = list(data)
        return self

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

    _kinds = ['zero', 'next', 'nearest', 'slinear', 'quadratic', 'cubic']

    def interpolate(self, method: str = 'slinear', old=np.nan, lowest=None):
        # TODO 未完成
        if method not in self._kinds:
            print('interpolate method error, will use slinear method')
            method = 'slinear'
        # npData = np.array(self.data)
        # x = np.nonzero(npData)[0]
        # print(x)
        # y = npData[x]
        # f = interp1d(x, y, kind=method, bounds_error=False, fill_value=(y[0], y[-1]))
        # x = np.arange(len(npData))
        # self.data = f(x).tolist()
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

    def print(self):
        print(f"{self}, length = {self.length()}")
        return self

    def printAll(self):
        print("-------print all elements--------")
        for i in range(0, len(self.data), 10):
            print(f"row = {i // 10}, {self.data[i:i + 10]}")
        print("length = ", self.length())
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

    def insertAnElement(self, index:int, value):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data.insert(index, value)
        return self

    def removeAnElement(self, index:int):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data.pop(index)
        return self

    def insertList(self, index:int, value: Sequence):
        if self.__checkIndex(index):
            index = self.__correctIndex(index)
        self.data = self.data[:index] + list(value) + self.data[index:]
        return self

    def replaceList(self, index:int, value: Sequence):
        self.__checkIndex(index + len(value))
        self.data[index:index + len(value)] = list(value)
        return self

    def __getitem__(self, item:int):
        return self.data[item]

    def __setitem__(self, key:int, value):
        self.data[key] = value

    def __add__(self, other: Sequence):
        for i in other:
            self.data.append(i)
        return self

    def __str__(self):
        if self.length() > 10:
            return f"[{self.data[0]}, {self.data[1]}, {self.data[2]} ... {self.data[-1]}]"
        else:
            return str(self.data)

    def __copy__(self):
        return LineList(copy(self.data))

    def __deepcopy__(self):
        return LineList(deepcopy(self.data))

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        return self.data.__next__()


class LineUtil:
    @staticmethod
    def equidistantList(start, end, step) -> list:
        """生成等距list"""
        return [start + i * step for i in range(int((end - start) / step) + 1)]


if __name__ == '__main__':
    l = LineList([0, 2, 0, 4, 0, 6, 7, 0, 9, 10, 0, 12, 24, 1, 0, 0])
    # print(l.getType())
    # l[0] = 2
    # l.print().interpolate().printAll()
    # l.replaceList(-1, [1, 2, ]).printAll()
    # print(LineUtil.equidistantList(1.1, 10, 1))
    # print(l.getType())
    pass
