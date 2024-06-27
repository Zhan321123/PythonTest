"""
装饰器


TODO 未完成
"""
import time


def decoratorFunction(func):
    """一个装饰器输出函数执行时间"""
    def wrapper(*args, **kwargs):
        startTime = time.time()
        v = func(*args, **kwargs)
        endTime = time.time()
        print(f'{func.__name__}函数执行时间{endTime - startTime}')
        return v
    return wrapper

@decoratorFunction
def function1(n):
    for i in range(1,n):
        n/i*i
    return n

x = function1(10000000)
print(x)

print('------------------------------------------')

def create(name, bases, dict):
    """
    动态创建类的函数。

    参数:
    name -- 类的名字
    bases -- 类的基类元组
    dict -- 类的字典，包含属性和方法
    """
    return type(name, bases, dict)

# 使用create_class函数动态创建一个类
MyClass = create('MyClass', (object,), {'x': 5, 'y': 10, 'add': lambda self: self.x + self.y})

# 实例化这个动态创建的类，并调用其方法
instance = MyClass()
print(instance.add())  # 输出: 15
