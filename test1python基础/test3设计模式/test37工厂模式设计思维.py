"""
工厂模式的设计思维
"""


class Factory:
    @staticmethod
    def create(goodId):
        if goodId == 0:
            return Milk(500)
        elif goodId == 1:
            return Bread(10)
        elif goodId == 2:
            return Cup('glass')


class Milk:
    def __init__(self, capacity):
        self.capacity = capacity


class Bread:
    def __init__(self, value):
        self.value = value


class Cup:
    def __init__(self, material):
        self.material = material

c = Factory.create(2)
print(c)