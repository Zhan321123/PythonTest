from typing import Sequence
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

from lib.excel import *


class LineData:
    def __init__(self, data: Sequence[float]):
        self.data = list(data)

    def getData(self):
        return self.data

    def replace(self, old, new):
        for index, i in enumerate(self.data):
            if i == old:
                self.data[index] = new
        return self

    def interpolate0(self):
        npData = np.array(self.data)
        x = np.nonzero(npData)[0]
        y = npData[x]
        f = interp1d(x, y, kind='linear', bounds_error=False, fill_value=(y[0], y[-1]))
        x = np.arange(len(npData))
        self.data = f(x).tolist()
        return self

    def toSet(self):
        self.data = list(set(self.data))
        return self

    def tolist(self):
        return self.data

    def sort(self, reverse=False):
        self.data.sort(reverse=reverse)
        return self

    def __str__(self):
        return str(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __add__(self, other: Sequence):
        self.data += list(other)
        return self


class SheetData:

    def __init__(self, sheetData: Sequence[Sequence]):
        self.data = []
        for i in sheetData:
            self.data.append(list(i))

    def getData(self):
        return self.data

    def T(self):
        self.data = SheetData(zip(*self.data))
        return self

    def replaceRow(self, row: int, old, new):
        if row >= len(self.data):
            print("row out of range")
        for index, i in enumerate(range(len(self.data[row]))):
            if i == old:
                self.data[row][index] = new
        return self

    def interpolateRow(self, row: int):
        if row >= len(self.data):
            print("row out of range")
        line = LineData(self.data[row])
        line.interpolate0()
        self.data[row] = line.getData()
        return self

    def insertRow(self, data: Sequence, row: int = None):
        if row is None:
            row = len(self.data)
        self.data.insert(row, list(data))

    def insertCol(self, data: Sequence, col: int = None):
        for i in range(len(self.data)):
            if col is None:
                self.data.append(data[i])
            else:
                self.data[i].insert(col, data[i])

    def getRow(self, row: int):
        if row >= len(self.data):
            print("row out of range")
        return self.data[row]

    def getRows(self, rows: Sequence[int]):
        if max(rows) >= len(self.data):
            print("row out of range")
        return [self.data[i] for i in rows]

    def getCol(self, col: int):
        if col >= len(self.data[0]):
            print("col out of range")
        return [self.data[i][col] for i in range(len(self.data))]

    def getCols(self, cols: Sequence[int]):
        if max(cols) >= len(self.data):
            print("col out of range")
        return [self.data[i] for i in cols]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def toList(self):
        return list(self.data)

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    l = LineData([0, 1, 11, 0, 0, 11, 0, 0, 0, 55, 9, 0, 3, 0])
    l.interpolate0()
    print(l)
    pass
