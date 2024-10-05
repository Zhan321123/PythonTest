"""
三体运动动态图

"""
import math
import matplotlib
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use('TkAgg')
fig, ax = plt.subplots(figsize=(6, 6))

G = 20  # 引力常数

# star恒星，planet行星
# 位置、速度
starPos = [[2, 2], [8, 20], [30, 9], [15, 15]]
starVel = [[0, 2], [3, 0], [-0.5, 1], [-4, -2]]
starMass = [6, 4, 5, 1]
# Circle(tuple(x,y), 半径radius, color, ...)
star0 = mpatches.Circle(starPos[0], starMass[0] / 5, color='red')
star1 = mpatches.Circle(starPos[1], starMass[1] / 5, color='green')
star2 = mpatches.Circle(starPos[2], starMass[2] / 5, color='blue')
planet = mpatches.Circle(starPos[3], starMass[3] / 5, color='black')

points = []
trace, = ax.plot([], [], '.-', lw=1, ms=2)

def planetCalculate():
    x1 = starPos[0][0] - starPos[3][0]
    y1 = starPos[0][1] - starPos[3][1]
    a1 = G * starMass[0] / (x1 ** 2 + y1 ** 2)
    angle1 = math.atan2(y1, x1)

    x2 = starPos[1][0] - starPos[3][0]
    y2 = starPos[1][1] - starPos[3][1]
    a2 = G * starMass[1] / (x2 ** 2 + y2 ** 2)
    angle2 = math.atan2(y2, x2)

    x3 = starPos[2][0] - starPos[3][0]
    y3 = starPos[2][1] - starPos[3][1]
    a3 = G * starMass[2] / (x3 ** 2 + y3 ** 2)
    angle3 = math.atan2(y3, x3)

    starPos[3][0] += starVel[3][0] * dt
    starPos[3][1] += starVel[3][1] * dt

    points.append(starPos[3])

    starVel[3][0] += (a1 * math.cos(angle1) + a2 * math.cos(angle2) + a3 * math.cos(angle3)) * dt
    starVel[3][1] += (a1 * math.sin(angle1) + a2 * math.sin(angle2) + a3 * math.sin(angle3)) * dt


def star0Calculate():
    x1 = starPos[1][0] - starPos[0][0]
    y1 = starPos[1][1] - starPos[0][1]
    a1 = G * starMass[1] / (x1 ** 2 + y1 ** 2)
    angle1 = math.atan2(y1, x1)

    x2 = starPos[2][0] - starPos[0][0]
    y2 = starPos[2][1] - starPos[0][1]
    a2 = G * starMass[2] / (x2 ** 2 + y2 ** 2)
    angle2 = math.atan2(y2, x2)

    starPos[0][0] += starVel[0][0] * dt
    starPos[0][1] += starVel[0][1] * dt

    starVel[0][0] += a1 * math.cos(angle1) * dt + a2 * math.cos(angle2) * dt
    starVel[0][1] += a1 * math.sin(angle1) * dt + a2 * math.sin(angle2) * dt


def star1Calculate():
    x1 = starPos[0][0] - starPos[1][0]
    y1 = starPos[0][1] - starPos[1][1]
    a1 = G * starMass[0] / (x1 ** 2 + y1 ** 2)
    angle1 = math.atan2(y1, x1)

    x2 = starPos[2][0] - starPos[1][0]
    y2 = starPos[2][1] - starPos[1][1]
    a2 = G * starMass[2] / (x2 ** 2 + y2 ** 2)
    angle2 = math.atan2(y2, x2)

    starPos[1][0] += starVel[1][0] * dt
    starPos[1][1] += starVel[1][1] * dt

    starVel[1][0] += a1 * math.cos(angle1) * dt + a2 * math.cos(angle2) * dt
    starVel[1][1] += a1 * math.sin(angle1) * dt + a2 * math.sin(angle2) * dt


def star2Calculate():
    x1 = starPos[0][0] - starPos[2][0]
    y1 = starPos[0][1] - starPos[2][1]
    a1 = G * starMass[0] / (x1 ** 2 + y1 ** 2)
    angle1 = math.atan2(y1, x1)

    x2 = starPos[1][0] - starPos[2][0]
    y2 = starPos[1][1] - starPos[2][1]
    a2 = G * starMass[1] / (x2 ** 2 + y2 ** 2)
    angle2 = math.atan2(y2, x2)

    starPos[2][0] += starVel[2][0] * dt
    starPos[2][1] += starVel[2][1] * dt

    starVel[2][0] += a1 * math.cos(angle1) * dt + a2 * math.cos(angle2) * dt
    starVel[2][1] += a1 * math.sin(angle1) * dt + a2 * math.sin(angle2) * dt


def calculatePosition():
    planetCalculate()
    star0Calculate()
    star1Calculate()
    star2Calculate()


def limit(i):
    l = min(starPos[0][i], starPos[1][i], starPos[2][i], starPos[3][i])
    r = max(starPos[0][i], starPos[1][i], starPos[2][i], starPos[3][i])
    return l - (r - l) * 0.2, r + (r - l) * 0.2


# 定义每帧更新图形的方法
def animate(i):
    calculatePosition()
    # 设置star0的位置
    star0.center = starPos[0]
    star1.center = starPos[1]
    star2.center = starPos[2]
    planet.center = starPos[3]
    # trace.set_data(points[0],[1])
    ax.add_patch(star0)
    ax.add_patch(star1)
    ax.add_patch(star2)
    ax.add_patch(planet)

    ax.set_xlim(limit(0))
    ax.set_ylim(limit(1))
    return star0, star1, star2, planet


ax.axis('equal')
# 设置动画参数
dt = 0.01  # 时间间隔
frames = int(5 / dt)  # 总帧数
# 创建动画
ani = FuncAnimation(fig, animate, frames=frames, interval=20)
plt.grid()
plt.show()
