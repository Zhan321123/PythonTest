"""
python中描述对象的方法
重写__str__即可
同Java中的tostring
"""


class C:
    def __init__(self):
        self.name = 'zhan'

    def __str__(self):
        return '{0} fuck you'.format(self.name)


o = object
c = C()
print(c)
