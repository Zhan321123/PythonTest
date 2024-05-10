"""
treeview
表格框
"""
from tkinter import ttk
from tkinter import *

root = Tk()
root.title('表结构')
root.geometry('600x600')

frame = Frame(root)
# frame.pack(anchor=W, ipadx=10, side=LEFT, expand=True, fill=X)
# fill 以对齐->加滚轮
content = Text(root, width=0, height=30)
content.pack(anchor=W, side=LEFT, expand=False)
content.configure(background=root.cget('background'), highlightbackground=root.cget('background'))

# 列,表中每一列的题头
column = ['line','value']
# 声明一个Treeview，参数（parent,height,columns,show)
# 这里的声明我用了四个参数，父节点自不用说（属于），height字段为前端显示的行数
# columns字段为属性列表，每一个列为一个字符串所标记
# show 字段我最常用的就是‘headings’，不显示表的第一列
treeview = ttk.Treeview(root, height=19, columns=column, show='headings')

# pack 布局，这是加滚轮所必须的布局，anchor方位（NSWE）可设八个方位，
# ipad为组件之间的距离（我也没试出来效果），expand 扩展参数bool，fill为填充字段X，Y，BOTH
treeview.pack(anchor=W, ipadx=100, side=LEFT, expand=True, fill=BOTH)

# 每一列的具体设置用column函数，heading为显示指定列名，可以循环指定，你懂得
treeview.column(column[0], width=100, anchor='center')
treeview.heading(column[0], text=column[0])
treeview.column(column[1], width=500, anchor='w')
treeview.heading(column[1], text=column[1])

# 下一部分很重要，如果需要加滚轮的话直接按这个来
# ----vertical scrollbar------------
vbar1 = ttk.Scrollbar(treeview, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=vbar1.set)
vbar1.pack(side=RIGHT, fill=Y)
# ----horizontal scrollbar----------
hbar1 = ttk.Scrollbar(treeview, orient=HORIZONTAL, command=treeview.xview)
treeview.configure(xscrollcommand=hbar1.set)
hbar1.pack(side=BOTTOM, fill=X)
# 不知道有没有用
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

for i in range(100):
    temp = treeview.insert('', index=i)  # 新建行
    treeview.set(temp, column=column[0], value=str(i))
    treeview.set(temp, column=column[1],value='我是值')
    # 上三行可以用下一行代替，你懂得
    # treeview.insert('',0,values=(str(i),'我是值'))
root.mainloop()
