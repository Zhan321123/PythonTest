"""
@staticmethod 类中的静态方法，但是不能使用类中的属性
@classmethod 不用创建对象就能使用的方法，可以通过“cls.属性”调用类的的属性

"""
class Stu:
    n = 'what'

    # staticmethod定义静态方法，不用创建对象就能使用的方法，不能使用类的属性的方法
    @staticmethod
    def speak(a, b):
        print(a)
        print(b)

    # classmethod定义类方法，不用创建对象就能使用的方法
    # 默认第一个参数为cls，不用管
    # 可以通过“cls.属性”调用类的的属性
    @classmethod
    def say(cls):
        print(cls.n)


Stu.speak('fuck', 'you')
Stu.say()
