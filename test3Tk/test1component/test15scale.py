"""
scale组件的测试
可拉伸的刻度条
"""
from tkinter import *

root = Tk()
root.geometry('800x600+300+100')

l = Label(root, text='fuck you', background='black', foreground='white')
l.pack()


def change(v):
    print(v)
    font = ('微软雅黑', v)
    l.config(font=font)

# 新建Scale(root,from_=开始值,to=结束值,length=长度,tickinterval=刻度间隔,orient=方向)
# 方向默认为竖直方向
# command，有变动时才会执行，也会自动传入一个参数，参数为当前刻度值
s = Scale(root, from_=10, to=50, length=200, tickinterval=10, orient=HORIZONTAL, command=change)
s.pack()

root.mainloop()
