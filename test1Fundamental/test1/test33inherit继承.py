"""
测试类的继承和多继承
所有类继承Object
测试父类方法的重写
"""


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
