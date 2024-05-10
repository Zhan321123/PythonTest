"""
分组柱状图

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['2020', '2021', '2022', '2023']
y = [[10, 20, 30, 40], [20, 30, 40, 50, ], [34, 12, 26, 76]]
z = ["product1", "product2", "product3"]

# 使用numpy的repeat和arange函数扩展x坐标以适应每组条形图
ind = np.arange(len(x))  # 获取x坐标的初始范围
print(ind)
width = 0.25  # 条形图的宽度
groups = len(y)  # 分组的数量

for i, yy in enumerate(y):
    plt.bar(ind + i * width, yy, width, label=z[i])

plt.xticks(ind + width * groups / 2, x)  # 设置x轴刻度标签的位置和标签内容
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Grouped Bar Chart')
plt.legend(title='Groups')

# --------------------------------------

species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

# --------------------------------
plt.show()
