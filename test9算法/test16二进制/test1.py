"""
类型
  char
  byte
  short
  int
  long
  float
  double
  bool

运算
  <<
  >>
  !
  &
  %
  |

编码
  binary
  decimal
  hexadecimal

问题
  +
  -
  *
  /
  <
  >

转码
  原码
  补码
  反码

"""
from binary import *


class Byte(BinaryByte):
  def __init__(self, value):
    self.bins = [0, 0, 0, 0, 0, 0, 0, 0]
    if isinstance(value, int):
      if value <-128 or value > 127:
        raise Exception("Invalid value")
      elif value<0:
        self.bins[0] = 1
      self.bins[1:] = [int(i) for i in bin(value)[2:]]
    elif isinstance(value, list):
      self.bins = value
    else:
      raise Exception("Invalid value")

  def __str__(self):
    return f'{"".join([str(i) for i in self.bins])} - value:'

class Integer(BinaryInteger):
  def __init__(self):
    pass