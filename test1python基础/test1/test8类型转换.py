"""
float, int, str, bool 类型转换
"""
import numpy as np

# float类型转换
try:
    # f = float(1) # 1.0
    # f = float('1') # 可1.0
    # f = float('1.1') # 1.1
    # f = float(None) # 报错
    # f = float('1.1a') # 报错
    # f = float('inf') # inf
    # f = float('-inf') # -inf
    # f = float(np.inf)  # inf
    # f = float('nan') # nan
    # f = float(np.nan)  # nan
    # f = float(True) # 1.0
    # f = float(False) # 0.0
    # f = float('a') # 报错
    f = float() # 0.0
    print('转为了:', f)
except Exception as e:
    print('error:', e)

# int类型转换
try:
    # i = int(1) # 1
    # i = int('1') # 1
    # i = int(1.1) # 1
    # i = int(1.9999) # 1
    # i = int(True) # 1
    # i = int(False) # 0
    # i = int('a') # 报错
    # i = int(None) # 报错
    # i = int('1a') # 报错
    # i = int('1.1') # 报错
    # i = int('inf') # 报错
    # i = int('nan') # 报错
    # i = int(np.nan) # 报错
    # i = int(np.inf) # 报错
    i = int() # 0
    print('转为了:', i)
except Exception as e:
    print('error:', e)

# str类型转换
try:
    # s = str(1) # '1'
    # s = str(1.1) # '1.1'
    # s = str(True) # 'True'
    # s = str(False) # 'False'
    # s = str(None) # 'None'
    # s = str('a') # 'a'
    # s = str([1,2]) # '[1, 2]'
    # s = str(np.nan) # 'nan'
    # s = str(np.inf) # 'inf'
    s = str() # ''
    print('转为了:', s)
except Exception as e:
    print('error:', e)

# bool类型转换
# 数字非0即True，序列非空即True
try:
    # b = bool(1) # True
    # b = bool(1.1) # True
    # b = bool(0) # False
    # b = bool(0.0) # False
    # b = bool(None) # False
    # b = bool('') # False
    # b = bool('a') # True
    # b = bool([]) # False
    # b = bool([1]) # True
    # b = bool(np.nan) # False
    # b = bool(np.inf) # True
    # b = bool(True) # True
    b = bool() # False
    print('转为了:', b)
except Exception as e:
    print('error:', e)
