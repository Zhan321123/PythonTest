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
    """绘制饼图"""
    wedges, texts, autotexts = ax.pie(ys, labels=xs, autopct=lambda p: f'{p:.1f}%', startangle=90)
    # 设置饼图的中心为空缺
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    ax.axis('equal')  # 调整图形为标准圆形
    ax.legend(wedges, xs, title='legend')
    ax.set_title('pie chart')


if __name__ == '__main__':
    x = ['A', 'B', 'C', 'D', 'E']
    y = [300, 234, 561, 272, 105]

    fig, axs = plt.subplots(1, 2)
    pieChart(axs[0], x, y)

    plt.show()
