"""
matplotlib marker标记类型:
    {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up', '<': 'triangle_left',
     '>': 'triangle_right', '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon',
     's': 'square', 'p': 'pentagon', '*': 'star', 'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus', 'x': 'x',
     'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline', 'P': 'plus_filled', 'X': 'x_filled',
     0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup',
     7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase',
     'None': 'nothing', 'none': 'nothing', ' ': 'nothing', '': 'nothing'}

让标记为空心的方法，设置参数:
    markerfacecolor='none',
    markeredgecolor='r',
    markeredgewidth=1

"""
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")

# 所有标记类型
import matplotlib.lines as mlines

print("所有标记类型:")
print(mlines.Line2D.markers)

fig, ax = plt.subplots(2, 2)

# 让标记为空心的方法
ax[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16], label='$y=x^2$', marker='*',
              markerfacecolor='none',
              markeredgecolor='r',
              markeredgewidth=1)

x, y = 0, 0
ms = mlines.Line2D.markers
for marker in ms:
    ax[1, 1].plot(x, y, marker=marker)
    ax[1, 1].text(x, y + 0.3, marker, ha='center', fontsize=8)
    x += 1
    if x > 8:
        x = 0
        y += 1

plt.show()
