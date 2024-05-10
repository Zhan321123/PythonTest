"""
label文本框组件

    一、options
activebackground	设置当 Label 处于活动状态（通过 state 选项设置状态）的背景色
activeforeground	设置当 Label 处于活动状态（通过 state 选项设置状态）的前景色
anchor	            控制文本（或图像）在 Label 中显示的位置，值有"n","ne","e","se","s","sw","w","nw","center"，默认值是 "center"
background	        设置背景颜色
foreground	        设置 Label 的文本和位图的颜色
bitmap	            指定显示到 Label 上的位，如果指定了 image 选项，则该选项被忽略
borderwidth	        指定 Label 的边框宽度
compound	        1. 控制 Label 中文本和图像的混合模式
                    2. 默认情况下，如果有指定位图或图片，则不显示文本
                    3. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）
                    4. 如果该选项设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边（如 "bottom"，则图像在文本的下方）
                    5. 默认值是 NONE
cursor	            指定当鼠标在 Label 上飘过的时候的鼠标样式
disabledforeground	指定当 Label 不可用的时候前景色的颜色
font	            1. 指定 Label 中文本的字体(注：如果同时设置字体和大小，应该用元组包起来，如（"楷体", 20）
                    2. 一个 Label 只能设置一种字体
height,width        1. 设置 Label 的高度、宽度
                    2. 如果 Label 显示的是文本，那么单位是文本单元大小
                    3. 如果 Label 显示的是图像，那么单位是像素（或屏幕单元）
                    4. 如果设置为 0 或者干脆不设置，那么会自动根据 Label 的内容计算出高度和宽度
highlightbackground	指定当 Label 没有获得焦点的时候高亮边框的颜色
highlightcolor	    指定当 Label 获得焦点的时候高亮边框的颜色
highlightthickness	指定高亮边框的宽度，默认值是 0（不带高亮边框）
image	            1. 指定 Label 显示的图片
                    2. 该值应该是 PhotoImage，BitmapImage，或者能兼容的对象
                    3. 该选项优先于 text 和 bitmap 选项
justify	            1. 定义如何对齐多行文本，注意，文本的位置取决于 anchor 选项
                    2. 使用 "left"，"right" 或 "center"，默认值是 "center"
padx,pady           指定 Label 水平方向上的额外间距（内容和边框间），单位是像素
relief	            指定边框样式，可以设置 "groove", "raised", "ridge", "solid" 或者 "sunken"，默认值是 "flat"
state	            1. 指定 Label 的状态，这个标签控制 Label 如何显示
                    2. 可以设置 "active" 或 "disabled"，默认值是 "normal
takefocus           如果是 True，该 Label 接受输入焦点，默认值是 False
text	            1. 指定 Label 显示的文本，文本可以包含换行符
                    2. 如果设置了 bitmap 或 image 选项，该选项则被忽略
textvariable	    1. Label 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
                    2. 如果变量被修改，Label 的文本会自动更新
underline	        1. 跟 text 选项一起使用，用于指定哪一个字符画下划线（例如用于表示键盘快捷键），默认值是 -1
                    2. 例如设置为 1，则说明在 Button 的第 2 个字符处画下划线
wraplength	        1. 决定 Label 的文本应该被分成多少行，默认值是 0
                    2. 该选项指定每行的长度，单位是屏幕单元

"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        self.l1 = Label(self, text='a label', width=10, height=2, background='pink', foreground='blue')
        self.l1.pack()
        self.l2 = Label(self, text='a new label', width=10, height=2, background='pink', foreground='blue',
                        font=('黑体', 40))
        self.l2.pack()

        # 新建图像
        self.photo = PhotoImage(file='../file/image1.png')
        self.l3 = Label(self, image=self.photo)
        self.l3.pack()


        # relief边框样式：solid黑框、groove沟槽、sunken凹陷
        # borderwidth边框宽度
        # justify对齐方式，left左对齐，center居中，right右对齐
        self.l4 = Label(self, text='fuck you\nthank you\nall for you', borderwidth=10, relief='sunken', justify='right')
        self.l4.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+400+200')
    root.title('label test')
    app = Application(master=root)

    root.mainloop()
