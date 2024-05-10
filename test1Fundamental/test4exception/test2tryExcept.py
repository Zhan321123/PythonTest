"""
利用try-except捕获异常
"
try:
    代码A
except:
    代码B
"
如果A出现异常则执行B
"""
a = input('input a number')
try:
    b = int(a)
    try:
        input(100 / b)
    except:
        print('a/b have exception')
except:
    print('int(a) have exception')
