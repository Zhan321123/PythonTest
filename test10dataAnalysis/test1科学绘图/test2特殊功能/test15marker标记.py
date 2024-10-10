"""
标记类型
"""
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.lines as mlines

matplotlib.use("TkAgg")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def showAllMarkers(ax: plt.Axes):
    """展示所有官方标记"""
    x, y = 0, 0
    import matplotlib.lines as mlines
    ms = mlines.Line2D.markers  # 所有标记类型
    for marker in ms:
        ax.plot(x, y, marker=marker, markersize=12)
        ax.text(x, y + 0.14, marker, ha='center', fontsize=8)
        x += 1
        if x > 8:
            x = 0
            y += 1


def showSpecialMarkers(ax: plt.Axes):
    """展示特殊标记"""
    xs = [1, 2, 3, 4]
    # 空心标记，手动的方法
    ax.plot(xs, [1, 2, 3, 4], label='空心标记', marker='o',  # 标记样式
            markerfacecolor='none',  # 标记内部颜色
            markeredgecolor='r',  # 标记边框的颜色
            markeredgewidth=1,  # 标记边框的宽度
            markersize=10)  # 标记的大小
    # 官方提供的填充样式
    fs = mlines.Line2D.fillStyles
    for i, f in enumerate(fs):
        ax.plot(i, i + 1, label=f'填充样式-{f}', marker='o', fillstyle=f)
    # TeX 符号的标记，用 '$...$'
    ax.plot(xs, [4, 5, 6, 7], label='TeX符号标记', marker='$?$')
    ax.plot(xs, [5, 6, 7, 8], label='TeX符号标记', marker='$M$')
    ax.legend()


if __name__ == '__main__':
    print("所有标记类型:", mlines.Line2D.markers)
    print("填充样式:", mlines.Line2D.fillStyles)

    fig, axs = plt.subplots(1, 2)
    showAllMarkers(axs[0])
    showSpecialMarkers(axs[1])

    plt.show()
