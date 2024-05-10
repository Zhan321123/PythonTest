pi = 3.14
e = 2.7
mol = 6.2


def add(a, b):
    return a + b


def divide(a, b):
    return a - b


def multiply(a, b):
    return a * b


class C1:
    def __init__(self, id):
        self.id = id

    def fuck(self):
        print('object s id is {0}'.format(self.id))
