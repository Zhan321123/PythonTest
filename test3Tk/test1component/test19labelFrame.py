"""
labelFrame文字边框frame

    一、options
labelanchor	    控制文本在 LabelFrame 的显示位置，"n", "ne", "e", "se", "s", "sw", "w", "nw", 或 "center" 来定位，默认值是 NW
labelwidget	    指定一个组件替代默认的文本 Label，如果同时设置此选项和 text 选项，则忽略 text 选项的内容
text	        指定 LabelFrame 显示的文本2. 文本可以包含换行符
visual	        为新窗口指定视觉信息
"""
from tkinter import *

root = Tk()
root.geometry('800x600')

lf = LabelFrame(root, text='i am a label frame')
lf.pack()

Button(lf, text='fuck', command=lambda: lf.config(text='fuck you')).pack()

root.mainloop()
