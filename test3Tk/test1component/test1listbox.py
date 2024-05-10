"""
listbox选择框
    一、functions
insert(位置,对象)
delete(起始位置,最终位置)
    二、options
exportselection	    指定选中的项目文本是否可以被复制到剪贴板默认值是 True，修改为 False 表示不允许复制项目文本
selectbackground	指定当某个项目被选中的时候背景颜色
selectborderwidth	1. 指定当某个项目被选中的时候边框的宽度
                    2. 默认是由 selectbackground 指定的颜色填充，没有边框
                    3. 如果设置了此选项，Listbox 的每一项会相应变大，被选中项为 "raised" 样式
selectforeground	指定当某个项目被选中的时候文本颜色
selectmode	        1. 决定选择的模式
                    2. 四种不同的选择模式：默认是 "browse"
                        "single"（单选）
                        "browse"（单选，拖动鼠标或通过方向键可以直接改变选项）
                        "multiple"（多选）
                        "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）
setgrid	            指定一个布尔类型的值，决定是否启用网格控制，默认值是 False
xscrollcommand,yscrollcommand
                    1. 为 Listbox 组件添加一条水平滚动条
                    2. 将此选项与 Scrollbar 组件相关联即可

"""
import tkinter as tk

root = tk.Tk()

# 创建一个空列表
lb = tk.Listbox(root)
lb.pack()

# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
    lb.insert("end", item)


lb.delete(1, "end")
# 插入新的项目
lb.insert("end", 'newitem')

root.mainloop()