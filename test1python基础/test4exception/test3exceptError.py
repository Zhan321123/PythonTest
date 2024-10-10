"""
异常的分类捕获
"
try:
    code A
except Error1:
    code B
except Error2:
    code C1
except Exception:
    code D
"
会依次检测A的error
如果没有就停止运行
Exception一些异常的父类异常
"""
a = input('input a number')

try:
    b = int(a)
    print(100/b)
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('zero division error')
except Exception:
    print('unknown exception')