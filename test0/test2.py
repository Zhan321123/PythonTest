import numpy as np
from pandas import Timestamp
from lib.excel import *
import pandas as pd

class RawData:
    es = range(1,46)
    def __init__(self):
        self.data = {}
        for i in self.es:
            self.data[i] = np.array(SingleSheetExcelReader(f'rain/{i}.xlsx').getSheet())

        self.outData = {}
        self.timeSet = self.getTimeSet()

    def getTimeSet(self):
        dates = []
        for i in self.es:
            dates += list(self.data[i].T[0])
        dates = list(set(dates))
        dates.sort()
        return dates

    def createRawOutputData(self):
        first,last = self.timeSet[0],self.timeSet[-1]


    def __str__(self):
        return str(self.data)

rawData = RawData()