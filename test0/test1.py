import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math
matplotlib.use('TkAgg')

class Body:
    def __init__(self, weight, pos0, v0):
        self.m = weight
        self.pos = pos0
        self.v = v0

    def update(self, others, delta_t):
        # 更新当前天体的位置
        # others存储前一时刻所有body的pos和m，list类型
        ft = np.array([0, 0, 0])
        for bodyi in others:
            # 各个引力的单位向量
            ft_dir = (bodyi.pos - self.pos) / np.linalg.norm(bodyi.pos - self.pos)
            # 设置引力常数为1
            ft = ft + (bodyi.m * self.m / sum(np.square(bodyi.pos - self.pos))) * ft_dir
        at = ft / self.m
        # 位置更新，delta_r = v*delta_t + 0.5*a*(delta_t**2)
        self.pos = self.pos + self.v * delta_t + 0.5 * at * (delta_t ** 2)
        # 速度更新，delta_v = a*delta_t
        self.v = self.v + at * delta_t

    def show(self, ax):
        # 展示当前天体，根据质量大小设置marker尺寸
        ax.scatter(self.pos[0], self.pos[1], self.pos[2], s=(self.m**0.5)**0.5*8,
                   label='Position:(%.2f, %.2f, %.2f)' % (self.pos[0], self.pos[1], self.pos[2]))
        plt.legend()


if __name__ == '__main__':

    # 设置初始参数，下面这个初始参数比较好
    body1 = Body(1000*math.sqrt(3),
                 np.array([10, 0, 0]),
                 np.array([10*math.cos(0.5*math.pi), 10*math.sin(0.5*math.pi), 15]))
    body2 = Body(1000*math.sqrt(3),
                 np.array([10*math.cos(2/3*math.pi), 10*math.sin(2/3*math.pi), 0]),
                 np.array([10*math.cos(0.5*math.pi+2/3*math.pi), 10*math.sin(0.5*math.pi+2/3*math.pi), -10]))
    body3 = Body(3000*math.sqrt(3),
                 np.array([10*math.cos(4/3*math.pi), 10*math.sin(4/3*math.pi), 0]),
                 np.array([10*math.cos(0.5*math.pi+4/3*math.pi), 10*math.sin(0.5*math.pi+4/3*math.pi), 5]))

    delta_t = 0.2  # 模拟时间步长
    all_t = 100  # 模拟总时间

    ax = plt.subplot(projection='3d')
    plt.ion()

    t = 0
    scale_show = 80  # 设置显示范围
    while t <= all_t:
        plt.cla()
        ax.set_title('3 Body, t = %.2fs' % t)
        ax.set_xlim(-scale_show, scale_show)
        ax.set_ylim(-scale_show, scale_show)
        ax.set_zlim(-scale_show, scale_show)
        ax.set_xlabel('X')  # 设置x坐标轴
        ax.set_ylabel('Y')  # 设置y坐标轴
        ax.set_zlabel('Z')  # 设置z坐标轴

        body_copy = [body1, body2, body3]
        body1.update([body_copy[1], body_copy[2]], delta_t)
        body1.show(ax)
        body2.update([body_copy[0], body_copy[2]], delta_t)
        body2.show(ax)
        body3.update([body_copy[0], body_copy[1]], delta_t)
        body3.show(ax)

        ax.plot([body1.pos[0], body2.pos[0]], [body1.pos[1], body2.pos[1]], [body1.pos[2], body2.pos[2]], 'r-')
        ax.plot([body2.pos[0], body3.pos[0]], [body2.pos[1], body3.pos[1]], [body2.pos[2], body3.pos[2]], 'r-')
        ax.plot([body3.pos[0], body1.pos[0]], [body3.pos[1], body1.pos[1]], [body3.pos[2], body1.pos[2]], 'r-')
        plt.pause(0.000001)
        plt.show()

        t = t + delta_t

