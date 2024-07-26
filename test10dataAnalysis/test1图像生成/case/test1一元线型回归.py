"""
一元线型回归示例

command
x = [1, 3, 5, 6, 8, 13, 14, 15, 19, 20]
y = [[12, 23, 34, 45, 56, 67, 78, 89, 90, 100],
    [13, 24, 35, 46, 57, 68, 79, 80, 102, 130],
    [14, 25, 36, 47, 58, 69, 80, 81, 103, 140]]
生成多元线型回归图像，每个点用*表示，x单位为mm，y单位为C，表头为“多元线型回归图像”
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义数据
x = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10, 13])  # 单位为m
y = np.array([12, 23, 34, 45, 56, 67, 78, 89, 90, 100])  # 单位为t

# 计算线性回归直线（此处仅作为示例，实际可能需要其他类型的回归分析）
m, b = np.polyfit(x, y, 1)  # 线性回归参数
print('线性回归参数：m =', m, 'b =', b)
# 生成回归线
regression_line = m * x + b
print('回归线：', regression_line)

# 绘制散点图及回归线
fig = plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data Points', marker='o')  # 使用'o'标记每个点
plt.plot(x, regression_line, 'r-', label='Regression Line')  # 绘制回归线

# 设置坐标轴标签和图例
plt.xlabel('Distance (m)')
plt.ylabel('Weight (t)')
plt.legend()

# 显示图形
plt.show()
