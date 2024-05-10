import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 10)
v = np.linspace(0, np.pi, 10)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

print("x", x)
print("y", y)
print("z", z)
print("u", u)
print("v", v)

# Plot the surface
ax.plot_surface(x, y, z)

# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()
