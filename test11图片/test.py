from test1ImageInfo import *
from test9算法.test1数据计算.test8矩阵 import *

img = Image.open("file/ruby.png")

r, g, b = img.split()
r, g, b = getPixelData(r), getPixelData(g), getPixelData(b)
r = [[i[0] for i in j] for j in r]
g = [[i[0] for i in j] for j in g]
b = [[i[0] for i in j] for j in b]
r, g, b = np.array(r), np.array(g), np.array(b)

r = matrixPooling(r, (2**7, 2**7), (2**7, 2**7), 'min')
g = matrixPooling(g, (2**7, 2**7), (2**7, 2**7), 'min')
b = matrixPooling(b, (2**7, 2**7), (2**7, 2**7), 'min')

new = [[(r[i][j], g[i][j], b[i][j]) for j in range(len(r[0]))] for i in range(len(r))]
img = drawPixel(new)
fig, axs = plt.subplots(1, 1)
show(img, axs)
plt.show()
