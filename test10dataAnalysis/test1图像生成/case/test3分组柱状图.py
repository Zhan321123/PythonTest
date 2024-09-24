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

ind = np.arange(len(x))  # 获取x坐标的初始范围
print(ind)
width = 0.25  # 条形图的宽度
groups = 3  # 分组的数量

for i, yy in enumerate(y):
    plt.bar(ind + i * width, yy, width=width, label=z[i])

plt.xticks(ind + width * groups / 2, x)  # 设置x轴刻度标签的位置和标签内容
plt.show()
