"""
optionMenu组件的测试
下拉选项框
"""
from tkinter import *

root = Tk()
root.geometry('800x600+300+100')

s = StringVar()
s.set('zhan')
# 新建选项组件OptionMenu
om = OptionMenu(root,s,'nuo','zhan','xiao','duo')
om.pack()

b = Button(root,text='ok',command=lambda :print(s.get()))
b.pack()

root.mainloop()