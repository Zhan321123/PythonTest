from typing import Sequence

from sklearn import linear_model

from test1python基础.test1.test35类属性 import printObject, printAttribute


def logisticFitting(xs: Sequence, ys: Sequence):
  """
  逻辑回归

  :param xs:
  :param ys:
  :return:
  """
  model = linear_model.LogisticRegression()
  xss = tuple(map(lambda x: (x,), xs))
  model.fit(xss, ys)
  printObject(model)

def mulLogisticFitting(xss: Sequence, ys: Sequence):
  """
  多特征逻辑回归

  :param xss:
  :param ys:
  :return:
  """
  model = linear_model.LogisticRegression()
  model.fit(xss, ys)
  printAttribute(model)

if __name__ == '__main__':
  x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  x2 = [
    [1, 6, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 6, 4],
    [4, 5, 6, 7],
    [5, 6, 7, 8],
    [6, 7, 5, 9],
    [7, 8, 9, 10],
    [8, 1, 10, 11],
    [9, 13, 2, 12],
    [10, 11, 12, 18]
  ]
  y1 = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
  y2 = [0, 1, 0, 0, 1, 0, 1, 2, 1, 2]
  mulLogisticFitting(x2, y2)
