import pandas as pd
from pandas import Timestamp

t1 = Timestamp('2014-01-01 00:00:00')
h = 24
# 过了一天
t2 = t1 + pd.Timedelta(hours=23)
for i in pd.date_range(start=t1, end=t2, freq='h'):
    print(i)