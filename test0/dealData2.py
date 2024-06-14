"""
evaporation data, rain data, water data's dealing

please
    1. put file in dir named "evaporation","rain","water"
    2.
"""
import numpy as np
import pandas as pd
from pandas import Timestamp
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from lib.excel import CsvReader, CsvWriter
from lib.sheetData import *


class DealWithData:
    rawData = {  # 原始数据
        'rain': {},
        'water': {},
        'evaporate': {}
    }
    # 数据范围
    rainRange = list(str(i) + 'rain' for i in range(1, 46))
    waterRange = ("A", "B")
    evaporateRange = list(str(i) + 'evaporate' for i in range(1, 7))
    dealWaterRange = ["A-H", "A-Q", "B-H", "B-Q"]

    dealData = {}  # 处理后的数据
    outputData = {}  # 输出的数据

    dateStart = Timestamp(2007, 1, 1, 0, 0, 0)  # 时间范围
    dateEnd = Timestamp(2014, 1, 1, 0, 0, 0)

    def __init__(self):
        for i in self.rainRange:
            self.rawData['rain'][i] = SheetData(SingleSheetExcelReader(f'rain/{i[0]}.xlsx', header=0).getSheet())
        for i in self.waterRange:
            self.rawData['water'][i] = SheetData(SingleSheetExcelReader(f'water/{i}.xlsx', header=0).getSheet())
        for i in self.evaporateRange:
            self.rawData['evaporate'][i] = SheetData(
                SingleSheetExcelReader(f'evaporation/{i[0]}.xlsx', header=0).getSheet())

        self.timeSeries = pd.date_range(start=self.dateStart, end=self.dateEnd, freq='h')  # 时间范围序列
        for i in self.timeSeries:
            self.dealData[i] = {j: 0 for j in (self.rainRange + self.dealWaterRange + self.evaporateRange)}
        self.__dealRain()
        self.__dealWater()
        self.__dealEvaporate()

    def _getTimeSet(self):  # 获取持续时间集合
        dates = LineData([])
        for i in self.rainRange:
            dates += self.rawData['rain'][i].T()[0]
        for i in self.waterRange:
            dates += self.rawData['water'][i].T()[0]

        return dates.toSet().sort()

    def __dealRain(self):  # 处理雨量1-45站数据
        def __splitValue(t: Timestamp, h: float, duration: float):  # 整合持续时长，拆分雨量
            if duration == 0 or h == 0:
                return {}
            timeStart = t.ceil('h')
            timeEnd = (t + pd.Timedelta(hours=duration)).ceil('h')
            timeSeries = pd.date_range(start=timeStart, end=timeEnd, freq='h')

            values = {}
            for i in timeSeries:
                values[i] = h / len(timeSeries)  # TODO 暂时先平均分配每小时雨量
            return values

        for i in self.rainRange:
            d = self.rawData['rain'][i]
            for t, h, duration in d:
                values = __splitValue(t, h, duration)
                for k in values:
                    self.dealData[k][i] += values[k]

    def __dealWater(self):  # 处理水情数据
        sheet = self.rawData['water']['A']
        for t, h, q in sheet:
            t = t.ceil('h')
            self.dealData[t]["A-H"] = h
            self.dealData[t]["A-Q"] = q
        sheet = self.rawData['water']['B']
        for t, h, q in sheet:
            t = t.ceil('h')
            self.dealData[t]["B-H"] = h
            self.dealData[t]["B-Q"] = q

    def __dealEvaporate(self):  # 处理蒸发1-6站数据
        def __evaporateDivide(yy, mm, dd, hh: float):  # 分配每日的蒸发量
            if hh == 0:
                return {}
            t = Timestamp(year=yy, month=mm, day=dd)

            v = hh / 24  # TODO 暂时先平均分配每日蒸发量
            return {ii: v for ii in pd.date_range(start=t, end=t + pd.Timedelta(hours=23), freq='h')}

        for i in self.evaporateRange:
            for y, m, d, h in self.rawData['evaporate'][i]:
                values = __evaporateDivide(y, m, d, h)
                for k in values:
                    self.dealData[k][i] = values[k]

    def output(self):  # 输出数据表格csv
        output = []
        for i in self.timeSeries:
            output.append([i, ] + list(self.dealData[i].values()))
        s = SheetData(output).T()
        # for i in [46, 47, 48, 49]:
        for i in range(len(self.rainRange)+1, len(self.rainRange)+len(self.dealWaterRange)+1):
            s[i] = LineData(s[i]).interpolate0().tolist()
        output = s.T().toList()
        output.insert(0, ['date time'] + self.rainRange + self.dealWaterRange + self.evaporateRange)
        print(output)
        w = CsvWriter(output)
        w.write()


dddd = DealWithData()
dddd.output()
