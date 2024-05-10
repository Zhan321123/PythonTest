"""
menu菜单栏
具体参照 https://blog.csdn.net/qq_41556318/article/details/85273584


"""

import tkinter as tk

root = tk.Tk()


def callback():
    print("~被调用了~")


# 创建一个顶级菜单
menubar = tk.Menu(root)

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="粘贴", command=callback)
menubar.add_cascade(label="编辑", menu=editmenu)

# 显示菜单
root.config(menu=menubar)

root.mainloop()