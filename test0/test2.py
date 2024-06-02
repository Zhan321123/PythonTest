import numpy as np
from pandas import Timestamp
from lib.excel import *
import pandas as pd

# 读取CSV文件
df = pd.read_csv('雨量+水情整合.csv',encoding='gbk')

# 遍历每一列
for col in df.columns:
    # 检查列的数据类型
    if np.issubdtype(df[col].dtype, np.number):  # 如果是数值类型
        # 直接替换0为100
        df[col] = df[col].replace(0, '')
    else:  # 对于非数值类型（可能是字符串）
        try:
            # 尝试转换为浮点数并替换
            df[col] = pd.to_numeric(df[col], errors='coerce').replace(0.0, '')
        except Exception as e:
            print(f"Column {col} could not be converted to numeric: {e}")
            continue

df.to_csv('output.csv', index=False, encoding='gbk')