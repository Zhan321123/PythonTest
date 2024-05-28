"""
turtle示例
"""
import turtle
turtle.showturtle()
turtle.write('zhan')
turtle.forward(300)
turtle.color('red')
turtle.left(90)
turtle.forward(300)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,300)
turtle.pendown()
turtle.circle(100)

print("-----------奥林匹克五环--------------")

turtle.width(20)

turtle.color('red')
turtle.circle(100)

turtle.color('black')
turtle.penup()
turtle.goto(240,0)
turtle.pendown()
turtle.circle(100)

turtle.color('green')
turtle.penup()
turtle.goto(480,0)
turtle.pendown()
turtle.circle(100)

turtle.color('yellow')
turtle.penup()
turtle.goto(120,-100)
turtle.pendown()
turtle.circle(100)

turtle.color('blue')
turtle.penup()
turtle.goto(360,-100)
turtle.pendown()
turtle.circle(100)

print("-----------同心圆--------------")
import random
t = turtle.Pen()
t.speed(0)
t.width(7)

r = 6
color = ('red', 'yellow', 'blue', 'green', 'purple', 'pink', 'brown')

for i in range(1, 1000):
    t.penup()
    t.goto(0, -i * r)
    t.pendown()
    t.color(color[random.randint(0,len(color)-1)])
    t.circle(r * i)

turtle.done()

print("画出棋盘并随机摆上棋子".center(50, '-'))
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