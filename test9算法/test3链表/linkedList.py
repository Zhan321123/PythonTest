class LinkedList:
  """
  链表
  """

  def addFirst(self, value) -> bool:
    """
    将元素插入头位置

    :param value:
    :return:
    """

  def addLast(self, value) -> bool:
    """
    将元素插入尾位置

    :param value:
    :return:
    """

  def add(self, index, value) -> bool:
    """
    将元素插入指定位置

    :param index: 索引位置
    :param value:
    :return:
    """

  def removeFirst(self) -> bool:
    """
    删除头元素

    :return:
    """

  def removeLast(self) -> bool:
    """
    删除尾元素

    :return:
    """

  def remove(self, index) -> bool:
    """
    删除指定位置的元素

    :param index: 索引位置
    :return:
    """

  def get(self, index) -> any:
    """
    获取指定位置的元素

    :param index: 索引位置
    :return:
    """

  def getFirst(self) -> any:
    """
    获取头元素

    :return:
    """

  def getLast(self) -> any:
    """
    获取尾元素

    :return:
    """

  def set(self, index, value) -> bool:
    """
    修改指定位置的元素

    :param index: 索引位置
    :param value:
    :return:
    """

  def indexOf(self, value) -> int:
    """
    获取指定元素的索引位置

    :param value:
    :return:
    """

  def size(self) -> int:
    """
    获取链表长度

    :return:
    """

  def isEmpty(self) -> bool:
    """
    判断链表是否为空

    :return:
    """

  def clear(self) -> None:
    """
    清空链表

    :return:
    """

  def __str__(self): ...
