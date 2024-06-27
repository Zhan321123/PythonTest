import time

def timer_decorator(func):
    """
    计算并打印函数执行时间的装饰器。
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def example_function(n):
    """
    简单示例函数，计算n的平方。
    """
    return n ** 2

a = example_function(1000)  # 输出计算结果，并打印执行时间
print(a)