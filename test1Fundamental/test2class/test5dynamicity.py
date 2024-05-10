"""
测试方法的动态性
可以随意修改对象的方法，添加，修改
"""
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