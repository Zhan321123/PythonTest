from typing import Sequence
import numpy as np

from lib.zCalculate.importBase import importMatplotlib

plt = importMatplotlib()


def groupBar(ax: plt.Axes, xs: Sequence, yss: Sequence[Sequence]):
    """绘制分组柱状图"""
    width = 0.12
    labels = ["Qp法", "Texas法", "最小月平均径流法", "累计频率曲线法", "Tennant法", "最终生态流量"]
    ind = np.arange(len(xs))
    for i, ys in enumerate(yss):
        b = ax.bar(ind + i * width, ys, width=width, )
        ax.bar_label(b, label_type='center')  # 在每个柱子中间添加数值标注
    ax.set_xticks(ind + width * (len(yss) - 1) / 2, xs)
    ax.set_xlabel('水库')
    ax.set_ylabel('流量 $m^3/s$')
    ax.grid()
    ax.legend(labels=labels)


y2 = [[2.666, 3.160, 0.6760],
      [1.458, 1.464, 0.343],
      [1.343, 1.167, 0.237],
      [0.903, 0.788, 0.002],
      [3.129, 3.149, 0.847],
      [2.098, 2.282, 0.438]]

x = ["下岸水库", "里石门水库", "龙溪水库"]
plt.figure(figsize=(16, 9))
groupBar(plt.gca(), x, y2)
# plt.show()
plt.savefig(r'C:\Users\刘高瞻\Desktop\生态流量计算值.png', dpi=600)
