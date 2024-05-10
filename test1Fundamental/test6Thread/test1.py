"""
测试多线程的进程属性
"""
# 导入多线程包
from multiprocessing import Process


def f1(age, name):
    print(name)
    print(age)


def f2():
    print(123)

# 多线程中一定呀使用main方法
if __name__ == '__main__':
    # Process(target=function,args=(参数))
    # 新建线程
    p1 = Process(target=f1, args=(18, 'fuck',))
    print(p1.pid)
    # 线程开始
    p1.start()
    # 主线程等待子线程的时间
    p1.join(0)

    p2 = Process(target=f2)
    p2.start()
    p2.join()
