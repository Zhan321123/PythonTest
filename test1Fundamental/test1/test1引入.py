"""
第三方库清华源 https://pypi.tuna.tsinghua.edu.cn/simple
例如：pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
import turtle

t = turtle.Pen()
t.speed(0)
for x in range(1000):
    t.forward(x)
    t.left(59)
