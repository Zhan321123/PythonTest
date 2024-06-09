import pandas as pd
from pandas import Timestamp

t1 = Timestamp('2014-01-01 10:30:00')
t1 = t1.ceil('h')
print(t1)