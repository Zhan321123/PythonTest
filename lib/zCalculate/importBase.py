# -*- coding: utf-8 -*-
"""
库导入类
"""
def importMatplotlib():
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文使用宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 英文使用Times New Roman
    return plt