"""
grid layout网格布局
    二、options
column	    1. 指定组件插入的列（0 表示第 1 列）
            2. 默认值是 0
columnspan	指定用多少列（跨列）显示该组件
in_	        1. 将该组件放到该选项指定的组件中
            2. 指定的组件必须是该组件的父组件
ipadx	    指定水平方向上的内边距
ipady	    指定垂直方向上的内边距
padx	    指定水平方向上的外边距
pady	    指定垂直方向上的外边距
row	        指定组件插入的行（0 表示第 1 行）
rowspan	    指定用多少行（跨行）显示该组件
sticky	    1. 控制组件在 grid 分配的空间中的位置
            2. 可以使用 "n", "e", "s", "w" 以及它们的组合来定位（ewsn代表东西南北，上北下南左西右东）
            3. 使用加号（+）表示拉长填充，例如 "n" + "s" 表示将组件垂直拉长填充网格，"n" + "s" + "w" + "e" 表示填充整个网格
            4. 不指定该值则居中显示
"""
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # grid网格布局
        # row和colum表示行列位置
        Label(self,text='username').grid(row=0,column=0)
        Label(self,text='password').grid(row=1,column=0)
        # columnspan和rowspan，跨越的行列数
        # sticky贴合边框
        Entry(self).grid(row=0,column=1,columnspan=2,sticky=EW)
        Entry(self,show='*').grid(row=1,column=1)
        Label(self,text='three chance').grid(row=1,column=2)

        Button(self,text='login').grid(row=2,column=1)
        Button(self,text='quit',command=lambda :quit()).grid(row=2,column=2)

if __name__ == '__main__':
    root = Tk()
    root.title('test grid layout')
    root.geometry('800x600+300+200')
    Application(root)
    root.mainloop()