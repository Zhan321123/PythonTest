"""
利用if-else解决解决能解决的异常
"""
a = input('input a number')
if a.isdigit():
    b = int(a)
    if b != 0:
        print(100 / b)
    else:
        print('division is zero')
else:
    print('what you input is not a number')
