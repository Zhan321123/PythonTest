"""
排序

基元：range, len,

方法：
  插入排序
  希尔排序（Knuth间隔）

"""
import copy

from test0utils import *


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


@timing
def bubbleSort(arr: list) -> list:
  """
  冒泡排序

  优点：
    1. 简单
  缺点：
    1. 最慢
  """
  for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr


@timing
def quickHoareSort(arr: list) -> list:
  """快速排序(Hoare)"""

  def hoarePartition(left: int, right: int) -> int:
    pivot = arr[left]  # 选最左元素为基准
    i, j = left, right
    while i < j:
      # 右指针左移，找小于基准的值
      while i < j and arr[j] >= pivot:
        j -= 1
      # 左指针右移，找大于基准的值
      while i < j and arr[i] <= pivot:
        i += 1
      arr[i], arr[j] = arr[j], arr[i]  # 交换左右指针指向的元素
    arr[left], arr[i] = arr[i], arr[left]  # 基准值归位
    return i  # 返回基准值最终位置

  def quickSort(left: int, right: int):
    if left < right:
      # 调用Hoare分区，获取基准值位置
      pivot_idx = hoarePartition(left, right)
      # 递归排序左侧子数组（left到pivot_idx-1）
      quickSort(left, pivot_idx - 1)
      # 递归排序右侧子数组（pivot_idx+1到right）
      quickSort(pivot_idx + 1, right)

  quickSort(0, len(arr) - 1)
  return arr


@timing
def quickPointerSort(arr: list) -> list:
  """
  快速排序(前后指针)
  从第一个开始，将后面大于它的放到前面，每轮比完之后就排序放前面的，然后从其后面排序更大的

  优点：
    1. 所有可比非数字型中最快的
  缺点：
    1. 对接近有序数组反而更慢
    2. 数组量级过大可能会 stack overflow
  """

  def pointerPartition(left, right):
    pivot = arr[left]
    prev = left  # 前指针
    for curr in range(left + 1, right + 1):
      if arr[curr] < pivot:
        prev += 1
        arr[prev], arr[curr] = arr[curr], arr[prev]
    arr[left], arr[prev] = arr[prev], arr[left]  # 基准值归位
    return prev

  def quickSort(left: int, right: int):
    if left < right:
      pivot_idx = pointerPartition(left, right)
      quickSort(left, pivot_idx - 1)
      quickSort(pivot_idx + 1, right)

  quickSort(0, len(arr) - 1)
  return arr


@timing
def quickHoleSort(arr: list) -> list:
  """快速排序(挖坑法)"""

  def holePartition(arr, left, right):
    pivot = arr[left]  # 取出基准值，left位置形成"坑"
    i, j = left, right
    while i < j:
      # 从右向左找小于基准的值，填左坑
      while i < j and arr[j] >= pivot:
        j -= 1
      arr[i] = arr[j]  # j位置形成新坑
      # 从左向右找大于基准的值，填右坑
      while i < j and arr[i] <= pivot:
        i += 1
      arr[j] = arr[i]  # i位置形成新坑
    arr[i] = pivot  # 基准值填入最后一个坑
    return i

  def quickSort(left: int, right: int):
    if left < right:
      pivot_idx = holePartition(arr, left, right)
      quickSort(left, pivot_idx - 1)
      quickSort(pivot_idx + 1, right)

  quickSort(0, len(arr) - 1)
  return arr


@timing
def quickNotRecursiveSort(arr: list) -> list:
  """快速排序(非递归)"""

  def pointerPartition(left, right):
    pivot = arr[left]
    prev = left  # 前指针
    for curr in range(left + 1, right + 1):
      if arr[curr] < pivot:
        prev += 1
        arr[prev], arr[curr] = arr[curr], arr[prev]
    arr[left], arr[prev] = arr[prev], arr[left]  # 基准值归位
    return prev

  if len(arr) <= 1:
    return arr
  stack = []
  stack.append((0, len(arr) - 1))  # 初始边界入栈

  while stack:
    left, right = stack.pop()
    if left >= right:
      continue
    # 用任意分区方法（如前后指针法）获取基准位置
    pivot_idx = pointerPartition(left, right)
    # 左右子数组边界入栈
    stack.append((left, pivot_idx - 1))
    stack.append((pivot_idx + 1, right))
  return arr


@timing
def recursiveSort(arr: list) -> list:
  """
  归并排序(递归法)
  全部拆分为组，每次遍历两个组排序合并为一个组，因为两个组都是有序数组，所以能够采用双指针来快速排序，最终合并为一个组

  优点：
    1. 较快
  """

  def merge(left_arr, right_arr):
    """合并两个有序子数组为一个有序数组"""
    merged = []
    i = j = 0  # i: 左子数组指针，j: 右子数组指针

    # 比较两个子数组的元素，按顺序加入合并数组
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] <= right_arr[j]:
        merged.append(left_arr[i])
        i += 1
      else:
        merged.append(right_arr[j])
        j += 1

    # 追加剩余元素（左或右子数组可能有剩余）
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    return merged
    # 终止条件：子数组长度 ≤ 1 时直接返回

  def recursive(arr):
    if len(arr) <= 1:
      return arr.copy()  # 返回副本避免修改原数组

    # 1. 拆分：从中间分为左右两个子数组
    mid = len(arr) // 2
    left = recursive(arr[:mid])  # 递归拆分左子数组
    right = recursive(arr[mid:])  # 递归拆分右子数组

    # 2. 合并：将两个有序子数组合并为一个有序数组
    return merge(left, right)

  return recursive(arr)


@timing
def nonRecursiveSort(arr: list) -> list:
  """归并排序(非递归)"""

  def merge(left_arr, right_arr):
    merged = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] <= right_arr[j]:
        merged.append(left_arr[i])
        i += 1
      else:
        merged.append(right_arr[j])
        j += 1
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    return merged

  arr = arr.copy()  # 复制数组避免修改原数据
  n = len(arr)
  step = 1  # 初始合并步长（子数组长度为1）

  while step < n:
    # 按当前步长遍历数组，合并相邻子数组
    for i in range(0, n, 2 * step):
      # 确定左、右子数组的范围
      left_start = i
      left_end = i + step  # 左子数组：[left_start, left_end)
      right_start = left_end
      right_end = min(i + 2 * step, n)  # 右子数组：[right_start, right_end)

      # 提取左、右子数组（已按上一步合并为有序）
      left = arr[left_start:left_end]
      right = arr[right_start:right_end]

      # 合并左、右子数组，并写回原数组
      merged = merge(left, right)
      arr[left_start:right_end] = merged

    # 步长翻倍（下次合并的子数组长度为当前的2倍）
    step *= 2

  return arr


@timing
def countSort(arr: list[int]) -> list:
  """
  计数排序
  从最低到最高统计每个数出现的次数，然后合并

  优点：
    1. 极快
  限制：
    1. 仅支持整数
    2. 需额外空间
  适用于：
    1. 数据范围远小于数据量，且都为整数
  应用举例：
    1. 一百万河南考生的高考成绩，数据量10^6 >> 数据范围750
  """
  min_val = min(arr)
  max_val = max(arr)
  range_size = max_val - min_val + 1

  # 2. 统计次数
  count = [0] * range_size
  for num in arr:
    count[num - min_val] += 1

  # 3. 计数数组转为前缀和（确定元素的最终位置范围）
  for i in range(1, range_size):
    count[i] += count[i - 1]  # count[i] 现在是“小于等于 i+min_val 的元素总数”

  # 4. 反向遍历原数组，填充结果（保证稳定性）
  result = [0] * len(arr)  # 用新数组存储结果，避免覆盖原数组
  for num in reversed(arr):
    # 计算当前元素在结果数组中的索引
    idx = count[num - min_val] - 1
    result[idx] = num
    count[num - min_val] -= 1  # 下一个相同元素的位置左移1位

  # 5. 将结果复制回原数组（可选，根据需求决定是否修改原数组）
  arr[:] = result
  return arr


@timing
def cardinalSort(arr: list[int]) -> list:
  """
  基数排序
  从最高位到百位，十位，个位依次比较并排序

  优点：
    1. 极快，但比计数排序略慢
    2. 相比于计数排序，不限制数据范围
  限制：
    1. 仅支持非负整数
    2. 需额外空间
  适用于：
    1. 数据都是非负整数
  应用举例：
    1. 一亿电话号码排序，数据量10^8 << 数据范围10^11
  """
  if not arr or len(arr) <= 1:
    return arr.copy()

    # 1. 找到数组中的最大元素，确定最大位数
  max_num = max(arr)
  max_digit = 0
  while max_num > 0:
    max_num //= 10
    max_digit += 1

  # 2. 初始化基数（10^d，d从0开始，对应个位、十位、百位...）
  radix = 1
  # 复制原数组，避免修改输入
  sorted_arr = arr.copy()

  # 3. 按位排序（从最低位到最高位）
  for _ in range(max_digit):
    # 步骤A：计数排序的“计数数组”（0-9共10个数字）
    count = [0] * 10
    # 统计每个位值的出现次数
    for num in sorted_arr:
      digit_val = (num // radix) % 10  # 求当前位的值
      count[digit_val] += 1

    # 步骤B：将计数数组转为“前缀和”，确定每个元素的最终位置（保证稳定性）
    for i in range(1, 10):
      count[i] += count[i - 1]

    # 步骤C：从后往前遍历（关键！保证计数排序的稳定性）
    temp = [0] * len(sorted_arr)
    for num in reversed(sorted_arr):
      digit_val = (num // radix) % 10
      count[digit_val] -= 1  # 前缀和减1，得到当前元素的索引
      temp[count[digit_val]] = num

    # 步骤D：将临时数组复制回sorted_arr，准备下一轮排序
    sorted_arr = temp
    # 基数扩大10倍，处理下一位（个位→十位→百位...）
    radix *= 10

  return sorted_arr


@timing
def bucketSort(arr: list) -> list:
  """
  桶排序
  分治策略，给定范围划分为从小到大的桶，并将数据分别放入其中，然后对每个桶进行"其他排序"，最后合并

  优点：
    1. 极快
  限制：
    1. 仅支持数字
    2. 数据分布比较均匀，若出现极端数字，会严重影响速度，塌缩为"其他排序"
  适用于：
    1. 分布均匀的数组
  应用举例：
    1. 人的身高排序，虽然呈现正态分布，但是较均匀，且没有极端数据
  """
  if len(arr) <= 1:
    return arr

    # 2. 确定数据范围，设计桶
  min_val = min(arr)
  max_val = max(arr)
  bucket_count = len(arr)  # 桶的数量设为数据量（常用策略）
  bucket_size = (max_val - min_val) / bucket_count  # 每个桶的区间大小

  # 3. 初始化桶（列表的列表，每个子列表代表一个桶）
  buckets = [[] for _ in range(bucket_count)]

  # 4. 数据分配：将元素放入对应桶中
  for x in arr:
    # 计算桶索引（避免索引越界，最后一个元素放入最后一个桶）
    idx = int((x - min_val) / bucket_size)
    idx = min(idx, bucket_count - 1)
    buckets[idx].append(x)

  # 5. 桶内排序（使用插入排序）+ 合并结果
  sorted_arr = []
  for bucket in buckets:
    # 对每个非空桶进行插入排序
    if bucket:
      # 插入排序实现
      for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
          bucket[j + 1] = bucket[j]
          j -= 1
        bucket[j + 1] = key
      # 将排序后的桶元素合并
      sorted_arr.extend(bucket)

  return sorted_arr

@timing
def sortSort(arr: list):
  arr.sort()
  return arr

if __name__ == '__main__':
  seq = generateRandomStrings(10000, 10)
  # seq = generateRandomSequence(10000, 100)

  sortSort(copy.copy(seq))

  insertSeq = insertSort(copy.copy(seq))
  hillSeq = hillSort(copy.copy(seq))
  selectSeq = selectSort(copy.copy(seq))
  heapSeq = heapSort(copy.copy(seq))
  bubbleSeq = bubbleSort(copy.copy(seq))
  quickHoareSeq = quickHoareSort(copy.copy(seq))
  quickPointerSeq = quickPointerSort(copy.copy(seq))
  quickHoleSeq = quickHoleSort(copy.copy(seq))
  quickNotRecursiveSeq = quickNotRecursiveSort(copy.copy(seq))
  recursiveSeq = recursiveSort(copy.copy(seq))
  nonRecursiveSeq = nonRecursiveSort(copy.copy(seq))
  # bucketSeq = bucketSort(copy.copy(seq))
  # countSeq = countSort(copy.copy(seq))
  # cardinalSeq = cardinalSort(copy.copy(seq))

  print(checkSequence(insertSeq))
  print(checkSequence(hillSeq))
  print(checkSequence(selectSeq))
  print(checkSequence(heapSeq))
  print(checkSequence(bubbleSeq))
  print(checkSequence(quickHoareSeq))
  print(checkSequence(quickPointerSeq))
  print(checkSequence(quickHoleSeq))
  print(checkSequence(quickNotRecursiveSeq))
  print(checkSequence(recursiveSeq))
  print(checkSequence(nonRecursiveSeq))
  # print(checkSequence(bucketSeq))
  # print(checkSequence(countSeq))
  # print(checkSequence(cardinalSeq))

  seq.sort()
  print(seq == insertSeq == hillSeq == selectSeq == heapSeq
        == bubbleSeq == quickHoareSeq == quickPointerSeq == quickHoleSeq
        == quickNotRecursiveSeq == recursiveSeq == nonRecursiveSeq)
  # == bucketSeq        == countSeq      == cardinalSeq )
