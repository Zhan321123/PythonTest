import copy
import io

from PIL import Image
from matplotlib import pyplot as plt

from test0utils import *


def insertSort(arr: list):
  """插入排序"""
  yield "origin", arr
  for i in range(len(arr)):
    v = arr[i]
    for j in range(i - 1, -1, -1):
      yield "compare", (j, i)
      if arr[j] > v:
        arr[j + 1] = arr[j]
        arr[j] = v
        yield "swap", (j, j + 1, arr)


def hillSort(arr: list):
  """希尔排序(使用Knuth间隔)"""
  yield "origin", arr
  maxGap = len(arr) // 3
  gap = 1
  while gap <= maxGap:
    gap = gap * 3 + 1  # 间隔为 3k + 1
    yield "info", {"gap": gap}
    for i in range(gap, len(arr)):
      v = arr[i]
      j = i - gap
      yield "compare", (j, i)
      while j >= 0 and arr[j] > v:
        arr[j + gap] = arr[j]
        yield "swap", (j + gap, j, arr)
        j -= gap
      arr[j + gap] = v
      yield "swap", (i, j + gap, arr)
  yield from insertSort(arr)


def selectSort(arr: list):
  """选择排序"""
  yield "origin", arr
  for i in range(len(arr)):
    minIndex = i
    for j in range(i + 1, len(arr)):
      yield "compare", (j, minIndex)
      if arr[j] < arr[minIndex]:
        minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]
    yield "swap", (i, minIndex, arr)


def heapSort(arr: list):
  """堆排序"""
  yield "origin", arr

  def heapify(arr, n, i):
    largest = i  # 初始化根节点为最大值
    yield "info", {"largest": largest}
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    if left < n:
      yield "compare", (left, largest)
      if arr[left] > arr[largest]:
        largest = left
    if right < n:
      yield "compare", (right, largest)
      if arr[right] > arr[largest]:
        largest = right
    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      yield "swap", (i, largest, arr)
      yield from heapify(arr, n, largest)

  n = len(arr)
  for i in range(n // 2 - 1, -1, -1):
    yield from heapify(arr, n, i)
  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    yield "swap", (0, i, arr)
    yield from heapify(arr, i, 0)


def bubbleSort(arr: list):
  """冒泡排序"""
  yield "origin", arr
  for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
      yield "compare", (j, j + 1)
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        yield "swap", (j, j + 1, arr)


def quickHoareSort(arr: list):
  """快速排序(Hoare)"""
  yield "origin", arr

  def partition(left: int, right: int) -> int:
    pivot = arr[left]  # 选最左元素为基准
    i, j = left, right
    while i < j:
      # 右指针左移，找小于基准的值
      while i < j:
        yield "compare", (left, j)
        if arr[j] >= pivot:
          j -= 1
        else: break
      # 左指针右移，找大于基准的值
      while i < j:
        yield "compare", (i, left)
        if arr[i] <= pivot:
          i += 1
        else: break
      arr[i], arr[j] = arr[j], arr[i]  # 交换左右指针指向的元素
      yield "swap", (i, j, arr)
    arr[left], arr[i] = arr[i], arr[left]  # 基准值归位
    yield "swap", (i, left, arr)
    return i  # 返回基准值最终位置

  def quickSort(left: int, right: int):
    if left < right:
      # 调用Hoare分区，获取基准值位置
      pivot_idx = yield from partition(left, right)
      # 递归排序左侧子数组（left到pivot_idx-1）
      yield from quickSort(left, pivot_idx - 1)
      # 递归排序右侧子数组（pivot_idx+1到right）
      yield from quickSort(pivot_idx + 1, right)

  yield from quickSort(0, len(arr) - 1)


def quickPointerSort(arr: list):
  """快速排序(前后指针)"""
  yield "origin", arr

  def pointerPartition(left, right):
    pivot = arr[left]
    prev = left  # 前指针
    for curr in range(left + 1, right + 1):
      yield "compare", (curr, left)
      if arr[curr] < pivot:
        prev += 1
        arr[prev], arr[curr] = arr[curr], arr[prev]
        yield "swap", (prev, curr, arr)
    arr[left], arr[prev] = arr[prev], arr[left]  # 基准值归位
    yield "swap", (left, prev, arr)
    return prev

  def quickSort(left: int, right: int):
    if left < right:
      # 调用Hoare分区，获取基准值位置
      pivot_idx = yield from pointerPartition(left, right)
      # 递归排序左侧子数组（left到pivot_idx-1）
      yield from quickSort(left, pivot_idx - 1)
      # 递归排序右侧子数组（pivot_idx+1到right）
      yield from quickSort(pivot_idx + 1, right)

  yield from quickSort(0, len(arr) - 1)


def quickHoleSort(arr: list):
  """快速排序(挖坑法)"""
  yield "origin", arr

  def holePartition(arr, left, right):
    pivot = arr[left]  # 取出基准值，left位置形成"坑"
    i, j = left, right
    while i < j:
      # 从右向左找小于基准的值，填左坑
      while i < j:
        yield "compare", (j, left)
        if arr[j] >= pivot:
          j -= 1
        else: break
      arr[i] = arr[j]  # j位置形成新坑
      yield "swap", (i, j, arr)
      # 从左向右找大于基准的值，填右坑
      while i < j:
        if arr[i] <= pivot:
          yield "compare", (i, left)
          i += 1
        else: break
      arr[j] = arr[i]  # i位置形成新坑
      yield "swap", (i, j, arr)
    arr[i] = pivot  # 基准值填入最后一个坑
    yield "swap", (i, left, arr)
    return i

  def quickSort(left: int, right: int):
    if left < right:
      pivot_idx = yield from holePartition(arr, left, right)
      yield from quickSort(left, pivot_idx - 1)
      yield from quickSort(pivot_idx + 1, right)

  yield from quickSort(0, len(arr) - 1)


def createGif(iterable: iter, savePath: str):
  imgs = []
  ys = None
  info = {
    "compare": 0,
    "swap": 0
  }

  while True:
    try:
      buf = io.BytesIO()
      plt.figure()
      colors = None

      kinds, data = next(iterable)
      if kinds == "origin":
        ys = data
        colors = ["blue"] * len(ys)
      elif kinds == "info":
        info = {**info, **data}
        plt.close()
        continue
      elif kinds == "compare":
        compare = data
        info["compare"] += 1
        colors = ["blue"] * len(ys)
        colors[compare[0]] = "yellow"
        colors[compare[1]] = "yellow"
      elif kinds == "swap":
        swap1, swap2, ys = data
        info["swap"] += 1
        colors = ["blue"] * len(ys)
        colors[swap1] = "green"
        colors[swap2] = "green"
      plt.bar(range(len(ys)), ys, color=colors)
      plt.text(0.05, 0.9, str(info), transform=plt.gca().transAxes)
      plt.savefig(buf, format='png')
      buf.seek(0)
      image = Image.open(buf)
      imgs.append(image)
      plt.close()

    except StopIteration:
      break

  imgs[0].save(savePath, save_all=True, append_images=imgs[1:], duration=50, loop=1)
  print("done")


if __name__ == '__main__':
  seq = generateRandomRange(100)

  createGif(quickPointerSort(seq), r"C:\Users\刘高瞻\Desktop\quickPointerSort.gif")
