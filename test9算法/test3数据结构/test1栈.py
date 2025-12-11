class Stack:
  """
  栈
  """

  def push(self, value) -> None:
    """
    入栈

    :param value:
    :return:
    """

  def pop(self) -> any:
    """
    出栈

    :return:
    """

  def peek(self) -> any:
    """
    查看栈顶元素

    :return:
    """

  def isEmpty(self) -> bool:
    """
    判断栈是否为空

    :return:
    """

  def __str__(self): ...


class LIFOStack(Stack):
  """
  先入后出(LIFO)栈
  """

  def __init__(self):
    self.stack = []

  def push(self, value) -> None:
    self.stack.append(value)

  def pop(self) -> any:
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.stack.pop()

  def peek(self) -> any:
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.stack[-1]

  def isEmpty(self) -> bool:
    return len(self.stack) == 0

  def __str__(self):
    return 'Stack: ' + ' -> '.join([str(i) for i in self.stack])


class MonotonicStack(Stack):
  """
  单调栈
  """

  def __init__(self):
    self.stack = []

  def push(self, value):
    for i in range(len(self.stack) - 1, 0, -1):
      if self.stack[i] > value:
        self.pop()
      else:
        self.stack.append(value)
        break

  def pop(self):
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def __str__(self):
    return 'Stack: ' + ' -> '.join([str(i) for i in self.stack])
