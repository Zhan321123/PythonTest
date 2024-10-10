"""
class类对象
    属性重名时只使用最后一个定义的属性，包括方法
    所有类继承Object

超类Object的方法：
    对象
        __init__构造器
        __call__对象变成方法时执行
        __str__打印对象，输出对象，tostring

    符号方法
        __add__         +
        __sub__         -
        __mul__         *
        __div__         /
        __floordiv__    //
        __pow__         **
        __getitem__     []
        __mod__         %
        __and__         &
        __or__          |
        __xor__         ^
        __lshift__      <<
        __rshift__      >>
        __invert__      ~
        __ne__          !=
        __eq__          ==
        __lt__          <
        __le__          <=
        __gt__          >
        __ge__          >=

    拷贝
        __copy__        浅拷贝copy.copy(object)
        __deepcopy__    深拷贝copy.deepcopy(object)

继承和多继承


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


t = 'test'
_t = '_test'
__t = '__test'
__t__ = '__test__'

print("-------------------inherit----------------")

class Animal:

    def __init__(self, name):
        self.name = name

    def die(self):
        print(self.name + ' die')


# 继承类，类名(父类名)
class Dog(Animal):
    def __init__(self, name, breed):
        # super()调用父类
        super().__init__(name)
        self.breed = breed

    def shout(self):
        print('dog wang!!!')


d = Dog('yellow', 1)
d.shout()
d.die()
# mro函数，列出该类的继承结构
print(Dog.mro())


class Cat(Animal):
    def die(self):
        super().die()
        print('i have 9 lives')


# 没有构造器的类会使用父类的构造器
c = Cat('flower')
c.die()


class A:
    def a(self):
        print('a')

    def say(self):
        print('AAA')


class B:
    def b(self):
        print('b')

    def say(self):
        print('BBB')


# 多继承
class C(A, B):
    def c(self):
        print('c')

    def shout(self):
        # 调用父类方法的两种方法
        # super().method()
        super().say()
        # class.method(object)
        B.say(self)
        print('CCC')


c = C()
c.a()
c.b()
c.c()
# 当继承多个父类有重名的方法时，调用括号内靠前的类
c.say()
c.shout()

print("-------------------------------------")
class Fraction:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self.value + other.value
        elif isinstance(other, int):
            return self.value * other
        else:
            return "can't mul"


f1 = Fraction('1/2')
f2 = Fraction('2/3')
print(f1 * f2)
print(f1 * 3)