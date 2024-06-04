import pandas as pd
from objprint import objprint

t = pd.Timestamp('2021-01-01 09:30:50')
x = 0.3

print(t.time().hour)
print(t.time().minute)
print(t.time().second)

duration = 0.5

timeStart = t.ceil('h')
timeEnd = (t + pd.Timedelta(hours=duration)).ceil('h')

print(timeStart,timeEnd)

# 获取相差的小时
print((timeEnd-timeStart).total_seconds()/3600)