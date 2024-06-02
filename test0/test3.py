import numpy as np
from pandas import Timestamp
from lib.excel import *

A = SingleSheetExcelReader('water/A.xlsx', header=0)
B = SingleSheetExcelReader('water/B.xlsx', header=0)
rain = SingleSheetExcelReader('compound/雨量45站整合.xlsx', header=0)

date = []
wA1 = A.getColumnData(1)
wB1 = B.getColumnData(1)
rd1 = rain.getColumnData(1)
rd = []
wa = []
wb = []
for i in rd1:
    rd.append(str(i))
    print(str(i))
for i in wA1:
    wa.append(str(i))
    print(str(i))
for i in wB1:
    wb.append(str(i))
    print(str(i))

date += wa
date += wb
date += rd
date = list(set(date))
date.sort()

dddd = []
title = ['日期', '时间']
for i in range(1, 46):
    title.append(f'{i}站雨量')
    title.append(f'{i}站时长')
title += ['A站水位', 'A站流量', 'B站水位', 'B站流量']
dddd.append(title)

for i, t in enumerate(date):
    d = [*t.split(), ]
    if t in rd:
        d += rain.getRowData(rd.index(t) + 1)[1:]
    else:
        d += [0] * 90

    if t in wa:
        d.append(A.getCell(wa.index(t) + 1, 2))
        d.append(A.getCell(wa.index(t) + 1, 3))
    else:
        d += [0] * 2

    if t in wb:
        d.append(B.getCell(wb.index(t) + 1, 2))
        d.append(B.getCell(wb.index(t) + 1, 3))
    else:
        d += [0] * 2

    dddd.append(d)

cc = CsvWriter(dddd)
cc.write()
