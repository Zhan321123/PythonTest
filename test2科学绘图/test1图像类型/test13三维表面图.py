import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')


def fxy(u, v):
    R = 30
    r = 10
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v)
    return x, y, z


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    U, V = np.meshgrid(u, v)
    x, y, z = fxy(U, V)
    ax.plot_surface(x, y, z, cmap='rainbow')
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax.zaxis.set_major_locator(plt.MultipleLocator(5))
    ax.set_aspect('equal')

    plt.show()
