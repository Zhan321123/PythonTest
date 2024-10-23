"""
eval()可以实现程序语句的输入
    eval(str)，返回该str程序语句返回值
    eval(str, dict)，dict为该str中变量名对应的值
"""
x = 2
y = 4
s='x*y'
a = eval(s)
print(a)

d={'x':100,'y':200}

a=eval(s,d)
print(a)

r = eval("list(range(1, 3))")
print(r)