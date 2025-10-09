import random

from test9算法.test2排序.test0 import timing


@timing
def mySearchString(string: str, sub: str) -> [int]:
  if not sub or len(sub) > len(string):
    return []
  position = []
  for i in range(len(string) - len(sub) + 1):
    for j in range(len(sub)):
      if string[i + j] != sub[j]:
        break
    else:
      position.append(i)
  return position


@timing
def kmpSearchString(string: str, sub: str) -> [int]:
  # TODO
  if not sub or len(sub) > len(string):
    return []

    # 构建部分匹配表(LPS数组)

  def build_lps(pattern):
    n = len(pattern)
    lps = [0] * n
    length = 0  # 最长前缀后缀的长度

    i = 1
    while i < n:
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0:
          # 回退到上一个可能的匹配
          length = lps[length - 1]
        else:
          lps[i] = 0
          i += 1
    return lps

  lps = build_lps(sub)
  result = []
  i = 0  # 主串指针
  j = 0  # 子串指针

  while i < len(string):
    if string[i] == sub[j]:
      i += 1
      j += 1

    if j == len(sub):
      # 找到一个匹配，记录起始位置
      result.append(i - j)
      j = lps[j - 1]
    elif i < len(string) and string[i] != sub[j]:
      if j != 0:
        # 根据LPS数组调整子串指针
        j = lps[j - 1]
      else:
        i += 1

  return result


if __name__ == '__main__':
  random.seed(0)
  text = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for _ in range(1000000))

  print(mySearchString(text, 'abcd'))
  print(kmpSearchString(text, 'abcd'))
