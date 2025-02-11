"""
matplotlib styles

获取所有styles
styles = plt.style.available

plt.style.use('风格主题')
"""
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# 获取所有styles
styles = plt.style.available
print(styles)

fig, (ax1, ax2) = plt.subplots(1, 2)

with plt.style.context('Solarize_Light2'):
    ax2.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax2.set_title('1')
with plt.style.context('dark_background'):
    ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax1.set_title('2')


plt.show()