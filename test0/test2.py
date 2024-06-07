import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator
from matplotlib.ticker import MaxNLocator
from pandas import Timestamp
from lib.excel import *
import pandas as pd

matplotlib.use('Qt5Agg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class RawData:
    es = range(1, 46)  # 雨量站数据范围

    def __init__(self):
        self.rainData = {}  # 雨量站数据
        self.waterData = {}  # 水情站数据

        for i in self.es:
            self.rainData[i] = SingleSheetExcelReader(f'rain/{i}.xlsx')
        self.waterData['A'] = SingleSheetExcelReader('water/A.xlsx')
        self.waterData['B'] = SingleSheetExcelReader('water/B.xlsx')

        self.timeSet = self._getTimeSet()
        self.outputData = self._createRawOutputData()
        self.__dealDuration()
        self.__dealWater()

    def _getTimeSet(self):  # 获取持续时间集合
        dates = []
        for i in self.es:
            d = np.array(self.rainData[i].getSheet()).T[0]
            dates += list(d)
        dates += list(np.array(self.waterData['A'].getSheet()).T[0])
        dates += list(np.array(self.waterData['B'].getSheet()).T[0])

        dates = list(set(dates))
        dates.sort()
        return dates

    def _createRawOutputData(self):  # 创建输出数据，数据全为0，后面加上
        self.first, last = self.timeSet[0], self.timeSet[-1]
        self.last = last.floor('h')
        self.last += pd.Timedelta(hours=5)
        self.timeSeries = pd.date_range(start=self.first, end=self.last, freq='h')
        outData = {}
        for i in self.timeSeries:
            outData[i] = [0] * (len(self.es)+4)
        return outData

    def __splitValue(self, t: Timestamp, h: float, duration: float):  # 处理持续时间
        timeStart = t.ceil('h')
        timeEnd = (t + pd.Timedelta(hours=duration)).ceil('h')
        timeSeries = pd.date_range(start=timeStart, end=timeEnd, freq='h')
        v = h / len(timeSeries)  # TODO 暂时先平均分配每小时雨量
        values = {}
        for i in timeSeries:
            values[i] = v
        return values

    def __dealDuration(self):  # 处理时长，即去掉持续的时间
        for i in self.es:
            d = self.rainData[i]
            for j in range(len(d.getColumnData(1))):
                t, h, duration = d.getRowData(j + 1)
                if duration == 0:
                    continue
                values = self.__splitValue(t, h, duration)
                for k in values:
                    self.outputData[k][i - 1] += values[k]

    def __dealWater(self):  # 处理水情数据
        dates = self.waterData['A'].getColumnData(1)
        for i in dates:
            j = i.ceil('h')
            l,f = list(self.waterData['A'].getRowData(dates.index(i) + 1)[1:])
            self.outputData[j][45]=l
            self.outputData[j][46]=f
        dates = self.waterData['B'].getColumnData(1)
        for i in dates:
            j = i.ceil('h')
            l, f = list(self.waterData['B'].getRowData(dates.index(i) + 1)[1:])
            self.outputData[j][47]=l
            self.outputData[j][48]=f

    def generateRainCurve(self):
        sum1 = {}  # y-m-d h:00:00 对应所有站的雨量
        for index, i in enumerate(self.outputData):
            sum1[index] = sum(self.outputData[i])
        sum2 = {}  # y-m-d 对应所有站的雨量
        dateRange = 24
        for i in range(len(sum1) // dateRange):
            v = 0
            for j in range(dateRange):
                try:
                    v += sum1[i + j]
                except IndexError:
                    break
            sum2[i] = v
        sum3 = {}
        for i in range(len(sum2)):
            v = 0
            for j in range(-4, 5):
                if i + j >= 0 & i + j < len(sum2) - 1:
                    print(i + j, sum2[i + j])
                    v += sum2[i + j]
            sum3[self.timeSeries[i * dateRange]] = v
        self.generateCurve(sum3)

    def generateCurve(self, data: dict):
        fig = plt.figure()
        plt.plot(list(data.keys()), list(data.values()))
        plt.ylim(0)
        plt.xlim(self.first, self.last)
        plt.gca().xaxis.set_major_formatter(DateFormatter('%yy-%mm-%dd'))
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=50))
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

    def SimplyOutputData(self):  # 简化数据，去掉整行都为0的数据
        simpleOutputData = []
        sites = map(lambda ii: f"{ii}stop", self.es)
        simpleOutputData.append(['time'] + list(sites) + ['A-Level','A-Flow', 'B-Level', 'B-Flow'])
        for i in self.outputData:
            if sum(self.outputData[i]) == 0:
                continue
            else:
                simpleOutputData.append([i,] + self.outputData[i])
        return simpleOutputData

    def write(self):  # 写入csv文件
        w = CsvWriter(self.SimplyOutputData())
        w.write()

    def __str__(self):
        return str(self.rainData)


rawData = RawData()
rawData.write()
