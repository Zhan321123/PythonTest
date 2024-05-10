"""
scrollbar滚动条
    一、options
command	            1. 当滚动条更新时回调的函数
                    2. 通常的是指定对应组件的 xview() 或 yview() 方法
elementborderwidth	指定滚动条和箭头的边框宽度
                    2. 默认值是 -1（表示使用 borderwidth 选项的值）
jump	            1. 指定当用户拖拽滚动条时的行为
                    2. 默认值是 False，滚动条的任何一丝变动都会即刻调用 command 选项指定的回调函数
                    3. 设置为 True 则当用户松开鼠标才调用
orient	            1. 指定绘制 "horizontal"（垂直滚动条）还是 "vertical"（水平滚动条）
                    2. 默认值是 VERTICAL
repeatdelay	        1. 该选项指定鼠标左键点击滚动条凹槽的响应时间
                    2. 默认值是 300（毫秒）
repeatinterval	    1. 该选项指定鼠标左键紧按滚动条凹槽时的响应间隔
                    2. 默认值是 100（毫秒）
takefocus	        1. 指定使用 Tab 键可以将焦点移到该 Scrollbar 组件上
                    2. 默认是开启的，可以将该选项设置为 False 避免焦点在此组件上
troughcolor	        指定凹槽的颜色
width	            指定滚动条的宽度，默认值是 16 像素

"""
import tkinter as tk

root = tk.Tk()

sb = tk.Scrollbar(root)
sb.pack(side="right", fill="y")

lb = tk.Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert("end", str(i))

lb.pack(side="left", fill="both")

sb.config(command=lb.yview)

root.mainloop()