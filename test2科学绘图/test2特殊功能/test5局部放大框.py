"""
局部放大


"""
import numpy as np
from matplotlib import cbook
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

# 图像
fig, ax = plt.subplots()
# 读取图像
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
# 创建空白图像
Z2 = np.zeros((150, 150))
# 填充空白图像
ny, nx = Z.shape
Z2[30:30 + ny, 30:30 + nx] = Z
extent = (-3, 4, -4, 3)
# 绘制图像
ax.imshow(Z2, extent=extent, origin="lower")

# 绘制子图像
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins = ax.inset_axes((0.5, 0.5, 0.47, 0.47),
                      xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
# 绘制子图像的框
ax.indicate_inset_zoom(axins, edgecolor="black")

plt.show()
