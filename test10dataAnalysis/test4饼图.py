"""
饼图

command:
x = ['A', 'B', 'C', 'D', 'E']
y = [300, 234, 561, 272, 105]
生成饼图，x为产品名称，y为销售数量，单位为个，表头为饼图，使用一种好看的渐变色风格
显示具体的值
要求饼图为标准的圆形
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('TkAgg')

# 定义产品名称和销售数量
x = ['A', 'B', 'C', 'D', 'E']
y = [300, 234, 561, 272, 105]

# 创建一个具有渐变色风格的标准圆形饼图
colors = plt.cm.get_cmap('Pastel1').colors

# 设置图形大小为正方形，保证饼图是标准圆形
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(y, labels=x, autopct=lambda p: f'{p:.1f}% ({int(round(p * sum(y) / 100))})', startangle=90, colors=colors)

# 设置饼图的中心文字（表头）
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('产品销售数量饼图')

# 调整图形为标准圆形
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# 配置并显示饼图
plt.legend(wedges, x, title='产品名称', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 显示百分比及具体值标签不重叠
for at in autotexts:
    at.set_size(8)
    at.set_color("black")

plt.show()