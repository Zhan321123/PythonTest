import math


class ActivateFunctions:
  @staticmethod
  def sigmoid(x):
    return 1 / (1 + math.exp(-x))

  @staticmethod
  def tanh(x):
    return math.tanh(x)

  @staticmethod
  def reLU(x):
    return max(0, x)

  @staticmethod
  def leakyReLU(x):
    return max(0.01 * x, x)


class ActivateDerivatives:
  @staticmethod
  def sigmoid(x):
    return x * (1 - x)

  @staticmethod
  def tanh(x):
    return 1 - x ** 2

  @staticmethod
  def reLU(x):
    return 1 if x > 0 else 0

  @staticmethod
  def leakyReLU(x):
    return 1 if x > 0 else 0.01


if __name__ == '__main__':
   print(ActivateFunctions.sigmoid(1))
   print(ActivateDerivatives.sigmoid(1))