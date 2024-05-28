"""
eval函数
可以实现程序语句的输入
"""
x = 2
y = 4
s='x**2+2*x+1'
a = eval(s)
print(a)

d={'x':100,'y':200}

a=eval(s,d)
print(a)
