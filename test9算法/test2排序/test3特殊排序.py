import random


def followOrderSort(canSort: list, order: list) -> (list, list):
  """
  跟随排序，order跟随canSort排序
  :param canSort:
  :param order:
  :return:
  """
  sortedPairs = sorted(zip(canSort, order))
  canSort, order = zip(*sortedPairs)
  return canSort, order


if __name__ == '__main__':
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  random.shuffle(a)
  print(a)
  # print(followOrderSort(a, b))

  b.sort(key=a)
  print(b)