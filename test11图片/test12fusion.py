"""
基于fusion模组的贴图绘制
"""
from test1ImageInfo import *


def matrixCover(bottomMatrix: np.ndarray, topMatrix: np.ndarray, startPosition: tuple[int, int],
                copy: bool = False) -> np.ndarray:
    """
    产生一个新的数组，不改变原数组
    :param copy:
    :param bottomMatrix:
    :param topMatrix:
    :param startPosition:
    :return:
    """
    xPos, yPos = startPosition
    length, width = topMatrix.shape[:2]
    if copy:
        bottomMatrix = bottomMatrix.copy()
    bottomMatrix[xPos:xPos + length, yPos:yPos + width] = topMatrix
    return bottomMatrix


def matrixTile(matrix: np.ndarray, repeat: tuple[int, int]) -> np.ndarray:
    row, col = repeat
    return np.tile(matrix, (col, row, 1))


def getCenter(texture: np.ndarray, pad: int) -> np.ndarray:
    """
    取得中间像素，平铺并2*2取中间16*16
    :param texture: 16*16像素
    :param pad: 边框像素数
    :return: 16*16中间像素
    """
    tex1 = texture[pad:16 - pad, pad:16 - pad]
    tex4 = matrixTile(tex1, (2, 2))
    return tex4[8 - 2 * pad:24 - 2 * pad, 8 - 2 * pad:24 - 2 * pad]


def get4Corner(texture: np.ndarray, pad: int) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    """
    获取四角
    :param texture: 贴图16*16
    :param pad: 边框格数
    :return: 四角(left-top, left-bottom, right-bottom, right-top)
    """


def get4side(texture: np.ndarray, pad: int) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    """
    取得四边像素，平铺1*2取中间padding*16像素
    :param texture: 16*16像素
    :param pad: 边框像素数
    :return: (right padding*16, top 16*padding, left padding*16, bottom 16*padding)
    """
    tr = texture[pad:16 - pad, 16 - pad:16]
    tp = texture[0:pad, pad:16 - pad]
    tl = texture[pad:16 - pad, 0:pad]
    tb = texture[16 - pad:16, pad:16 - pad, ]
    tr2, tl2 = matrixTile(tr, (1, 2)), matrixTile(tl, (1, 2))
    tp2, tb2 = matrixTile(tp, (2, 1)), matrixTile(tb, (2, 1))
    return (tr2[8 - 2 * pad:24 - 2 * pad, 0:pad],
            tp2[0:pad, 8 - 2 * pad:24 - 2 * pad],
            tl2[8 - 2 * pad:24 - 2 * pad, 0:pad],
            tb2[0:pad, 8 - 2 * pad:24 - 2 * pad])


def suture(blocks: [[np.ndarray]]) -> np.ndarray:
    """
    缝合blocks
    :param blocks:
    :return:
    """
    rows = [np.concatenate(row, axis=1) for row in blocks]
    result = np.concatenate(rows, axis=0)
    return result


def generate(texture: np.ndarray, pad: int, mode: str = 'full') -> np.ndarray:
    """
    生成图像
    :param texture: 贴图
    :param pad: 边框
    :param mode: fusion对应的模式
    :return: 生成好的像素图
    """

    transparent = np.zeros((16, 16, 4), dtype=np.uint8)
    center = getCenter(texture, pad)
    centerHor, centerVer = center[pad:16 - pad, :], center[:, pad:16 - pad]
    rig, top, lef, bot = get4side(texture, pad)
    # 第一个block
    b1 = matrixCover(texture, center[pad:16 - pad, pad:16 - pad], (pad, pad))

    b2 = matrixCover(b1, center[pad:16 - pad, pad:], (pad, pad), True)  # 2A
    matrixCover(b2, top[:, pad:], (0, pad))
    matrixCover(b2, bot[:, pad:], (16 - pad, pad))

    b3 = matrixCover(b1, centerHor, (pad, 0), True)
    matrixCover(b3, top, (0, 0))
    matrixCover(b3, bot, (16 - pad, 0))

    b4 = matrixCover(b1, center[pad:16 - pad, :16 - pad], (pad, 0), True)  # 4A
    matrixCover(b4, top[:, :16 - pad], (0, 0))
    matrixCover(b4, bot[:, :16 - pad], (16 - pad, 0))

    b5 = matrixCover(b1, center[pad:16 - pad, pad:], (pad, pad), True)  # 5A
    matrixCover(b5, center[pad:, pad:16 - pad], (pad, pad))
    matrixCover(b5, top[:, pad:], (0, pad))
    matrixCover(b5, lef[pad:, :], (pad, 0))

    b6 = matrixCover(b1, center[pad:16 - pad, :16 - pad], (pad, 0), True)  # 6A
    matrixCover(b6, center[pad:, pad:16 - pad], (pad, 0 + pad))
    matrixCover(b6, top[:, :16 - pad], (0, 0))
    matrixCover(b6, rig[pad:, :], (pad, 16 - pad))

    b7 = matrixCover(b1, center[pad:16 - pad, pad:], (pad, pad), True)  # 7A
    matrixCover(b7, centerVer, (0, pad))
    matrixCover(b7, lef, (0, 0))

    b8 = matrixCover(b1, center[pad:, pad:16 - pad], (pad, pad), True)  # 8A
    matrixCover(b8, centerHor, (pad, 0))
    matrixCover(b8, top, (0, 0))

    b9 = matrixCover(b1, center[pad:, pad:16 - pad], (pad, pad), True)  # 1B
    matrixCover(b9, lef[pad:, :], (pad, 0))
    matrixCover(b9, rig[pad:, :], (pad, 16 - pad))

    b10 = matrixCover(b1, center[pad:, pad:], (pad, pad), True)  # 2B
    matrixCover(b10, top[:, pad:], (0, pad))
    matrixCover(b10, lef[pad:, :], (pad, 0))

    b11 = matrixCover(b1, center[pad:, :], (pad, 0), True)  # 3B
    matrixCover(b11, top, (0, 0))

    b12 = matrixCover(b1, center[pad:, :16 - pad], (pad, 0), True)  # 4B
    matrixCover(b12, top[:, :16 - pad], (0, 0))
    matrixCover(b12, rig[pad:, :], (pad, 16 - pad))

    b13 = matrixCover(b1, center[:16 - pad, pad:16 - pad], (0, pad), True)  # 5B
    matrixCover(b13, center[pad:16 - pad, pad:], (pad, pad))
    matrixCover(b13, lef[:16 - pad, :], (0, 0))
    matrixCover(b13, bot[:, pad:], (16 - pad, pad))

    b14 = matrixCover(b1, center[pad:16 - pad, :16 - pad], (pad, 0), True)  # 6B
    matrixCover(b14, center[:16 - pad, pad:16 - pad], (0, pad))
    matrixCover(b14, bot[:, :16 - pad], (16 - pad, 0))
    matrixCover(b14, rig[:16 - pad, :], (0, 16 - pad))

    b15 = matrixCover(b1, centerHor, (pad, 0), True)  # 7B
    matrixCover(b15, center[:16 - pad, pad:16 - pad], (0, pad))
    matrixCover(b15, bot, (16 - pad, 0))

    b16 = matrixCover(b1, centerVer, (0, pad), True)  # 8B
    matrixCover(b16, center[pad:16 - pad, :16 - pad], (pad, 0))
    matrixCover(b16, rig, (0, 16 - pad))

    b17 = matrixCover(b1, centerVer, (0, pad), True)  # 1C
    matrixCover(b17, lef, (0, 0))
    matrixCover(b17, rig, (0, 16 - pad))

    b18 = matrixCover(b1, center[:, pad:], (0, pad), True)  # 2C
    matrixCover(b18, lef, (0, 0))

    b19 = center

    b20 = matrixCover(b1, center[:, :16 - pad], (0, 0), True)  # 4C
    matrixCover(b20, rig, (0, 16 - pad))

    b21 = matrixCover(b18, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)

    b22 = matrixCover(b11, b1[16 - pad:, :pad], (16 - pad, 0), True)

    b23 = matrixCover(b18, b1[:pad, 16 - pad:], (0, 16 - pad), True)

    b24 = matrixCover(b11, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)

    b25 = matrixCover(b1, center[:16 - pad, pad:16 - pad], (0, pad), True)  # 1D
    matrixCover(b25, lef[:16 - pad, :], (0, 0))
    matrixCover(b25, rig[:16 - pad, :], (0, 16 - pad))

    b26 = matrixCover(b1, center[:16 - pad, pad:], (0, pad), True)  # 2D
    matrixCover(b26, lef[:16 - pad, :], (0, 0))
    matrixCover(b26, bot[:, pad:], (16 - pad, pad))

    b27 = matrixCover(b1, center[:16 - pad, :], (0, 0), True)  # 3D
    matrixCover(b27, bot, (16 - pad, 0))

    b28 = matrixCover(b1, center[:16 - pad, :16 - pad], (0, 0), True)  # 4D
    matrixCover(b28, bot[:, :16 - pad], (16 - pad, 0))
    matrixCover(b28, rig[:16 - pad, :], (0, 16 - pad))

    b29 = matrixCover(b27, b1[:pad, 16 - pad:], (0, 16 - pad), True)

    b30 = matrixCover(b20, b1[:pad, :pad], (0, 0), True)

    b31 = matrixCover(b27, b1[:pad, :pad], (0, 0), True)

    b32 = matrixCover(b28, b1[16 - pad:, :pad], (16 - pad, 0), True)

    b33 = matrixCover(b1, center[:16 - pad, pad:], (0, pad), True)  # 1E
    matrixCover(b33, center[pad:, :16 - pad], (pad, 0))

    b34 = matrixCover(b1, centerVer, (0, pad), True)  # 2E
    matrixCover(b34, centerHor, (pad, 0))

    b35 = matrixCover(b1, center[:, pad:], (0, pad), True)  # 3E
    matrixCover(b35, centerHor, (pad, 0))

    b36 = matrixCover(b1, center[pad:, :], (pad, 0), True)  # 4E
    matrixCover(b36, centerVer, (0, 0 + pad))

    b37 = matrixCover(b36, b1[16 - pad:, :pad], (16 - pad, 0), True)

    b38 = matrixCover(b36, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)

    b39 = matrixCover(b19, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)

    b40 = matrixCover(b19, b1[16 - pad:, :pad], (16 - pad, 0), True)

    b41 = matrixCover(b1, center[:16 - pad, :16 - pad], (0, 0), True)  # 1F
    matrixCover(b41, center[pad:, pad:], (pad, pad))

    b42 = transparent

    b43 = matrixCover(b1, center[:16 - pad, :], (0, 0), True)  # 3F
    matrixCover(b43, centerVer, (0, pad))

    b44 = matrixCover(b1, center[:, :16 - pad], (0, 0), True)  # 4F
    matrixCover(b44, centerHor, (0 + pad, 0))

    b45 = matrixCover(b35, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)

    b46 = matrixCover(b43, b1[:pad, 16 - pad:], (0, 16 - pad), True)

    b47 = matrixCover(b19, b1[:pad, 16 - pad:], (0, 16 - pad), True)

    b48 = matrixCover(b19, b1[:pad, :pad], (0, 0), True)

    arranged = [
        [b1, b2, b3, b4, b5, b6, b7, b8],
        [b9, b10, b11, b12, b13, b14, b15, b16],
        [b17, b18, b19, b20, b21, b22, b23, b24],
        [b25, b26, b27, b28, b29, b30, b31, b32],
        [b33, b34, b35, b36, b37, b38, b39, b40],
        [b41, b42, b43, b44, b45, b46, b47, b48],
        [transparent] * 8,
        [transparent] * 8,
    ]
    return suture(arranged)


if __name__ == '__main__':
    file = r"C:\Users\刘高瞻\Desktop\Sprite-0001.png"
    image = Image.open(file)
    getInfo(image)
    pixels = getPixelData(image)
    out = generate(pixels, 3)
    last = drawPixel(out)
    # last.convert('P')
    # last.save(r"C:\Users\刘高瞻\Desktop\Sprite-0002.png")

    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(plt.MultipleLocator(16))
    ax.yaxis.set_major_locator(plt.MultipleLocator(16))
    show(last, ax)
    plt.show()
