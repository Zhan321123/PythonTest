"""
checkbutton多选按钮
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
        self.a = IntVar()
        self.b = IntVar()
        # 新建多选，onvalue选中时的值，offvalue未选中时的值
        self.c1 = Checkbutton(self,text='fuck',variable=self.a,
                              onvalue=1,offvalue=0)
        self.c2 = Checkbutton(self, text='shit', variable=self.b,
                              onvalue=1, offvalue=0)

        self.c1.pack()
        self.c2.pack()

        Button(self,text='say',command=self.confirm).pack()

    def confirm(self):
        s = ''
        if self.a.get() == 1:
            s+='fuck you '
        if self.b.get() == 1:
            s+='all shit'
        messagebox.showinfo('test',s)

if __name__ == '__main__':
    root=Tk()
    root.geometry('600x400+400+300')
    root.title('test radiobutton')
    app = Application(root)
    root.mainloop()

