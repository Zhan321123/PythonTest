"""
treeview
树结构，文件分层结构
"""

from tkinter import ttk
from tkinter import *

root = Tk()
root.title('树结构')
root.geometry('600x600')

# Treeview树
tree = ttk.Treeview(root)

tree.pack(fill=BOTH, expand=YES)

# insert(parent,index,iid=None,**kw)
# insert 方法是向Treeview中添加结点，返回值为插入的item
# 参数说明：parent为父节点, ''空串，代表根节点
# index为第几个结点，通常都是用0 或者 'end' 来放置结点到第一个或者最后一个位置
# iid可以显示确定也可以默认
# 关键字字段可以有text属性，用于前端显示文本
# 可以有vlaue属性, 这个字段在树型结构中可以不定义，应该是用于判断节点等价的（理解为hash）
# 可以有open属性，这个字段代表节点默认打开还是关闭，bool型，缺省值为False
item0 = tree.insert('',0,text='我是根节点',open=True)
item1 = tree.insert(item0,0,text='我是第一个子节点')
item21 = tree.insert(item1,0,text='我是第一个子节点的第一个子节点')
item22 = tree.insert(item1,'end',text='我是第一个子节点的最后一个子节点')


root.mainloop()
