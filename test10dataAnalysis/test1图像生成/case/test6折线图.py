"""
折线图

data的key为日期，value为数量
要求图上标上数据
由于日期字符太长，斜着写
"""
import pyarrow
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = {
    "2019-01-01": 156,
    "2019-01-02": 167,
    "2019-01-03": 156,
    "2019-01-04": 189,
    "2019-01-05": 167,
    "2019-01-06": 189,
    "2019-01-07": 200,
    "2019-01-08": 189,
    "2019-01-09": 156,
    "2019-01-10": 124,
    "2019-01-11": 180,
    "2019-01-12": 249
}


# 将数据转换为pandas DataFrame以方便处理日期
df = pd.DataFrame.from_dict(data, orient='index').reset_index()
df.columns = ['date', 'quantity']

# 转换日期字符串为datetime对象
df['date'] = pd.to_datetime(df['date'])

# 创建图形
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df['date'], df['quantity'], marker='o', linestyle='-')

# 在每个点上标注数值
for x, y in zip(df['date'], df['quantity']):
    ax.annotate(f'{y}', xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom')

# 设置x轴为日期格式
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

# 添加标题和坐标轴标签
plt.title("Daily Quantity Over Time")
plt.xlabel("Date")
plt.ylabel("Quantity")

plt.xticks(rotation=45)

# 显示图形
plt.show()