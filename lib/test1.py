import numpy as np
from matplotlib import pyplot as plt


a = np.array([1,2,3])
print(a.shape)
print(np.tile(a,2))

fig,ax = plt.subplots()
plt.savefig("test.png")