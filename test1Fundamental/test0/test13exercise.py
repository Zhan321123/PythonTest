import turtle
from math import *

"""
实现输入函数画出函数
"""
t = turtle.Pen()
t.speed(0)

t.width(1)
t.goto(-10000, 0)
t.goto(10000, 0)
t.goto(0, 0)
t.goto(0, 10000)
t.goto(0, -10000)
t.goto(0, 0)

t2 = turtle.Pen()

# 图像大小
size = 50

# 定义域左侧
x = y = 0

# 函数
s1 = input('input function')
s2 = s1.replace('x', 'y')

y0 = eval(s1)
t.goto(0, y0*size)
t2.goto(0, y0*size)

t2.width(2)
t.width(2)
while (True):
    x += 0.1
    y -= 0.1
    y1 = eval(s1)
    y2 = eval(s2)
    t2.goto(x * size, size * y1)
    t.goto(-x * size, size * y2)
