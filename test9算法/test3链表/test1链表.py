from linkedList import LinkedList

class SingleLinkedList(LinkedList):
  """
  单链表
  """
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  class Node:
    def __init__(self, value, next: "SingleLinkedList.Node"):
      self.value = value
      self.next = next

  def addFirst(self, value) -> bool:
    node = self.Node(value, self.head)
    if self.size == 0:
      self.tail = node
    self.head = node
    self.size += 1
    return True

  def addLast(self, value) -> bool:
    node = self.Node(value, None)
    if self.size == 0:
      self.head = node
    else:
      self.tail.next = node
    self.tail = node
    self.size += 1
    return True

  def add(self, index, value) -> bool:
    if index < 0 or index > self.size:
      raise IndexError('索引越界')
    if index == 0:
      return self.addFirst(value)
    if index == self.size:
      return self.addLast(value)
    node = self._getNode(index - 1)
    newNode = self.Node(value, node.next)
    node.next = newNode
    self.size += 1
    return True

  def removeFirst(self) -> bool:
    if self.size == 0:
      raise IndexError('链表为空')
    if self.size == 1:
      self.head = None
      self.tail = None
      self.size -= 1
      return True
    self.head = self.head.next
    self.size -= 1
    return True

  def removeLast(self) -> bool:
    if self.size == 0:
      raise IndexError('链表为空')
    if self.size == 1:
      self.head = None
      self.tail = None
      self.size -= 1
      return True
    node = self._getNode(self.size - 2)
    node.next = None
    self.tail = node
    self.size -= 1
    return True

  def remove(self, index) -> bool:
    if index < 0 or index >= self.size:
      raise IndexError('索引越界')
    if index == 0:
      return self.removeFirst()
    node = self._getNode(index - 1)
    node.next = node.next.next
    self.size -= 1
    return True

  def _getNode(self, index) -> any:
    if index < 0 or index >= self.size:
      raise IndexError('索引越界')
    node = self.head
    for i in range(index):
      node = node.next
    return node

  def get(self, index) -> any:
    return self._getNode(index).value

  def getFirst(self) -> any:
    if self.size == 0:
      raise IndexError('链表为空')
    return self.head.value

  def getLast(self) -> any:
    if self.size == 0:
      raise IndexError('链表为空')
    return self.tail.value

  def set(self, index, value) -> bool:
    if index < 0 or index >= self.size:
      raise IndexError('索引越界')
    pre_node = self._getNode(index - 1)
    next_node = pre_node.next.next
    node = self.Node(value, next_node)
    pre_node.next = node
    return True

  def size(self) -> int:
    return self.size

  def isEmpty(self) -> bool:
    return self.size == 0

  def clear(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0

  def indexOf(self, value) -> int:
    for i in range(self.size):
      if self._getNode(i).value == value:
        return i
    return -1

  def __str__(self):
    l = []
    node = self.head
    while node:
      l.append(node.value)
      node = node.next
    return 'SingledLinkedList[ ' + ' -> '.join(map(str, l)) + ' ]'

class DoubleLinkedList(LinkedList):
  """
  双链表
  TODO
  """
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  class Node:
    def __init__(self, value, prev: "DoubleLinkedList.Node", next: "DoubleLinkedList.Node"):
      self.value = value
      self.prev = prev
      self.next = next
