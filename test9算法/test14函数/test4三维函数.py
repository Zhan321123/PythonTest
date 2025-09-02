import matplotlib.pyplot as plt

from test2drawThreeDimension import *

def torus(R=30, r=10):
    """
    圆环体
    :param R: 大半径
    :param r: 小圆半径
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    U, V = np.meshgrid(u, v)
    x = (R + r * np.cos(V)) * np.cos(U)
    y = (R + r * np.cos(V)) * np.sin(U)
    z = r * np.sin(V)
    return x, y, z


def water(a=1, b=1):
    """
    水滴
    :param a: 整体大小
    :param b: 扁平或尖锐程度
    """
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    T, P = np.meshgrid(theta, phi)
    r = lambda theta: a * (1 + b * np.cos(theta))
    x = r(T) * np.sin(T) * np.cos(P)
    y = r(T) * np.sin(T) * np.sin(P)
    z = r(T) * np.cos(T)
    return x, y, z

if __name__ == '__main__':
    fig,ax = plt.subplots()
    x,y,z = water()
    graph(ax,x,y,z)
    plt.show()