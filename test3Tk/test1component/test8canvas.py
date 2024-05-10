"""
canvas画布
具体参照 https://blog.csdn.net/qq_41556318/article/details/85272026

    一、functions
create_arc          弧形
create_bitmap       位图
create_image        BitmapImage或PhotoImage的实例对象
create_line         线段
create_oval         椭圆
create_polygon      多边形
create_rectangle    矩形
create_text         文本
create_window       组件component

    二、options
closeenough	        1. 指定一个距离，当鼠标与画布对象的距离小于该值时，鼠标被认为在画布对象上
                    2. 该选项是一个浮点类型的值
confine	            1. 指定 Canvas 组件是否允许滚动超出 scrollregion 选项指定的范围
                    2. 默认值是 True
highlightbackground	指定当 Canvas 没有获得焦点的时候高亮边框的颜色
highlightcolor	    指定当 Canvas 获得焦点的时候高亮边框的颜色
highlightthickness	指定高亮边框的宽度
scrollregion	    1. 指定 Canvas 可以被滚动的范围
                    2. 该选项的值是一个 4 元组（x1, y1, x2, y2）表示的矩形
selectbackground	指定当画布对象被选中时的背景色
selectborderwidth	指定当画布对象被选中时的边框宽度（选中边框）
selectforeground	指定当画布对象被选中时的前景色
state	            1. 设置 Canvas 的状态："normal" 或 "disabled"
                    2. 默认值是 "normal"
                    3. 注意：该值不会影响画布对象的状态
xscrollcommand	    1. 与 scrollbar（滚动条）组件相关联（水平方向）
                    2. 使用方法可以参考：Scrollbar 组件
xscrollincrement	1. 该选项指定 Canvas 水平滚动的“步长”
                    2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
                    3. 默认值是 0，表示可以水平滚动到任意位置
yscrollcommand	    1. 与 scrollbar（滚动条）组件相关联（垂直方向）
                    2. 使用方法可以参考：Scrollbar 组件
yscrollincrement	1. 该选项指定 Canvas 垂直滚动的“步长”
                    2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）
                    3. 默认值是 0，表示可以水平滚动到任意位置


"""
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidght()

    def createWidght(self):
        # 新建画布
        self.c = Canvas(self, width=500, height=350, bg='blue')
        self.c.pack()
        # 画直线，形参为偶数or列表
        self.c.create_line(10, 100, 200, 30, 50, 90, 300, 20)
        # 画矩形
        self.c.create_rectangle(50,50,100,100)
        # 画椭圆
        self.c.create_oval(50,50,100,100)

        self.image = PhotoImage(file='../file/image1.png')
        # 画图像
        self.c.create_image(100,200,image = self.image)


if __name__ == '__main__':
    root = Tk()
    root.geometry('600x400+400+200')
    root.title('button test')
    app = Application(master=root)

    root.mainloop()
