"""
基于fusion模组的贴图绘制
"""
from test1ImageInfo import *


def matrixCover(bottomMatrix: np.ndarray, topMatrix: np.ndarray, startPosition: tuple[int, int]) -> np.ndarray:
    row, col = startPosition
    coverLength = min(bottomMatrix.shape[0] - row, topMatrix.shape[0])
    coverWidth = min(bottomMatrix.shape[1] - col, topMatrix.shape[1])
    bottomMatrix[row:row + coverLength, col:col + coverWidth] = topMatrix[0:coverLength, 0:coverWidth]
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


def replaceBlock(texture: np.ndarray, top: tuple[int, int], bottom: tuple[int, int]) -> np.ndarray:
    """
    同图替换块
    :param texture: 大图
    :param top: 替换方块坐标*16, [y, x]
    :param bottom: 被替换方块坐标*16, [y, x]
    :return: 修改后的大图
    """
    top = texture[top[0] * 16:top[0] * 16 + 16, top[1] * 16:top[1] * 16 + 16]
    matrixCover(texture, top, (bottom[0] * 16, bottom[1] * 16))
    return texture


def generate(texture: np.ndarray, pad: int, mode: str = 'full') -> np.ndarray:
    """
    生成图像
    :param texture: 贴图
    :param pad: 边框
    :param mode: fusion对应的模式
    :return: 生成好的像素图
    """

    center = getCenter(texture, pad)
    centerHor, centerVer = center[pad:16 - pad, :], center[:, pad:16 - pad]
    rig, top, lef, bot = get4side(texture, pad)
    # 第一个block
    first = matrixCover(texture, center[pad:16 - pad, pad:16 - pad], (pad, pad))  # 1A
    # 阵列出全部块
    result = matrixTile(first, (8, 6))
    # 清除左下角右边为空白
    transparent = np.zeros((16, 16, 4), dtype=np.uint8)
    matrixCover(result, transparent, (80, 16))
    # 替换其他方块
    matrixCover(result, center[pad:16 - pad, pad:], (pad, 16 + pad))  # 2A
    matrixCover(result, top[:, pad:], (0, 16 + pad))
    matrixCover(result, bot[:, pad:], (16 - pad, 16 + pad))
    matrixCover(result, centerHor, (pad, 32))  # 3A
    matrixCover(result, top, (0, 32))
    matrixCover(result, bot, (16 - pad, 32))
    matrixCover(result, center[pad:16 - pad, :16 - pad], (pad, 48))  # 4A
    matrixCover(result, top[:, :16 - pad], (0, 48))
    matrixCover(result, bot[:, :16 - pad], (16 - pad, 48))
    matrixCover(result, center[pad:16 - pad, pad:], (pad, 64 + pad))  # 5A
    matrixCover(result, center[pad:, pad:16 - pad], (pad, 64 + pad))
    matrixCover(result, top[:, pad:], (0, 64 + pad))
    matrixCover(result, lef[pad:, :], (pad, 64))
    matrixCover(result, center[pad:16 - pad, :16 - pad], (pad, 80))  # 6A
    matrixCover(result, center[pad:, pad:16 - pad], (pad, 80 + pad))
    matrixCover(result, top[:, :16 - pad], (0, 80))
    matrixCover(result, rig[pad:, :], (pad, 96 - pad))
    matrixCover(result, center[pad:16 - pad, pad:], (pad, 96 + pad))  # 7A
    matrixCover(result, centerVer, (0, 96 + pad))
    matrixCover(result, lef, (0, 96))
    matrixCover(result, center[pad:, pad:16 - pad], (pad, 112 + pad))  # 8A
    matrixCover(result, centerHor, (pad, 112))
    matrixCover(result, top, (0, 112))
    matrixCover(result, center[pad:, pad:16 - pad], (16 + pad, pad))  # 1B
    matrixCover(result, lef[pad:, :], (16 + pad, 0))
    matrixCover(result, rig[pad:, :], (16 + pad, 16 - pad))
    matrixCover(result, center[pad:, pad:], (16 + pad, 16 + pad))  # 2B
    matrixCover(result, top[:, pad:], (16, 16 + pad))
    matrixCover(result, lef[pad:, :], (16 + pad, 16))
    matrixCover(result, center[pad:, :], (16 + pad, 32))  # 3B
    matrixCover(result, top, (16, 32))
    matrixCover(result, center[pad:, :16 - pad], (16 + pad, 48))  # 4B
    matrixCover(result, top[:, :16 - pad], (16, 48))
    matrixCover(result, rig[pad:, :], (16 + pad, 64 - pad))
    matrixCover(result, center[:16 - pad, pad:16 - pad], (16, 64 + pad))  # 5B
    matrixCover(result, center[pad:16 - pad, pad:], (16 + pad, 64 + pad))
    matrixCover(result, lef[:16 - pad, :], (16, 64))
    matrixCover(result, bot[:, pad:], (32 - pad, 64 + pad))
    matrixCover(result, center[pad:16 - pad, :16 - pad], (16 + pad, 80))  # 6B
    matrixCover(result, center[:16 - pad, pad:16 - pad], (16, 80 + pad))
    matrixCover(result, bot[:, :16 - pad], (32 - pad, 80))
    matrixCover(result, rig[:16 - pad, :], (16, 96 - pad))
    matrixCover(result, centerHor, (16 + pad, 96))  # 7B
    matrixCover(result, center[:16 - pad, pad:16 - pad], (16, 96 + pad))
    matrixCover(result, bot, (32 - pad, 96))
    matrixCover(result, centerVer, (16, 112 + pad))  # 8B
    matrixCover(result, center[pad:16 - pad, :16 - pad], (16 + pad, 112))
    matrixCover(result, rig, (16, 128 - pad))
    matrixCover(result, centerVer, (32, pad))  # 1C
    matrixCover(result, lef, (32, 0))
    matrixCover(result, rig, (32, 16 - pad))
    matrixCover(result, center[:, pad:], (32, 16 + pad))  # 2C
    matrixCover(result, lef, (32, 16))
    matrixCover(result, center, (32, 32))  # 3C
    matrixCover(result, center[:, :16 - pad], (32, 48))  # 4C
    matrixCover(result, rig, (32, 64 - pad))
    replaceBlock(result, (2, 1), (2, 4))  # 5C
    matrixCover(result, first[16 - pad:, 16 - pad:], (48 - pad, 80 - pad))
    replaceBlock(result, (1, 2), (2, 5))  # 6C
    matrixCover(result, first[16 - pad:, :pad], (48 - pad, 80))
    replaceBlock(result, (2, 1), (2, 6))  # 7C
    matrixCover(result, first[:pad, 16 - pad:], (32, 112 - pad))
    replaceBlock(result, (1, 2), (2, 7))  # 8C
    matrixCover(result, first[16 - pad:, 16 - pad:], (48 - pad, 128 - pad))
    matrixCover(result, center[:16 - pad, pad:16 - pad], (48, pad))  # 1D
    matrixCover(result, lef[:16 - pad, :], (48, 0))
    matrixCover(result, rig[:16 - pad, :], (48, 16 - pad))
    matrixCover(result, center[:16 - pad, pad:], (48, 16 + pad))  # 2D
    matrixCover(result, lef[:16 - pad, :], (48, 16))
    matrixCover(result, bot[:, pad:], (64 - pad, 16 + pad))
    matrixCover(result, center[:16 - pad, :], (48, 32))  # 3D
    matrixCover(result, bot, (64 - pad, 32))
    matrixCover(result, center[:16 - pad, :16 - pad], (48, 48))  # 4D
    matrixCover(result, bot[:, :16 - pad], (64 - pad, 48))
    matrixCover(result, rig[:16 - pad, :], (48, 64 - pad))
    replaceBlock(result, (3, 2), (3, 4))  # 5D
    matrixCover(result, first[:pad, 16 - pad:], (48, 80 - pad))
    replaceBlock(result, (2, 3), (3, 5))  # 6D
    matrixCover(result, first[:pad, :pad], (48, 80))
    replaceBlock(result, (3, 2), (3, 6))  # 7D
    matrixCover(result, first[:pad, :pad], (48, 96))
    replaceBlock(result, (2, 3), (3, 7))  # 8D
    matrixCover(result, first[16 - pad:, :pad], (64 - pad, 112))
    matrixCover(result, center[:16 - pad, pad:], (64, pad))  # 1E
    matrixCover(result, center[pad:, :16 - pad], (64 + pad, 0))
    matrixCover(result, centerVer, (64, 16 + pad))  # 2E
    matrixCover(result, centerHor, (64 + pad, 16))
    matrixCover(result, center[:, pad:], (64, 32 + pad))  # 3E
    matrixCover(result, centerHor, (64 + pad, 32))
    matrixCover(result, center[pad:, :], (64 + pad, 48))  # 4E
    matrixCover(result, centerVer, (64, 48 + pad))
    replaceBlock(result, (4, 3), (4, 4))  # 5E
    matrixCover(result, first[16 - pad:, :pad], (80 - pad, 64))
    replaceBlock(result, (4, 3), (4, 5))  # 6E
    matrixCover(result, first[16 - pad:, 16 - pad:], (80 - pad, 96 - pad))
    replaceBlock(result, (2, 2), (4, 6))  # 7E
    matrixCover(result, first[16 - pad:, 16 - pad:], (80 - pad, 112 - pad))
    replaceBlock(result, (2, 2), (4, 7))  # 8E
    matrixCover(result, first[16 - pad:, :pad], (80 - pad, 112))
    matrixCover(result, center[:16 - pad, :16 - pad], (80, 0))  # 1F
    matrixCover(result, center[pad:, pad:], (80 + pad, pad))
    matrixCover(result, center[:16 - pad, :], (80, 32))  # 3F
    matrixCover(result, centerVer, (80, 32 + pad))
    matrixCover(result, center[:, :16-pad], (80, 48))  # 4F
    matrixCover(result, centerHor, (80 + pad, 48))
    replaceBlock(result, (4,2), (5,4))  # 5F
    matrixCover(result, first[16 - pad:, 16 - pad:], (96 - pad, 80 - pad))
    replaceBlock(result, (5,2), (5,5))  # 6F
    matrixCover(result, first[:pad, 16 - pad:], (80, 96 - pad))
    replaceBlock(result, (2, 2), (5, 6))  # 7F
    matrixCover(result, first[:pad, 16 - pad:], (80, 112 - pad))
    replaceBlock(result, (2, 2), (5, 7))  # 8F
    matrixCover(result, first[:pad, :pad], (80, 112))

    return result


if __name__ == '__main__':
    file = r"C:\Users\刘高瞻\Desktop\fusion\fusion-createBlock\industrial_iron_block.png"
    image = Image.open(file)
    getInfo(image)
    pixels = getPixelData(image)
    result = generate(pixels, 3)
    last = drawPixel(result)
    last.convert('P')
    # last.save(r"C:\Users\刘高瞻\Desktop\industrial_iron_block.png")


    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(plt.MultipleLocator(16))
    ax.yaxis.set_major_locator(plt.MultipleLocator(16))
    show(last, ax)
    plt.show()


