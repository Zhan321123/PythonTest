"""
radiobutton单选
"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create()

    def create(self):
        self.v = StringVar()
        self.v.set('m')
        # 新建单选按钮，variable绑定StringVar，value为选中时StringVar所set的值
        # 用variable来区别同一个单选
        self.r1 = Radiobutton(self,text='male',value='m',variable=self.v)
        self.r2 = Radiobutton(self,text='female',value='f',variable=self.v)

        self.r1.pack()
        self.r2.pack()

        Button(self,text='confirm',command=self.b).pack()

    def b(self):
        messagebox.showinfo('test','you choose '+self.v.get())

if __name__ == '__main__':
    root=Tk()
    root.geometry('600x400+400+300')
    root.title('test radiobutton')
    app = Application(root)
    root.mainloop()

