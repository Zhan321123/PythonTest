import sys
import time
from pathlib import Path

Root = Path(__file__).resolve().parent  # root path
if Root not in sys.path:
  sys.path.append(str(Root))


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
  file = Root / 'files/sortGif/quickPointerSort.gif'
  print(file.exists())
