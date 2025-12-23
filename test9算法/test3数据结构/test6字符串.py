"""
哈夫曼编码
"""


def countTimes(data: str) -> dict:
  """
  统计字符出现的次数
  :param data:
  :return: 字符出现的次数
  """
  return {char: data.count(char) for char in set(data)}


def toHuffmanCode(data: str) -> (dict, str):
  """
  哈夫曼编码 TODO
  :param data:
  :return: 编码表，编码结果
  """
  ct = countTimes(data)
