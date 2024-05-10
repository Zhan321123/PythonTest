"""
toplevel顶窗格
具体参照 https://blog.csdn.net/qq_41556318/article/details/85597698

"""
import tkinter as tk

root = tk.Tk()


def create():
    top = tk.Toplevel()
    top.title("Python")

    msg = tk.Message(top, text="I love Python!")
    msg.pack()


tk.Button(root, text="创建顶级窗口", command=create).pack()

root.mainloop()