"""
堆积条形柱状图


"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# 创建数据
x = np.arange(5)
y1 = [10, 20, 30, 40, 50]
y2 = [5, 10, 15, 20, 25]
y3 = [2, 4, 6, 8, 10]
# 创建图形
fig = plt.figure()
ax = fig.add_subplot(111)
# 绘制堆积条形图
ax.bar(x, y1, label='y1')
ax.bar(x, y2, bottom=y1, label='y2')
ax.bar(x, y3, bottom=np.array(y1)+np.array(y2), label='y3')
ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
ax.legend()
plt.show()
