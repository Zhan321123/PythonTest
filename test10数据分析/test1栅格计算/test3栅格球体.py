from test1drawBlocks import *


def calcSphere(radius: int) -> spacePoints:
    """
    栅格化球体表面
    引用自：https://stackoverflow.com/questions/41656006/how-to-rasterize-a-sphere/41666156#41666156

    :param radius: 整数球体半径radius
    :return: 坐标列表
    """
    radius += 0.5

    def mirror(x: float, y: float, z: float, bs: set):
        """镜像卦限"""
        positions = [
            (x, y, z), (-x, y, z), (x, -y, z), (-x, -y, z),
            (x, y, -z), (-x, y, -z), (x, -y, -z), (-x, -y, -z)
        ]
        bs.update(positions)

    blocks = set()
    maxR2 = int(np.floor(radius * radius))
    zMax = int(np.floor(radius))
    x = 0
    while True:
        # 当 x^2 + zMax^2 大于 maxR2 且 zMax 大于等于 x 时，减小 zMax
        while x * x + zMax * zMax > maxR2 and zMax >= x:
            zMax -= 1
        # 如果 zMax 小于 x，说明当前 x 下 z 无法成为最大值，跳出循环
        if zMax < x:
            break
        z = zMax
        y = 0
        while True:
            # 当 x^2 + y^2 + z^2 大于 maxR2 且 z 大于等于 x 和 y 时，减小 z
            while x * x + y * y + z * z > maxR2 and z >= x and z >= y:
                z -= 1
            # 如果 z 小于 x 或 z 小于 y，说明当前 x 和 y 下 z 无法成为最大值，跳出循环
            if z < x or z < y:
                break
            # 旋转和镜像其他卦限坐标
            mirror(x, y, z, blocks)
            mirror(y, z, x, blocks)
            mirror(z, x, y, blocks)
            y += 1
        x += 1

    return blocks

if __name__ == '__main__':
    fig, axs = plt.subplots(1, 1)


    points = calcSphere(16)
    drawBlock(axs, points)

    plt.show()