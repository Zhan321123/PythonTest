"""
调和数列
    A(n) = 1/n
    S(n) = ln(n) + C, (n足够大)
    欧拉常数 C 约等于 0.5772156649

斐波那契fibonacci数列
    A(1) = 1
    A(2) = 1
    A(n) = A(n-1) + A(n-2)
    A(n) = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)
    S(n) = 2 * A(n) + A(n - 1) - 1

等差数列
    A(1) = 0
    A(n) - A(n-1) = a
    A(n) = a * (n - 1)
    S(n) = a * n * (n - 1) / 2

等比数列
    A(1) = 1
    A(n) / A(n-1) = a
    A(n) = a ** (n - 1)
    S(n) = (a ** n - 1) / (a - 1)

幂数列
    A(n) = n ** a
    S(n) =
    当 a=2
        S(n) = n * (n + 1) * (2 * n + 1) / 6
    当 a=3
        S(n) = (n * (n + 1)) ** 2 / 4



"""
import math


def euler():
  """欧拉常数"""
  x = 0
  last = 0
  while True:
    x += 1
    a = math.log(x)
    b = sum(1 / j for j in range(1, x + 1))
    deta = a - b
    if abs(deta - last) < 1e-9:
      print(deta)
      return deta
    last = deta


def harmonicSum(n):
  """调和数列求和"""
  result = sum(1 / i for i in range(1, n + 1))
  print(result)
  return result


def fibonacci(n, fast=False):
  """斐波那契数列"""
  if not fast:
    a, b = 1, 1
    for i in range(n - 2):
      a, b = b, a + b
    # print(b)
    return b

  result = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)
  # print(result)
  return result


def fibonacciSum(n):
  """斐波那契数列求和"""
  result = 2 * fibonacci(n) + fibonacci(n - 1) - 1
  print(result)
  return result


if __name__ == '__main__':
  # euler()
  # harmonicSum(10)
  # fibonacci(10)
  fibonacciSum(10)
