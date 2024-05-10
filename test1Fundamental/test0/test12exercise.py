import random
import turtle
# 同心圆
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
