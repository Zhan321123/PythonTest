"""
class类对象
属性重名时只使用最后一个定义的属性，包括方法

object def
    __init__构造器
    __call__对象变成方法时执行
    __str__打印对象，输出对象，tostring


"""
class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def say(self):
        return self.name + ' fuck you'


s1 = Student('zhan', 120, 2022)
print(s1.say())
print(s1.name)
s1.age = 12
print(s1.age)

# 解释器调用方法：class.method(对象self)
print(Student.say(s1))

# dir获取该对象类的所有方法和属性
for i in dir(s1):
    print(i)
print(dir(s1))


class Genshin:
    pass


print(isinstance(s1, Student))
print(isinstance(s1, Genshin))

print(type(s1))
print(type(Student))


print("------------call----------------")
class Stu:

    # call，对象变成方法使用时执行
    def __call__(self, *args, **kwargs):
        print('call method')


s1 = Stu()
# 这里直接将对象变成方法使用
s1()


print("-------------重栽-------------------")
class Stu:
    def fuck(self):
        print('fuck')

    def fuck(self,name):
        print(name+'fuck')


s1 = Stu()
# s1.fuck()
s1.fuck('zhan')

print("-----------------方法的动态性--------------------")
# 可任意添加、修改、删除方法
class Stu:
    def work(self):
        print('working hard')


def play():
    print('playing game')

s = Stu()
s.work()

# 直接将方法赋予对象
s.playGame = play
s.playGame()
# 直接修改对象的方法
s.work=play
s.work()