"""
place layout test
"""
from tkinter import *

root = Tk()
root.title('test place layout')
root.geometry('800x600')

f1 = Frame(root,background='green',width=200,height=200)
# place布局
# x,y左上角增加偏移量
f1.place(x=0,y=100)
# relx和rely相对于父容器大小的百分比位置
# relwidth和relheight相对于父容器的百分比大小
Button(f1,text='button1').place(relx=0.5,relheight=0.5)

f2 = Frame(root,background='blue')
f2.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.5)


root.mainloop()