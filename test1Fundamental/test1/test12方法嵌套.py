"""
嵌套方法
在方法里定义方法
"""
def f():
    print('fuck')
    def f1():
        print('shit')
    f1()
f()

def fuck(china, mom, name):
    def shit(a, b):
        print(a, b)
    if not china:
        shit(mom, name)
    else:
        shit(name, mom)
fuck(True, 'mom', 'xiao')
