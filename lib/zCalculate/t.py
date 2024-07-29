from matplotlib.colors import LinearSegmentedColormap
from sympy.physics.control.control_plots import matplotlib

from importBase import *
from excel import ExcelReader
from flatList import *

plt = importMatplotlib()


def hm():
    ex = ExcelReader(r'C:\Users\刘高瞻\Desktop\hotmap.xlsx').getSheetData('Sheet1')
    fl = FlatList(ex)
    xMonth = fl.getRow(0)[1:]
    yYear = fl.getColumn(0)[1:]
    data = fl[1, fl.row() - 1, 1, fl.col() - 1]
    FlatList(data).printAll()
    plt.figure(figsize=(16, 9))
    colors = [(0, '#e1eef7'),
              # (0.5, '#FFFF00'),
              (1, '#026db3')]
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    # plt.imshow(data, cmap=cmap, interpolation="none",)
    plt.pcolormesh(data, cmap=cmap,edgecolors='black', linewidth=1)
    plt.gca().set_aspect('equal')
    # plt.imshow(data, cmap='PiYG', interpolation="none")
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=28)
    plt.xticks(list(i+0.5 for i in range(12)), xMonth,fontsize=25)
    plt.yticks(list(i+0.5 for i in range(len(yYear))), yYear,fontsize=26)
    plt.xlabel('月份',fontsize=30)
    plt.ylabel('年份',fontsize=30)
    plt.xticks(rotation=45)
    # plt.title('生态流量保证率热图')
    # 标注数值
    # for i in range(len(data)):
    #     for j in range(len(data[0])):
    #         plt.text(j, i, f"{data[i][j]:.2f}", ha="center", va="center", color="blue")
    # plt.grid()
    plt.tight_layout()
    plt.savefig(r'C:\Users\刘高瞻\Desktop\hotmap.png', dpi=600)


def genQpPlot():
    # 画出Qp法图像保证流量图像
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, ]
    qm90 = [0.57, 0.44, 0.99, 0.98, 1.22, 1.63, 1.9, 1.85, 1.36, 0.96, 0.51, 0.51]
    qm95 = [0.17, 0.13, 0.29, 0.29, 0.36, 0.48, 0.56, 0.55, 0.4, 0.28, 0.15, 0.15]
    qy90 = [2.64, 2, 1.5, 1.57, 0.8, 0.87, 0.6, 1.16, 2.75, 1.26, 1.19, 0.2, 0.79, 1.3, 1.52]

    # qy95 =
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))
    ax1.plot(x, qm90, label='90%保证率', marker='o')
    ax1.plot(x, qm95, label='95%保证率', marker='o')
    ax1.set_xlabel('月份')
    ax1.set_ylabel('流量 m^3/s')
    ax1.set_title('Qp法计算各月生态流量')
    ax1.grid()
    ax1.legend()

    ax2.plot(y, qy90, label='90%保证率', marker='+')
    # ax2.plot(monthData.getYearSet(), qy95, label='Q year 95%', marker='+')
    ax2.set_xlabel('年份')
    ax2.set_ylabel('流量 m^3/s')
    ax2.set_title('Qp法计算各年生态流量')
    ax2.legend()
    ax2.grid()
    # plt.show()
    plt.savefig(r'C:\Users\刘高瞻\Desktop\line.png', dpi=600)
hm()