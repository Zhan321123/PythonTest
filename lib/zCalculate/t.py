import numpy as np

from flatList import *

plt = importMatplotlib()

# from matplotlib.colors import LinearSegmentedColormap
# from excel import ExcelReader
# def hm():
#     ex = ExcelReader(r'C:\Users\刘高瞻\Desktop\hotmap.xlsx').getSheetData('Sheet1')
#     fl = FlatList(ex)
#     xMonth = fl.getRow(0)[1:]
#     yYear = fl.getColumn(0)[1:]
#     data = fl[1, fl.row() - 1, 1, fl.col() - 1]
#     FlatList(data).printAll()
#     plt.figure(figsize=(16, 9))
#     colors = [(0, '#e1eef7'),
#               # (0.5, '#FFFF00'),
#               (1, '#026db3')]
#     cmap = LinearSegmentedColormap.from_list('custom', colors)
#     # plt.imshow(data, cmap=cmap, interpolation="none",)
#     plt.pcolormesh(data, cmap=cmap,edgecolors='black', linewidth=1)
#     plt.gca().set_aspect('equal')
#     # plt.imshow(data, cmap='PiYG', interpolation="none")
#     cb = plt.colorbar()
#     cb.ax.tick_params(labelsize=28)
#     plt.xticks(list(i+0.5 for i in range(12)), xMonth,fontsize=25)
#     plt.yticks(list(i+0.5 for i in range(len(yYear))), yYear,fontsize=26)
#     plt.xlabel('月份',fontsize=30)
#     plt.ylabel('年份',fontsize=30)
#     plt.xticks(rotation=45)
#     # plt.title('生态流量保证率热图')
#     # 标注数值
#     # for i in range(len(data)):
#     #     for j in range(len(data[0])):
#     #         plt.text(j, i, f"{data[i][j]:.2f}", ha="center", va="center", color="blue")
#     # plt.grid()
#     plt.tight_layout()
#     plt.savefig(r'C:\Users\刘高瞻\Desktop\hotmap.png', dpi=600)


def genQpPlot():
    # 画出Qp法图像保证流量图像
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, ]
    qm900 = [0.57, 0.44, 0.99, 0.98, 1.22, 1.63, 1.9, 1.85, 1.36, 0.96, 0.51, 0.51]
    qm901 = [0.17, 0.13, 0.79, 1.29, 2.36, 2.48, 2.56, 1.55, 1.45, 1.28, 1.15, 1.15]
    qm902 = [0.62, 1.16, 1.15, 1.16, 2.25, 2.35, 1.45, 1.68, 1.55, 1.38, 0.55, 0.64]
    qm903 = [0.27, 0.11, 1.25, 1.40, 2.33, 1.23, 2.42, 2.44, 2.43, 1.33, 1.22, 1.32]

    qy900 = [0.64, 2.00, 1.50, 1.57, 0.8, 0.87, 0.6, 1.16, 2.75, 1.26, 1.19, 0.2, 0.79, 1.3, 1.52]
    qy901 = [1.64, 1.22, 1.53, 2.17, 1.89, 1.87, 1.60, 1.56, 1.75, 1.66, 1.89, 1.04, 0.89, 0.52, 0.53]
    qy902 = [1.43, 1.90, 1.65, 1.88, 2.01, 2.78, 2.66, 2.16, 2.95, 2.26, 2.19, 2.20, 1.79, 1.70, 1.22]
    qy903 = [2.00, 1.45, 1.32, 1.57, 1.33, 2.07, 1.32, 1.01, 1.97, 2.06, 2.22, 1.33, 1.36, 1.56, 0.99]

    titleSize = 18
    legendSize = 14
    tickSize = 14
    labelSize = 16

    # qy95 =
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    ax1.plot(x, qm901, label='里石山水库', marker='o')
    ax1.plot(x, qm900, label='龙溪水库', marker='*')
    ax1.plot(x, qm902, label='下岸水库', marker='+')
    ax1.plot(x, qm903, label='牛头山水库', marker='*')
    # 将刻度值字符大小设置为20
    ax1.set_xticks(x, x)
    ax1.tick_params(axis='both', which='major', labelsize=tickSize)
    ax1.set_xlabel('月份', fontsize=labelSize)
    ax1.set_ylabel('流量 m$^3$/s',fontsize=labelSize)
    ax1.set_title('Qp法计算各月生态流量', fontsize=titleSize)
    # 显示更多刻度
    ax1.set_ylim(0, 2.7)
    ax1.set_yticks(np.arange(0,3,0.3))
    ax1.grid()
    ax1.legend(fontsize=legendSize)

    ax2.plot(y, qy900, label='里石山水库', marker='o')
    ax2.plot(y, qy901, label='龙溪水库', marker='*')
    ax2.plot(y, qy902, label='下岸水库', marker='+')
    ax2.plot(y, qy903, label='牛头山水库', marker='*')
    # ax2.plot(monthData.getYearSet(), qy95, label='Q year 95%', marker='+')
    ax2.set_xlabel('年份(20**年)',fontsize=labelSize)
    ax2.set_xticks(y, y)
    # 旋转45度
    ax2.set_xticklabels((f"{i}"[2:] for i in y))
    # ax2.set_xticklabels(y, rotation=45)
    ax2.set_ylabel('流量 m$^3$/s',fontsize=labelSize)
    ax2.tick_params(axis='both', which='major', labelsize=tickSize)
    ax2.set_title('Qp法计算各年生态流量', fontsize=titleSize)
    ax2.legend(fontsize=legendSize)
    # 显示更多刻度
    ax2.set_ylim(0, 3)
    ax2.set_yticks(np.arange(0,3.3,0.3))
    ax2.grid()
    # plt.show()
    plt.savefig(r'C:\Users\刘高瞻\Desktop\line.png', dpi=600)
genQpPlot()