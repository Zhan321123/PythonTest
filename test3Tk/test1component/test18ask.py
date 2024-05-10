"""
simpledialog和messagebox消息对话框

    一、对话框类型
  1、输入对话框simpledialog
askinteger()        输入int对话框
askfloat()          输入float对话框
askstring()         输入string对话框
  2、事件对话框messagebox
askokcancel()               ok/cancel问题对话框
askquestion()/askyesno()    yes/no确认对话框
askretrycancel()            retry/cancel重试对话框
showerror()                 错误对话框
showinfo()                  信息对话框
showwarning()               警告对话框
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

root = Tk()
root.geometry('800x600+300+100')
s = StringVar()
s.set('your age is:')
l = Label(root,textvariable=s)
def get():
    i = askinteger(title='input frame',prompt='input your age',initialvalue=18,minvalue=1,maxvalue=100)
    s.set(f'your age is : {i}')
def retry():
    # 各自的返回值
    b = askretrycancel(title='retry',message='retry? do you know?')
    print(b)
    y = askquestion(message='')
    print(y)
    y = showerror(message='you have a error')
    print(y)
Button(root,text='get your age',command=get).pack()
Button(root,text='dialog',command=retry).pack()
l.pack()

root.mainloop()