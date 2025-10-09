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
