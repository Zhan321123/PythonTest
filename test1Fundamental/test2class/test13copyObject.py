"""
测试copy对象和deepcopy对象
copy：对象新的地址，但是引用原来的属性
deepcopy：对象新的地址，属性也是复制新的一份
"""
from copy import copy, deepcopy


class Computer:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

    def play(self):
        print('play game')

    def feigning(self):
        print('the configuration of my computer is {0},{1},{2}'.format(id(self), id(self.cpu), id(self.screen)))


class Cpu:
    def __init__(self, efficiency):
        self.efficiency = efficiency

    def work(self):
        print('cpu smoking')


class Screen:
    def __init__(self, size):
        self.size = size

    def show(self):
        print('screen lit up')


c = Cpu(10)
s = Screen(1080)
computer = Computer(c, s)
computer.feigning()

# 测试浅拷贝，属性还是那个属性
computer1 = copy(computer)
computer1.feigning()

# 测试深拷贝，属性完全复制一份新的
computer2 = deepcopy(computer)
computer2.feigning()
