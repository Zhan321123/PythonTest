"""
bind绑定事件
bind_class所有该类绑定事件
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self['width'] = 800
        self['height'] = 600
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        s = ['J','Q','K','A',]+[str(i) for i in range(2,11)]
        ls = [Label(self,background='pink',borderwidth=2,relief='solid', width=5, height=20) for i in range(13)]
        self.ls2 = [Label(ls[i],text=s[i],background='red',) for i in range(13)]
        for i in range(13):
            ls[i].place(x=100+i*30,y=100)
            self.ls2[i].place(relheight=0.1,relwidth=0.3)

        # 给每一个class为Label的组件绑定事件
        # bind_class(组件,事件,执行函数)
        ls[0].bind_class('Label','<Button-1>',self.out)


    def out(self,event):
        # 获取事件发生的组件的属性
        print(event.widget.winfo_geometry())
        if event.widget.winfo_y() == 100:
            event.widget.place(y=50)
        else:
            event.widget.place(y=100)

if __name__ == '__main__':
    root = Tk()
    root.title('test')
    root.geometry('800x600+300+200')
    Application(root)
    root.mainloop()
