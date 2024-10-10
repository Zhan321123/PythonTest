"""
将matplotlib常规设置封装为函数并返回plt
"""


def importMatplotlib():
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('TkAgg') # 在不兼容的终端上使用python自带的窗口展示
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文使用 宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 英文使用 Times New Roman
    plt.rcParams['image.cmap'] = 'rainbow' # 默认颜色方案为 rainbow
    plt.style.use('Solarize_Light2') # 根据需要使用图像风格
    plt.rcParams.update({
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
        # 'axes.facecolor': 'white',  # 轴背景色
        # 'figure.facecolor': 'white',  # 图形背景色
    })
    return plt

if __name__ == '__main__':
    plt = importMatplotlib()
    plt.plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36], label='line', marker='o')
    plt.bar([1, 2, 3, 4, 5, 6], [6, 2, 4, 6, 1, 2], label='bar')
    plt.text(2, 15, 'Text')
    plt.title('Sample Plot')
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    plt.legend()
    plt.show()
