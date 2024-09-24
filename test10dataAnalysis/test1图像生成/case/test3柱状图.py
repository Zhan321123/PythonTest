"""
柱状图

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 前提
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
x = ['A', 'B', 'C', 'D', 'E']
y = [300, 234, 561, 272, 105]

# 创建图形
fig, ax = plt.subplots(facecolor='lightgrey')

# 绘制柱状图
bars = ax.bar(x, y, color='green', edgecolor='red', hatch='/')

# 在每个柱子上方添加数值标注
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{height}', ha='center', va='bottom')

# 设置图表标题和坐标轴标签
plt.title('柱状图 - 地区高度比较')
ax.tick_params(axis='both', colors='white')
# ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.xlabel('地名')
plt.ylabel('高度（m）')

plt.show()
