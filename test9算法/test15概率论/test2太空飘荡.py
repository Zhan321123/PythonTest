from math import *
from random import random

from matplotlib import pyplot as plt

x, y = 0, 0
vx, vy = 0, 0
positionXs = []
positionYs = []

for i in range(1000):
  ax = random() - 0.5
  ay = random() - 0.5
  vx += ax
  vy += ay
  x += vx
  y += vy
  positionXs.append(x)
  positionYs.append(y)

plt.plot(positionXs, positionYs)
plt.axis('equal')
plt.show()
