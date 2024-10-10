"""
文本输入框
输入函数图像就画出
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.widgets import TextBox
matplotlib.use('TkAgg')
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-6.0, 6.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)


def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "t" as its independent variable, e.g.
    "t ** 3".
    """
    ydata = eval(expression, {'np': np}, {'t': t})
    l.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate", textalignment="center")
text_box.on_submit(submit)
text_box.set_val("np.sin(t)*t")  # Trigger `submit` with the initial string.

plt.show()