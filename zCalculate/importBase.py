# -*- coding: utf-8 -*-
"""
库导入类
"""
def importMatplotlib():
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    matplotlib.rcParams['axes.unicode_minus'] = False
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    return plt