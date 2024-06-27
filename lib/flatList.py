from copy import copy, deepcopy
from typing import Sequence, Union, Any
from lineList import LineList, LineUtil


class _Flat(Sequence):
    """
    二维数组列表
    在执行过程中，请保持每列元素个数相等

    执行和返回对象全部为list，要执行一维数组列表，请套入LineList
    """

    def __init__(self, data: Sequence[Sequence]):
        self.data = list(data)
        if len(data) == 0:
            print("data is empty")

    def get(self):
        return self.data

    def length(self) -> int:
        return len(self.data)

    def t(self):
        """转置"""
        pass

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

    def getColumn(self, index: int) -> list:
        """获取一列"""
        pass

    def insertRow(self, index: int, value: Sequence):
        """插入一行"""
        pass

    def insertColumn(self, index: int, value: Sequence):
        """插入一列"""
        pass

    def removeRow(self, index: int):
        """删除一行"""
        pass

    def removeColumn(self, index: int):
        """删除一列"""
        pass

    def replaceRow(self, index: int, value: Sequence):
        """替换一行"""
        pass

    def replaceColumn(self, index: int, value: Sequence):
        """替换一列"""
        pass

    def __eq__(self, other):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        return self.length()

    def __add__(self, other):
        pass

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

    def generateFigure(self):
        """生成多线折线图"""
        pass


class FlatList(_Flat):
    def __init__(self, data: Sequence[Sequence]):
        super().__init__(data)

    def t(self):
        self.data = list(zip(*self.data))
        self.data = [list(i) for i in self.data]
        return self

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


if __name__ == '__main__':
    a = FlatList([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24],
                  [25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36], [37, 38, 39], [40, 41, 42]])
    # a.t().print().printAll()
    b = FlatList(
        [(1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40), (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41),
         (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42)]
    )
