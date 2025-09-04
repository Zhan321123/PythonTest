import copy
import io

from PIL import Image
from matplotlib import pyplot as plt

from test0 import *


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
  seq = generateRandomRange(16)

  createGif(heapSort(seq), r"C:\Users\刘高瞻\Desktop\heapSort.gif")
