"""
详细参照：tkinter api
https://blog.csdn.net/qq_41556318/category_9283243.html
"""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('my first gui')
# geometry(width x high + leftDistance + topDistance)组件的大小及宽度设置
root.geometry('500x300+400+200')

b1 = Button(root)
b1['text'] = 'start'
b1.pack()


def start(e):
    messagebox.showinfo('Message', 'start here')


b1.bind('<Button-1>', start)

root.mainloop()
