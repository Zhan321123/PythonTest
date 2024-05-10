"""
text
"""
import webbrowser
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create()

    def create(self):
        # 新建text文本框
        # width的数字不是像素大小，而是字母的宽度，一半汉字的宽度
        # height是字母的高度
        self.t1 = Text(self, width=40, height=12, background='gray')
        self.t1.pack()
        # insert(行.列,string文本)，行从1开始，列从0开始
        self.t1.insert(1.0, 'fuck you\ndo you know')
        self.t1.insert(2.3, 'hello world\n')

        Button(self, text='add 666', command=self.b1).pack(side='left')
        Button(self, text='print 2.3-4.5 and all', command=self.b2).pack(side='right')
        Button(self, text='add image', command=self.b3).pack(side='left')
        Button(self, text='add widget', command=self.b4).pack(side='left')
        Button(self, text='delete all', command=self.b5).pack(side='left')
        Button(self, text='tag text', command=self.b6).pack(side='left')

    def b1(self):
        # INSERT光标所在位置，END文本最后
        self.t1.insert(INSERT, 'fuck')
        self.t1.insert(END, '666')

    def b2(self):
        # get(开始行.开始列,结束行.结束列)，获取text文本内容，string和float都行
        print(self.t1.get(2.3, '4.5'))
        # 1.0-END索引到全部
        print(self.t1.get(1.0, END))

    def b3(self):
        self.image = PhotoImage(file='../file/image2.png')
        # 添加图片
        self.t1.image_create(END, image=self.image)

    def b4(self):
        b = Button(self.t1, text='DONE', command=lambda: print('fuck'))
        # 添加组件可执行的组件
        self.t1.window_create(INSERT, window=b)

    def b5(self):
        # 删除文本
        self.t1.delete(1.0, END)

    def b6(self):
        # 标记文本和操作
        self.t1.tag_add('tag1', 2.0, '2.10')
        self.t1.tag_config('tag1',background='yellow',foreground='red')

        self.t1.tag_add('tag2',3.0,3.5)
        # underline下划线
        self.t1.tag_config('tag2',underline=True)

        # 打开网页操作，一定要在形参中写event才行
        def bb(event):
            webbrowser.open('https://fanyi.baidu.com/')
        # 标记的鼠标左击操作
        self.t1.tag_bind('tag2','<Button-1>',bb)


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+400+200')
    root.title('text test')
    app = Application(root)

    root.mainloop()
