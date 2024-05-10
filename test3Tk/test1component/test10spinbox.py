"""
spinbox
具体参照 https://blog.csdn.net/qq_41556318/article/details/85596217

"""

import tkinter as tk

root = tk.Tk()

w = tk.Spinbox(root, values=("小新", "风间", "正男", "妮妮", "阿呆"))
w.pack()

root.mainloop()