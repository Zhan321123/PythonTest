"""
两种图的结合


"""
import matplotlib
from matplotlib.ticker import NullLocator

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import host_subplot

plt.style.use('ggplot')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义数据
name = ['Pessl Instruments', 'Campbell Scientific', 'HWM-Water', 'Valarm', 'global average']
years = ['2019', '2020', '2021', '2022', '2023']
sales_prices = [
    [26.2, 29.4, 24.2, 25.8, 27.3],
    [15.6, 16.2, 15.4, 18.1, 17.7],
    [15.1, 19.7, 21.2, 20.5, 22.8],
    [14.2, 12.8, 12.6, 15.4, 13.1],
    [95.7, 101.4, 106.8, 111.6, 115.3]
]
sales_volumes = [
    [147, 153, 142, 150, 168],
    [163, 171, 181, 164, 172],
    [115, 106, 124, 130, 141],
    [131, 149, 152, 147, 132],
    [135, 148, 132, 147, 159],
]

# 绘制图像
fig, ax1 = plt.subplots()

# 分组柱状图（主图）
ax1.set_xlabel('年份', fontsize=20)
ax1.set_ylabel('销售单价（分组柱状图） - 元/天', fontsize=20)
ind = np.arange(len(years))
width = 0.18
for i, _ in enumerate(name):
    ax1.bar(ind + i * width - 0.3, sales_volumes[i], width, label=name[i], alpha=0.6)
# 设置属性
ax1.set_xticks(ind + width / 2)
ax1.set_xticklabels(years)
ax1.tick_params(labelsize=18)
ax1.set_ylim(bottom=80, top=220)

# 折线图（次图，共享x轴）
name = ['Pessl Instruments', 'Campbell Scientific', 'HWM-Water', 'Valarm', 'global sum']
ax2 = ax1.twinx()
ax2.set_ylabel('销售额（折线图） - 亿元', fontsize=20)
for i, product_name in enumerate(name):
    ax2.plot(years, sales_prices[i], label=product_name, marker='o')
# 设置属性
ax2.tick_params(axis='y', )
ax2.legend(loc='upper right', fontsize=18)
ax2.tick_params(labelsize=18)
ax2.set_ylim(top=140)

# 整体图像属性
plt.title('相关产品销售情况', fontsize=22)
plt.xticks(rotation=0)
plt.tight_layout()
plt.grid(True, axis='y')

plt.show()
