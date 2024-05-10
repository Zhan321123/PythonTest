"""
方法的
"""
def f1(n):
    """finding the factorial of n"""
    if n == 1:
        return 1
    else:
        return f1(n - 1) * n


print(f1(100))


def f2(n):
    """finding the Fibonacci of n"""
    if n == 1 or n == 2:
        return 1
    else:
        return f2(n - 1) + f2(n - 2)


print(f2(30))
