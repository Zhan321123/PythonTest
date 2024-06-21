"""
微分

定积分 scipy库
    result结果, error误差 = scipy.integrate.quad(function函数, 下限, 上限)

不定积分 sympy库
    变量x = symbols('x')
    函数y = function(x)
    积分结果integral = integrate(y, x)

"""
import math
from scipy.integrate import quad
from sympy import symbols, integrate

# 定积分
def function1(x: float) -> float:# 标准正态分布函数
    return math.e ** (-x ** 2 / 2) / math.sqrt(2 * math.pi)
result, error = quad(function1, -3, 3)  # 积分(-3,3)
print(f"积分结果: {result}, 积分误差: {error}")

# 不定积分
x = symbols('x')
y = x**2
integral = integrate(y, x)
print(integral)