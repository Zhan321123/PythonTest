"""
条形码

暂不妙
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

text = "Hello, World! python is a shit language! dont use python write game!" \
       "zhan is a handsome boy! everyone love him!" \
       "wei is a beautiful girl and she is zhan is wife"
binary_text = text.encode('utf-8')
print(binary_text)
code = np.array([int(i) for i in binary_text])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
