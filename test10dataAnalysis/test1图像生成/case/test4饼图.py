"""
饼图
"""
from typing import Sequence

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')


def pieChart(ax: plt.Axes, xs: Sequence, ys: Sequence):
    """绘制普通饼图"""
    explode = [0] * (len(ys) - 1) + [0.2]
    wedges, texts, autotexts = ax.pie(ys, autopct=lambda p: f'{p:.1f}%',
                                      startangle=90,  # 旋转角度
                                      shadow=True,  # 显示阴影
                                      explode=explode, )  # 突出
    ax.axis('equal')  # 调整图形为标准圆形
    ax.legend(wedges, xs, title='legend')
    ax.set_title('pie chart')


def stackPieChart(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """绘制堆叠饼图"""
    width = 0.3
    radius = 0.7 + width * len(yss)
    for index, i in enumerate(yss):
        ax.pie(i, radius=radius, autopct='%1.1f%%', pctdistance=1 - width / radius / 2)
        radius -= width
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')  # 设置饼图的中心为空缺
    ax.add_artist(centre_circle)
    ax.axis('equal')
    ax.legend(xs, title='legend')
    ax.set_title('stack pie chart')


if __name__ == '__main__':
    fig, axs = plt.subplots(1, 2)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # 调整子图间距

    x = ['A', 'B', 'C', 'D', 'E']
    y1 = [300, 234, 561, 272, 105]
    y2 = [[234, 561, 272, 105, 300],
          [300, 234, 561, 272, 105],
          [274, 344, 172, 405, 100]]

    pieChart(axs[0], x, y1)
    stackPieChart(axs[1], x, y2)

    plt.show()
