import random
import turtle
"""
画出棋盘并随机摆上棋子
"""
t = turtle.Pen()
t.speed(0)

width = 20
for i in range(0, 17):
    t.penup()
    t.goto(0, i * width)
    t.pendown()
    t.goto(16 * width, i * width)

for i in range(0, 17):
    t.penup()
    t.goto(i * width, 0)
    t.pendown()
    t.goto(i * width, 16 * width)

p = list((x, y) for x in range(0, 17) for y in range(0, 17))


for i in range(0,17*17):
    a = p.pop(random.randint(0, len(p)-1))

    t.penup()
    t.goto(a[0]*width, a[1]*width-width/2)
    t.pendown()
    t.circle(width/2)

turtle.done()
