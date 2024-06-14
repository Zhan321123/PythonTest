"""
将图插入到tkinter中

command:
x = [1, 2, 7, 3, 4, 5, 6, 8, 9, 10, 7, 3, 4, 5, 4, 8, 3]
y = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 7, 8, 9, 10, 1, 2, 3]
做散点图，x单位为m，y单位为K，并将图插入到tkinter的frame中

增加一个按钮，点击后x和y的数据打乱，然后散点图更新

要求的图像在frame中可以拖动，拖动方式也是matplotlib自带的扭转三维图像、放大图像等功能

将Matplotlib的缩放功能嵌入到Tkinter画布中
"""
import random

import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
# 定义初始数据
x = [1, 2, 7, 3, 4, 5, 6, 8, 9, 10, 7, 3, 4, 5, 4, 8, 3]
y = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 7, 8, 9, 10, 1, 2, 3]


def shuffle_data():
    global x, y
    random.shuffle(x)
    random.shuffle(y)
    update_plot()


def update_plot():
    ax.cla()  # 清除当前图像
    ax.scatter(x, y)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (K)')
    canvas.draw()


# 创建Tkinter窗口
root = tk.Tk()
root.title("Scatter Plot")

# 创建matplotlib Figure对象
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(x, y)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (K)')

# 将Figure转换为Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# 创建并配置button
shuffle_button = tk.Button(root, text="Shuffle Data", command=shuffle_data)
shuffle_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# 将canvas放置在Tkinter窗口上
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 将工具条嵌入在Tkinter窗口上
toolbar = NavigationToolbar2Tk(canvas, root)

# 启动主循环
tk.mainloop()
