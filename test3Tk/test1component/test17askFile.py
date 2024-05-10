"""
filedialog文件选择对话框

    一、对话框类型
  1、文件对话框
askopenfilename(**options)      返回打开的文件
askopenfilenames(**options)     返回打开的多个文件名列表
askopenfile(**options)          返回打开文件对象
askopenfiles(**options)         返回打开的文件的列表
  2、目录对话框
askdirectory(**options)         返回目录名
  3、保存对话框
asksaveasfile(**options)        返回保存的文件对象
asksaveasfilename(**options)    返回保存的文件名

    二、options
defaultextension                                    后缀名，默认为.xxx，没有输入则会自动添加
filetypes=[(label1,pattern1),(label2,pattern2)]     文件显示过滤器，过滤pattern后缀名，显示为(label1,pattern1),(label2,pattern2)
initaldir                                           初始目录
initalfile                                          初始文件
parent                                              父窗口，默认为根窗口
title                                               窗口标题
"""
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('800x600+300+100')
l = Label(root,text='open file here')

# 文件过滤器，用*.filter表示，用*.*表示所有文件类型
filter1 = [('文本文档', '*.txt'), ('python file', '*.py'), ('all file', '*.*')]

def getFile():
    file = askopenfilename(title='open file',initialdir='D:/')
    print(file)
    l.config(text=file)
def view():
    # with打开askopenfile，然后用open打开该文件，就可以设置gbk编码格式
    with askopenfile(filetypes=filter1,) as f:
        print(f.name)
        with open(f.name,encoding='utf-8') as file:
            print(file)
            l.config(text=file.read())
def getDir():
    d = askdirectory(initialdir='C:/user/')
    print(d)
    l['text']=d
def save():
    s = asksaveasfilename(defaultextension='*.zhan',filetypes=filter1)
    s.replace("/", "\\\\")
    print(s)


Button(root,text='open a file',command=getFile).pack()
Button(root,text='view a file',command=view).pack()
Button(root,text='open a dir',command=getDir).pack()
Button(root,text='save a file',command=save).pack()

l.pack()

root.mainloop()