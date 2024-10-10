"""
添加水印


"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# file = r"../file/logo.png"

with cbook.get_sample_data(r"D:\code\pythonProject\PythonTest\test10dataAnalysis\test1图像生成\file\logo.png") as file:
    im = image.imread(file)

fig, ax = plt.subplots()

x = np.arange(30)
ax.bar(x, x)
ax.grid()

fig.figimage(im,200,20,zorder=3, alpha=.3)

plt.show()