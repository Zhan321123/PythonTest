"""
单例创建的设计模式
对于创建对象占用太多资源的类，确保每次新建对象时都是调用了已经创建了的对象
"""


class Reader:
    reader = None
    exist = False

    def __new__(cls, *args, **kwargs):
        if cls.reader == None:
            cls.reader = object.__new__(cls)
        return cls.reader

    def __init__(self, name):
        if not self.exist:
            self.name = name
            Reader.exist = True


r1 = Reader('fuck')
r2 = Reader('shit')
r3 = Reader('fart')

for i in (r1, r2, r3):
    print(i)
print(r1 is r2 is r3)
