"""
pack layout简单布局


    一、options
anchor	1. 控制组件在 pack 分配的空间中的位置
        2. "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位（ewsn 代表东西南北，上北下南左西右东）
        3. 默认值是 "center"
expand	1. 指定是否填充父组件的额外空间
        2. 默认值是 False
fill	1. 指定填充 pack 分配的空间
        2. 默认值是 NONE，表示保持子组件的原始尺寸
        3. 还可以使用的值有："x"（水平填充），"y"（垂直填充）和 "both"（水平和垂直填充）
in_	    1. 将该组件放到该选项指定的组件中
        2. 指定的组件必须是该组件的父组件
ipadx	指定水平方向上的内边距
ipady	指定垂直方向上的内边距
padx	指定水平方向上的外边距
pady	指定垂直方向上的外边距
side	1. 指定组件的放置位置
        2. 默认值是 "top"
        3. 还可以设置的值有："left"，"bottom"，"right"
"""
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # Frame新的容器
        f1 = Frame(self)
        f1.pack()
        # side靠的方向
        for i in ['chinese','math','english','PE','music']:
            Button(f1,text=i).pack(side='left')

        # pady和padx，x和y方向的间隔
        f2 = Frame(self)
        f2.pack(side='bottom',pady=10)
        for i in range(0,20):
            Label(f2,background='black' if i%2==0 else 'white',width=5,height=10).pack(side='left',padx=1)

if __name__ == '__main__':
    root = Tk()
    root.title('test grid layout')
    root.geometry('800x600+300+200')
    Application(root)
    root.mainloop()