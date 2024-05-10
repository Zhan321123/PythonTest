"""
Button按钮

invoke(参)，调用button的command并返回参数
    一、options
command         指定按钮的执行的命令

"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidght()

    def createWidght(self):
        def login():
            messagebox.showinfo('message', 'you just clicked here')

        self.b1 = Button(text='click here', command=login)
        self.b1.pack()

        # anchor锚，文字的方位，可填NESW
        self.image = PhotoImage(file='../file/image2.png')
        self.b2 = Button(text='login', image=self.image, anchor=NE, width=300, height=200,
                         command=lambda: print('login'))
        self.b2.pack()

        self.b3 = Button(text="can't click here", state=DISABLED, command=lambda: print('never click here'))
        self.b3.pack()

        self.b4 = Button(text='what', width=6, height=3, anchor=SW)
        self.b4.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x400+400+200')
    root.title('button test')
    app = Application(master=root)

    root.mainloop()
