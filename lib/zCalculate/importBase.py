# -*- coding: utf-8 -*-
"""
库导入类
"""


def importMatplotlib():
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg')
    plt.rcParams.update({
        'axes.unicode_minus': False,  # 正确显示负号
        'font.sans-serif': 'SimSun',  # 中文使用宋体
        'font.serif': 'Times New Roman',  # 英文使用Times New Roman
        'axes.titlesize': 18,  # 标题字体大小
        'legend.fontsize': 14,  # 图例字体大小
        'xtick.labelsize': 14,  # X轴刻度字体大小
        'ytick.labelsize': 14,  # Y轴刻度字体大小
        'axes.labelsize': 16,  # 轴标签字体大小
        # 'figure.figsize': (16, 9),   # 图形大小
        # 'lines.linewidth': 2,        # 线宽
        'lines.markersize': 8,  # 标记大小
        # 'font.family': 'Arial',      # 字体家族
        # 'grid.linestyle': '--',      # 网格线样式
        'font.size': 15,  # 默认字体大小，通常为text()方法中的字体大小
        'grid.color': 'gray',  # 网格颜色
        'grid.linewidth': 0.5,  # 网格线宽度
        'axes.facecolor': 'white',  # 轴背景色
        'figure.facecolor': 'white'  # 图形背景色
    })
    # plt.grid()
    return plt
