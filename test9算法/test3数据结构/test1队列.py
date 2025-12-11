from typing import Any


class Queue:
  """
  队列
  """

  def enqueue(self, item: Any) -> None:
    """
    入队

    :param item:
    :return:
    """

  def dequeue(self) -> Any:
    """
    出队

    :return:
    """

  def size(self) -> int:
    """
    队列长度

    :return:
    """

  def isEmpty(self) -> bool:
    """
    队列是否为空

    :return:
    """

  def __str__(self): ...


class DoubleQueue:
  """
  双端队列
  """

  def enqueueToHead(self, item: Any) -> None:
    """
    入队头

    :param item:
    :return:
    """

  def enqueueToTail(self, item: Any) -> None:
    """
    入队尾

    :param item:
    :return:
    """

  def dequeueHead(self) -> Any:
    """
    队头出

    :return:
    """

  def dequeueTail(self) -> Any:
    """
    队尾出

    :return:
    """

  def size(self) -> int:
    """
    队列长度

    :return:
    """

  def isEmpty(self) -> bool:
    """
    队列是否为空

    :return:
    """

  def __str__(self): ...


class FIFOQueue(Queue):
  """
  先入先出(FIFO)队列
  """

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  class Node:
    def __init__(self, value, next):
      self.value = value
      self.next = next

  def enqueue(self, value) -> None:
    if self.isEmpty():
      self.head = self.tail = self.Node(value, None)
    else:
      self.tail.next = self.Node(value, None)
      self.tail = self.tail.next
    self.length += 1

  def dequeue(self) -> any:
    if self.isEmpty():
      raise IndexError('队列为空')
    value = self.head.value
    if self.head is self.tail:
      self.head = self.tail = None
    else:
      self.head = self.head.next
    self.length -= 1
    return value

  def isEmpty(self) -> bool:
    return self.length == 0

  def peek(self) -> any:
    return self.head.value

  def size(self) -> int:
    return self.length

  def __str__(self):
    queue = []
    head = self.head
    while head is not None:
      queue.append(head.value)
      head = head.next
    return f"FIFOQueue:[ {'->'.join(queue)} ]"


class DoubleEndedQueue(DoubleQueue):
  """
  双端队列
  """

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  class Node:
    def __init__(self, value, prev, next):
      self.value = value
      self.prev = prev
      self.next = next

  def enqueueToHead(self, item):
    if self.isEmpty():
      self.head = self.tail = self.Node(item, None, None)
    else:
      node = self.Node(item, None, self.head)
      self.head.prev = node
      self.head = node

  def enqueueToTail(self, item):
    if self.isEmpty():
      self.head = self.tail = self.Node(item, None, None)
    else:
      node = self.Node(item, self.tail, None)
      self.tail.next = node
      self.tail = node
    self.length += 1

  def dequeueHead(self):
    if self.isEmpty():
      raise IndexError('队列为空')
    value = self.head.value
    if self.head is self.tail:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
    self.length -= 1
    return value

  def dequeueTail(self):
    if self.isEmpty():
      raise IndexError('队列为空')
    value = self.tail.value
    if self.head is self.tail:
      self.head = self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    self.length -= 1
    return value

  def size(self):
    return self.length

  def isEmpty(self):
    return self.length == 0

  def __str__(self):
    queue = []
    head = self.head
    while head is not None:
      queue.append(head.value)
      head = head.next
    return f"FIFOQueue:[ {'<->'.join(queue)} ]"
