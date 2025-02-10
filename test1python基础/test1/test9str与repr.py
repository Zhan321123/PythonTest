class Obj:
    def __init__(self):
        pass

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


o = Obj()
print(o)
print(repr(o))
print(str(o))
print([o, Obj()])
