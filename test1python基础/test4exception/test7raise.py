"""
抛出异常
raise Exception()
"""

def divide(a=str(),b=str()):
    if a.isdigit() or b.isdigit():
        if int(b) != 0:
            print(int(a)/int(b))
        else:
            raise ZeroDivisionError()
    else:
        raise ValueError()

try:
    divide('23','a')
except (ZeroDivisionError,ValueError) as e:
    print(e)
    print(type(e))

try:
    divide('23','0')
except (ZeroDivisionError,ValueError) as e:
    print(e)
    print(type(e))