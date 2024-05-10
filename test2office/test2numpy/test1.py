"""
test numpy
"""
import numpy as np
import time


def calculation(n):
    a = np.arange(1, n) ** 2
    b = np.arange(1, n) ** 3
    c = a + b
    print(c)


def testTime(function):
    t1 = time.time()
    print(t1)
    function()
    t2 = time.time()
    print(t2)
    print(f'spending {t2 - t1} seconds')


testTime(lambda: calculation(10000000))
