"""
用tuple包含所有exception的写法
"
try:
    code
except(error1,error2...) as e:
    code
"
将异常包含到元组中，异常没有顺序要求
具体的异常将赋给e
"""
a = input('input')
try:
    b = int(a)
    print(100/b)
except(IOError,ZeroDivisionError,ValueError) as e:
    print(type(e))
    print(e)