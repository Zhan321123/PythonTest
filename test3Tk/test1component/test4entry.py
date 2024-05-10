"""
entry单行输入框
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidght()

    def createWidght(self):
        self.l1 = Label(text='input your telephone')
        self.l1.pack()

        # 使用StringVar绑定组件的textvariable
        v1 = StringVar()
        self.e1 = Entry(textvariable=v1)
        self.e1.pack()
        v1.set('+86')

        # show输入的字符变成展示的字符
        self.e2 = Entry(show='*')
        self.e2.pack()

        def f1():
            v2.set(v2.get() + '\n' + v1.get() + '\nthis is your telephone\nplease remember it')

        self.b1 = Button(text='register', command=f1)
        self.b1.pack()

        v2 = StringVar()
        v2.set('no')
        self.l2 = Label(textvariable=v2)
        self.l2.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+400+200')
    root.title('test entry')
    app = Application(root)
    root.mainloop()
