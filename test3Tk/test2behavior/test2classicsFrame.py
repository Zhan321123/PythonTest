"""
python经典的GUI界面的写法
"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        # new button
        self.b1 = Button(self)
        self.b1['text'] = 'click'
        self.b1.pack()
        self.b1['command'] = self.click

        #
        self.b2 = Button(self, text='quit', command=root.destroy)
        self.b2.pack()

    def click(self):
        messagebox.showinfo('click', 'you click here')


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+400+200')
    root.title('classical GUI')
    app = Application(master=root)

    root.mainloop()
