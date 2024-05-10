"""
按键事件
    一、
<1> <Button-1> <ButtonPress-1>    1为按下鼠标左键，2为中键，3为右键
<ButtonRelease-1>                 释放鼠标左键
<B1-Motion>                       移动鼠标左键
<Double-Button-1>                 双击鼠标左键
<Enter>                           鼠标进入组件区域
<Leave>                           鼠标离开组件区域
<MouseWheel>                      滚动滚轮
<KeyPress-a>                      按下a键
<KeyPress>                        按下任意键
<KeyRelease-a>                    释放a键
<KeyPress-A>                      按下A键
<Alt-KeyPress-a>                  同时按下alt和a，代替的有ctrl，shift
<Control-C>                       同时按下ctrl和C键

    event对象的属性、
char            按键字符，仅对键盘事件有效
keycode         按键编码，仅对键盘事件有效
keysym          按键名称，仅对键盘事件有效，空格键为space，a为a
num             鼠标按键，仅对鼠标事件有效
type            所触发的事件类型
widget          事件发生的组件
width,height    组件改变后的大小，仅Configure有效
x,y             鼠标相对于父容器的位置
x_root,y_root   鼠标相对于整个屏幕的位置

"""
from tkinter import *

root = Tk()
root.geometry('800x600+300+100')

c = Canvas(root,background='grey',width=600,height=400)
c.pack()

def paint(event):
    c.create_oval(event.x,event.y,event.x+1,event.y+1)
def get(event):
    print(event.x,event.y)
    print(event.widget)

# bind绑定事件和执行的任务
# bind_class所有该class绑定该事件
c.bind('<B1-Motion>',paint)
c.bind('<Button-1>',get)

root.mainloop()