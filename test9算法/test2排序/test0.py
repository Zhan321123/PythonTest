import copy
import random
import time

random.seed(100)


def generateRandomSequence(n: int, m: int) -> list:
  """
  生成长度为 n 的随机序列，序列中的元素范围是 [1, m]
  """
  return [random.random() * m for _ in range(n)]


def generateRandomRange(n: int) -> list:
  """
  生成 range(1,n+1)，然后打乱
  """
  return random.sample(range(1, n + 1), n)


def generateRandomStrings(n: int, length: int, ):
  """
  生成n个字符串，长度(0,length]
  """
  return [''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(1, length + 1)))
          for _ in range(n)]


def checkSequence(arr: list) -> bool:
  """
  检查序列是否为有序的
  """
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      return False
  return True


def timing(func: callable) -> callable:
  """
  函数执行时间装饰器
  """

  def wrapper(*args, **kwargs):
    startTime = time.time()
    v = func(*args, **kwargs)
    endTime = time.time()
    print(f'{func.__name__} 函数执行时间 {(endTime - startTime) * 1000} ms')
    return v

  return wrapper


if __name__ == '__main__':
  print(generateRandomStrings(100, 10))
