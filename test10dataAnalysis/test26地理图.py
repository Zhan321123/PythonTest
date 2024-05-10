import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")

plt.figure()
plt.subplot(projection="aitoff")
plt.title("Aitoff")
plt.grid(True)

plt.show()