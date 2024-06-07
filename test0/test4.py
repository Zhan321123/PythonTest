import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# 假设你有一个包含时间（时间戳或序号）和值的DataFrame
from lib.excel import CsvReader, CsvWriter

data = np.array(CsvReader('雨量45+水情AB整合2.0.csv', header=0).getColumns([1, 0]))  # 示例数据，第一列时间，第二列值

# 转换为DataFrame，并将时间列转换为datetime类型
df = pd.DataFrame(data, columns=['time', 'value'])

df['value'] = df['value'].astype(float)

df['value'] = df['value'].replace(0, np.nan)

df['time'] = pd.to_datetime(df['time'])

# 使用PCHIP插值方法进行插值，它适用于非等距时间序列
df['value'] = df['value'].interpolate(method='nearest')

# 显示插值后的数据
w = CsvWriter(df.to_numpy().tolist())
w.write()
