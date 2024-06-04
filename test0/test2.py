import numpy as np
from pandas import Timestamp
from lib.excel import *
import pandas as pd


class RawData:
    es = range(1, 46)  # 雨量站数据范围

    def __init__(self):
        self.data = {}
        for i in self.es:
            self.data[i] = SingleSheetExcelReader(f'rain/{i}.xlsx')

        self.timeSet = self._getTimeSet()
        self.outputData = self._createRawOutputData()
        self.__dealDuration()

    def _getTimeSet(self):  # 获取持续时间集合
        dates = []
        for i in self.es:
            d = np.array(self.data[i].getSheet()).T[0]
            dates += list(d)
        dates = list(set(dates))
        dates.sort()
        return dates

    def _createRawOutputData(self):  # 创建输出数据，数据全为0，后面加上
        first, last = self.timeSet[0], self.timeSet[-1]
        last = last.floor('h')
        last += pd.Timedelta(hours=5)
        timeSeries = pd.date_range(start=first, end=last, freq='h')
        outData = {}
        for i in timeSeries:
            outData[i] = [0] * len(self.es)
        return outData

    def __splitValue(self, t: Timestamp, h: float, duration: float):  # 处理持续时间
        timeStart = t.ceil('h')
        timeEnd = (t + pd.Timedelta(hours=duration)).ceil('h')
        timeSeries = pd.date_range(start=timeStart, end=timeEnd, freq='h')
        v = h / len(timeSeries) # TODO 暂时先平均分配每小时雨量
        values = {}
        for i in timeSeries:
            values[i] = v
        return values

    def __dealDuration(self):  # 处理时长，即去掉持续的时间
        for i in self.es:
            d = self.data[i]
            for j in range(len(d.getColumnData(1))):
                t, h, duration = d.getRowData(j + 1)
                if duration == 0:
                    continue
                values = self.__splitValue(t, h, duration)
                for k in values:
                    self.outputData[k][i - 1] += values[k]

    def SimplyOutputData(self):  # 简化数据，去掉整行都为0的数据
        simpleOutputData = []
        sites = map(lambda ii: f"{ii}th step", self.es)
        simpleOutputData.append(['time'] + list(sites))
        for i in self.outputData:
            if sum(self.outputData[i]) == 0:
                continue
            else:
                simpleOutputData.append([i] + self.outputData[i])
        return simpleOutputData

    def write(self):
        w = CsvWriter(self.SimplyOutputData())
        w.write()

    def __str__(self):
        return str(self.data)


rawData = RawData()
rawData.write()
