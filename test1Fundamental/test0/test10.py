import random

for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + '*' + str(i) + '=' + str(i * j), end='\t')
    print()

# for下的else，当for语句没有被break时，else会执行
for i in range(1, 11):
    a = random.randint(0, 10)
    print(a)
    if a == 5:
        break
else:
    print('successful')

#
a = ('zhan', 'xiao', 'duo')
b = (12, 34, 56)
c = ('male', 'female', 'male')
for i, j, k in zip(a, b, c):
    print('{0}-{1}-{2}'.format(i,j,k))
