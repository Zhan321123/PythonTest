a = tuple((x, y) for x in range(1, 17) for y in range(1, 17))
for i in range(0, 16):
    for j in range(0, 16):
        print(a[i * 16 + j], end='  \t')
    print()

s = 'x am zhan, x love minecraft, x dont love family'
a = tuple(s)
char={i:s.count(i) for i in s}
print(char)
