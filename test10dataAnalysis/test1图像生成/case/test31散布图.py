"""
散布图
    https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py


"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = [5, 7, 8, 2, 1, 8, 2, 1, 3, 7, 2]
y = [9, 1, 2, 6, 3, 7, 2, 9, 1, 0, 2]
a = [100, 200, 326, 182, 173, 782, 347, 235, 163, 181, 865]
cmap = LinearSegmentedColormap.from_list('my_cmap', ['red', 'yellow', 'green'])
print(cmap(np.arange(cmap.N)))
colors = cmap(np.arange(cmap.N))[::int(256 / 11)][0:11]
print(colors)
plt.scatter(x, y, s=a, c=colors, alpha=0.5)
plt.show()
