"""
Bezier曲线
"""
import math
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


# def Amn(over: int, under: int) -> int:
#     """:math:`A_under^over`"""
#     return math.factorial(under) // math.factorial(under - over)
#
#
# def Cmn(over: int, under: int) -> int:
#     """:math:`C_under^over`"""
#     return Amn(over, under) // math.factorial(over)


class Bezier:
    def __init__(self, points: [[]]):
        self.points = points
        self.n = len(points) - 1

    def curve(self, t: float) -> [float]:
        points, n = self.points, self.n
        result = list(sum(math.comb(n, i) * (1 - t) ** (n - i) * t ** i * points[i][j] for i in range(n + 1)) for j in
                      range(len(points[0])))
        return result

    def appendPoint(self, point: [float]):
        self.points.append(point)
        self.n += 1

    def _rang(self, quantity: int = 100) -> [float]:
        return [i / quantity for i in range(quantity + 1)]

    def getCoordinate(self, quantity: int = 100) -> [[]]:
        return [self.curve(i) for i in self._rang(quantity)]

    def draw(self, ax: plt.Axes):
        """仅支持二维"""
        if len(self.points[0]) != 2:
            raise ValueError('仅支持二维')
        xs, ys = list(zip(*self.getCoordinate()))
        ax.plot(xs, ys, '-', color='red', label='bezier curve')
        ax.plot(*list(zip(*ps)), '-.', color='green')
        ax.scatter(*list(zip(*ps)), color='blue', label='control points')
        ax.grid()
        ax.set_aspect("equal")
        ax.legend()


class SubBezier:
    def __init__(self, pointss: [[[]]]):
        self.pointss = pointss
        self.ns = list(len(points) - 1 for points in self.pointss)
        self.colors = ['red', 'green', 'blue', 'orange', 'brown', 'yellow', 'purple', 'pink', ]

    def curve(self, t: float) -> [float]:
        points, ns = self.pointss, self.ns
        results = list(
            list(
                sum(math.comb(ns[k], i) * (1 - t) ** (ns[k] - i) * t ** i * points[k][i][j]
                    for i in range(ns[k] + 1)) for j in range(len(points[k][0]))
            )
            for k in range(len(ns)))
        return results

    def _rang(self, quantity: int = 100) -> [float]:
        return [i / quantity for i in range(quantity + 1)]

    def getCoordinate(self, quantity: int = 100) -> [[]]:
        return [self.curve(i) for i in self._rang(quantity)]

    def draw(self, ax: plt.Axes):
        for index, s in enumerate(list(zip(*self.getCoordinate()))):
            xs, ys = list(zip(*s))
            ax.plot(xs, ys, color=self.colors[index])
            ax.scatter(*list(zip(*ps[index])), color=self.colors[index])
            ax.plot(*list(zip(*ps[index])), color=self.colors[index])
        ax.grid()
        ax.set_aspect("equal")


if __name__ == '__main__':
    fig, axs = plt.subplots()

    # ps = [[0, 0], [1, 0], [1, 1.8], [-1, 1.8], [-1, 0], [0, 0]]
    # ps = [[0,0],[0,1],[1,0],[1,1]]
    ps = [
        [[0, 1], [0, 0.4], [0.4, 0], [1, 0]],
        [[1, 0], [1.6, 0], [2, 0.4], [2, 1]],
        [[2, 1], [2, 1.6], [1.6, 2], [1, 2]],
        [[1, 2], [0.4, 2], [0, 1.6], [0, 1]]
    ]
    bz = SubBezier(ps)
    bz.draw(axs)
    plt.show()
