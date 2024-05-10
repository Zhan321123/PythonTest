"""
An = n
Sn = ∑(An,1,n)
求：Sn = Sm-Sn 的整数解：
n m,

2, 3,
14, 20,
84, 119,
492, 696,
2870, 4059,
16730, 23660,
97512, 137903,
568344, 803760,
3312554, 4684659,
19306982, 27304196,
65918161, 93222357,
104532126, 147830750,
112529340, 159140519,
120526554, 170450287,
159140519, 225058680,
167137733, 236368448,
197754484, 279667073,
205751698, 290976841,

"""
import math


# 求Sn
def sum_n(n: int):
    sun = 0
    for i in range(1, n + 1):
        sun += i
    return sun


# 由Sn求n
def n_sum(sn: int):
    n = 0
    for i in range(1, sn + 1):
        n += i
        if n == sn:
            return i
        elif n > sn:
            return i - 1


i = 1
while True:
    if math.sqrt(8 * i * (i + 1) + 1) % 1 == 0:
        m = n_sum(2 * sum_n(i))
        print(i, ",", m, ",")

    i += 1
