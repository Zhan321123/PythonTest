"""
排序

基元：range, len,

方法：
  插入排序
  希尔排序（Knuth间隔）

"""
import copy

from test0 import *


@timing
def insertSort(arr: list) -> list:
  """插入排序"""
  for i in range(len(arr)):
    v = arr[i]
    for j in range(i - 1, -1, -1):
      if arr[j] > v:
        arr[j + 1] = arr[j]
        arr[j] = v

  return arr


@timing
def hillSort(arr: list) -> list:
  """希尔排序(使用Knuth间隔)"""
  maxGap = len(arr) // 3
  gap = 1
  while gap <= maxGap:
    gap = gap * 3 + 1  # 间隔为 3k + 1
    for i in range(gap, len(arr)):
      v = arr[i]
      j = i - gap
      while j >= 0 and arr[j] > v:
        arr[j + gap] = arr[j]
        j -= gap
      arr[j + gap] = v
  return insertSort(arr)  # 最后插入排序


@timing
def selectSort(arr: list) -> list:
  """选择排序"""
  for i in range(len(arr)):
    minIndex = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[minIndex]:
        minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
  return arr


@timing
def heapSort(arr: list) -> list:
  """堆排序"""

  def heapify(arr, n, i):
    largest = i  # 初始化根节点为最大值
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 若左子节点大于根节点，更新最大值索引
    if left < n and arr[left] > arr[largest]:
      largest = left
    # 若右子节点大于当前最大值，更新最大值索引
    if right < n and arr[right] > arr[largest]:
      largest = right

    # 若最大值不是根节点，交换并递归调整子树
    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)

  n = len(arr)

  # 构建大顶堆（从最后一个非叶子节点向上调整）
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # 逐步提取最大值并调整堆
  for i in range(n - 1, 0, -1):
    # 交换堆顶（最大值）与当前堆尾
    arr[0], arr[i] = arr[i], arr[0]
    # 调整剩余元素为大顶堆（堆大小减1）
    heapify(arr, i, 0)

  return arr


def bubbleSort(arr: list) -> list:
  """冒泡排序"""


def quickHoareSort(arr: list) -> list:
  """快速排序(Hoare)"""


def quickPointerSort(arr: list) -> list:
  """快速排序(前后指针)"""


def quickHoleSort(arr: list) -> list:
  """快速排序(挖坑法)"""


def quickNotRecursiveSort(arr: list) -> list:
  """快速排序(非递归)"""


def recursiveSort(arr: list) -> list:
  """归并排序(递归法)"""


def notRecursiveSort(arr: list) -> list:
  """归并排序(非递归)"""


def countSort(arr: list) -> list:
  """计数排序"""


def cardinalSort(arr: list) -> list:
  """基数排序"""


def bucketSort(arr: list) -> list:
  """桶排序"""


if __name__ == '__main__':
  seq = generateRandomSequence(10000, 100)

  insertSeq = insertSort(copy.copy(seq))
  hillSeq = hillSort(copy.copy(seq))
  selectSeq = selectSort(copy.copy(seq))
  heapSeq = heapSort(copy.copy(seq))

  print(checkSequence(insertSeq))
  print(checkSequence(hillSeq))
  print(checkSequence(selectSeq))
  print(checkSequence(heapSeq))

  seq.sort()
  print(seq == insertSeq == hillSeq == selectSeq == heapSeq)

  print(heapSeq)
