# -*- coding: utf-8 -*-
"""
二维数组相关计算
"""
from copy import copy, deepcopy
from typing import Sequence, Union, Any

from lib.zCalculate.importBase import importMatplotlib


class _Flat(Sequence):
    """
    二维数组列表
    在执行过程中，请保持每列元素个数相等

    执行和返回对象全部为list，要执行一维数组列表，请套入LineList
    """
    data: list[list]

    def __init__(self, data: Sequence[Sequence]):
        self.data = list(map(list, data))
        if len(data) == 0:
            print("data is empty, subsequent operations may encounter issues")

    def _reformList(self):
        """归正数据"""
        self.data = list(map(list, self.data))

    def _isRectangle(self) -> bool:
        """判断是否为矩形"""
        for i in self.data:
            if len(i) != len(self.data[0]):
                print("data is not rectangle, subsequent operations may encounter issues")
                return False
        return True

    def get(self):
        return self.data

    def row(self) -> int:
        return len(self.data)

    def col(self) -> int:
        if len(self.data) == 0:
            print("data is empty, so column is 0")
            return 0
        return len(self.data[0])

    def count(self, value: Any) -> int:
        """统计元素个数"""
        pass

    def print(self):
        """简洁打印"""
        pass

    def printAll(self):
        """全部打印"""
        pass

    def getRow(self, index: int) -> list:
        """获取一行"""
        pass

    def insertRow(self, index: int, value: Sequence):
        """插入一行"""
        pass

    def appendRow(self, value: Sequence):
        """末尾添加一行"""
        pass

    def removeRow(self, index: int):
        """删除一行"""
        pass

    def replaceRow(self, index: int, value: Sequence):
        """替换一行"""
        pass

    def getColumn(self, index: int) -> list:
        """获取一列"""
        pass

    def removeColumn(self, index: int):
        """删除一列"""
        pass

    def insertColumn(self, index: int, value: Sequence):
        """插入一列"""
        pass

    def appendColumn(self, value: Sequence):
        """末尾添加一列"""
        pass

    def replaceColumn(self, index: int, value: Sequence):
        """替换一列"""
        pass

    def __eq__(self, other):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, item: Union[
        int, Sequence[Union[Sequence[int], Sequence[int]]], tuple[int, int, int, int]]):
        """
        FlatList[int] -> list
        FlatList[startRow:int, endRow:int, startCol:int. endCol:int] -> list[list]
        FlatList[chooseRow:Sequence[int], chooseCol:Sequence[int]] -> list[list]
        """
        pass

    def __setitem__(self, key: Union[int, Sequence[Union[int, int, int, int]]], value: Union[Sequence, int]):
        pass

    def __len__(self):
        return self.row()

    def __str__(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self):
        pass

    # 前提是元素对象都是数类型，生成图像这里都不进行检查
    def generateHotMap(self):
        """生成热图"""
        pass

    def generateLineFigure(self):
        """生成多线折线图"""
        pass


class _FlatMove:

    def transpose(self):
        """转置，对称轴为 / """
        pass

    def transposeSymmetry(self):
        """反向转置，对称轴为 \ """
        pass

    def mirrorHorizon(self):
        """镜像，水平翻转"""
        pass

    def mirrorVertical(self):
        """镜像，垂直翻转"""
        pass

    def rotate90(self):
        """顺时针旋转90度"""
        pass

    def rotate180(self):
        """顺时针旋转180度"""
        pass

    def rotate270(self):
        """顺时针旋转270度，逆时针旋转90度"""
        pass


class FlatList(_Flat, _FlatMove):
    def __init__(self, data: Sequence[Sequence]):
        super().__init__(data)

    def count(self, value: Any) -> int:
        co = 0
        for i in self:
            co += i.count(value)
        return co

    def print(self):
        if len(self.data) == 0:
            print(f"data is empty, is {self.data}")
            return
        if len(self.data[0]) <= 10:
            if len(self.data) < 10:
                for i in self.data:
                    print(i)
            else:
                for i in (0, 1, 2):
                    print(self.data[i])
                print('......')
                print(self.data[-1])
        else:
            if len(self.data) < 10:
                for i in self.data:
                    print(f'[{i[0]}, {i[1]}, ..., {i[-1]}]')
            else:
                for i in (0, 1, 2):
                    print(f'[{self.data[i][0]}, {self.data[i][1]}, ..., {self.data[i][-1]}]')
                print('......')
                print(f'[{self.data[-1][0]}, {self.data[-1][1]}, ..., {self.data[-1][-1]}]')
        print(f'row = {len(self.data)}, column = {len(self.data[0])}')
        return self

    def printAll(self):
        print('----print all element----')
        for index, i in enumerate(self.data):
            print('row :', index + 1, ',', i)
        print(f'row = {len(self.data)}, column = {len(self.data[0])}')
        print('----------end------------')
        return self

    def __checkRow(self, index: Union[int, Sequence]) -> bool:
        if index < 0 or index >= self.row():
            print('index out of range')
            return False
        else:
            return True

    def __checkRowLength(self, value: Sequence) -> bool:
        if len(value) != self.col():
            print('row length not equal, subsequent operations may encounter issues')
            return False
        return True

    def getRow(self, index: int) -> list:
        if not self.__checkRow(index):
            return []
        return self.data[index]

    def appendRow(self, value: Sequence):
        self.data.append(list(value))
        self.__checkRowLength(value)
        return self

    def insertRow(self, index: int, value: Sequence):
        if not self.__checkRow(index + 1):
            return self
        self.__checkRowLength(value)
        self.data.insert(index, list(value))
        return self

    def removeRow(self, index: int):
        if not self.__checkRow(index):
            return self
        self.data.pop(index)
        return self

    def replaceRow(self, index: int, value: Sequence):
        if not self.__checkRow(index):
            return self
        self.__checkRowLength(value)
        self.data[index] = list(value)
        return self

    def __checkCol(self, index: int) -> bool:
        if index < 0 or index >= self.col():
            print('index out of range')
            return False
        else:
            return True

    def __checkColLength(self, value: Sequence) -> bool:
        if len(value) != self.row():
            print('col length not equal')
            return False
        return True

    def getColumn(self, index: int) -> list:
        if not self.__checkCol(index):
            return []
        return list([i[index] for i in self.data])

    def removeColumn(self, index: int):
        if not self.__checkCol(index):
            return self
        for i in self.data:
            i.pop(index)
        return self

    def appendColumn(self, value: Sequence):
        if not self.__checkColLength(value):
            return self
        for i, v in enumerate(self.data):
            v.append(value[i])
        return self

    def insertColumn(self, index: int, value: Sequence):
        if not self.__checkCol(index + 1):
            return self
        if self.__checkColLength(value):
            for i in range(len(self.data)):
                self.data[i].insert(index, value[i])
        return self

    def replaceColumn(self, index: int, value: Sequence):
        if not self.__checkCol(index):
            return self
        if self.__checkColLength(value):
            for i in range(len(self.data)):
                self.data[i][index] = value[i]
        return self

    def transpose(self):
        if self._isRectangle():
            self.data = list(zip(*self.data))
            self._reformList()
        return self

    def transposeSymmetry(self):
        return self.rotate90().mirrorHorizon()

    def mirrorHorizon(self):
        if self._isRectangle():
            self.data = list(zip(*self.data[::-1]))
            self._reformList()
        return self

    def mirrorVertical(self):
        if self._isRectangle():
            self.data = self.data[::-1]
        return self

    def rotate90(self):
        return self.transpose().mirrorVertical()

    def rotate180(self):
        return self.mirrorVertical().mirrorHorizon()

    def rotate270(self):
        return self.mirrorVertical().transpose()

    def __getitem__(self, item: Union[
        int, Sequence[Union[Sequence[int], Sequence[int]]], tuple[int, int, int, int]]):
        if isinstance(item, int):
            if self.__checkRow(item):
                return self.data[item]
            return []
        elif isinstance(item, Sequence):
            if isinstance(item[0], int):
                if all((self.__checkRow(item[0]), self.__checkRow(item[1]), self.__checkCol(item[2]),
                       self.__checkCol(item[3]))):
                    return list(self.data[i][item[2]:item[3]+1] for i in range(item[0], item[1]+1))
                else:
                    print('getitem error, index out of range')
            elif isinstance(item[0], Sequence):
                if all(*map(self.__checkRow, item[0]), *map(self.__checkCol, item[1])):
                    return list([list([self.data[i][j] for j in item[1]]) for i in item[0]])

    def __setitem__(self, key: Union[int, Sequence[Union[int, int, int, int]]], value: Sequence):
        if isinstance(key, int) and self.__checkRow(key):
            if isinstance(value, Sequence):
                if self.__checkColLength(value):
                    self.data[key] = list(value)
            else:
                self.data[key] = [value] * self.col()
        elif isinstance(key, Sequence) and all(*map(self.__checkRow, key[0:1]), *map(self.__checkCol, key[2:3])):
            if isinstance(value, Sequence):
                if (len(value) != key[1] - key[0]) | (len(value[0]) != key[3] - key[2]):
                    print('setitem error, the shape of key not equal to the shape of value')
                else:
                    for index, i in enumerate(range(key[0], key[1])):
                        self.data[i][key[2]:key[3]] = list(value[index])

    def __str__(self):
        return str(self.data)

    def __copy__(self):
        return copy(self.data)

    def __deepcopy__(self):
        return deepcopy(self.data)

    def __eq__(self, other):
        if not isinstance(other, Sequence):
            return False
        for i, j in zip(self.data, other):
            for k, l in zip(i, j):
                if k != l:
                    return False
        return True

    def __iter__(self):
        return iter(self.data)

    def generateHotMap(self):
        plt = importMatplotlib()
        plt.imshowChart(self.data,,
        return plt

    def generateLineFigure(self):
        plt = importMatplotlib()
        for i in range(self.row()):
            plt.plot(self.data[i])
        plt.show()
        return self


if __name__ == '__main__':
    a = FlatList([[1, 2, 3], [1, 2, 3], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24],
                  [25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36], [37, 38, 39], [40, 41, 42]])
    # a.t().print().printAll()
    b = FlatList(
        [(1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40), (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41),
         (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42)]
    )
