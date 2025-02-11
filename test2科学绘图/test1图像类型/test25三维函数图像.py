"""
三维函数图像

本例画 z=x^2+y^2 的函数图像
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')
# 1. 定义数据网格范围和分辨率
x_min, x_max = -20, 20
y_min, y_max = -20, 20
resolution = 60

x = np.linspace(x_min, x_max, resolution)
y = np.linspace(y_min, y_max, resolution)
X, Y = np.meshgrid(x, y)

# 2. 计算函数值
# Z = X ** 2 + Y ** 2
Z = (np.sin(X)+np.cos(Y))/2
# Z = np.cos(X + Y)

# 3. 创建三维坐标系并设置视图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 4. 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)

# 5. 添加轴标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('f(x,y,z)')

# 6. 显示图形
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
