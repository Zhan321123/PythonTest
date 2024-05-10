"""
colorchooser.askcolor颜色选择界面
"""
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry('800x600+300+100')

def a():
    # 颜色选择框
    # color默认颜色，title标题
    # 返回((r,g,b),颜色#str)元组
    c = askcolor(color='green',title='color choosing frame')

    print(c)
    root.config(background=c[1])
b = Button(root,text='choose a color')
b.pack()
b.config(command=a)


root.mainloop()