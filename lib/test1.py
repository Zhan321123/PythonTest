"""
Texture Connection Mapping Based on Fusion and CTM Mod
"""
import numpy as np
from PIL import Image


def drawPixel(pixels: np.ndarray) -> Image.Image:
    image = Image.fromarray(pixels)
    return image


def getPixelData(image: Image.Image) -> np.ndarray[tuple]:
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    pixels = np.array(image)
    return pixels


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
    Take the middle pixel, tile it and take 2 * 2, take the middle 16 * 16
    :param texture:  16 * 16 pixels
    :param pad:  Number of border pixels
    :return:  16 * 16 middle pixel
    """
    tex1 = texture[pad:16 - pad, pad:16 - pad]
    tex4 = matrixTile(tex1, (2, 2))
    return tex4[8 - 2 * pad:24 - 2 * pad, 8 - 2 * pad:24 - 2 * pad]


def get4side(texture: np.ndarray, pad: int) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    """
    Obtain four pixels, tile 1 * 2 and take the middle padding * 16 pixels
    :param texture:  16 * 16 pixels
    :param pad:  Number of border pixels
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
    Replace block with the same image
    :param texture:  Big picture
    :param top:  Replace block coordinates * 16, [y, x]
    :param bottom:  Replaced block coordinates * 16, [y, x]
    :return:  Modified large image
    """
    top = texture[top[0] * 16:top[0] * 16 + 16, top[1] * 16:top[1] * 16 + 16]
    matrixCover(texture, top, (bottom[0] * 16, bottom[1] * 16))
    return texture


def generate(texture: np.ndarray, pad: int, mode: str = 'full') -> np.ndarray:
    """
    Generate texture connected images
    :param texture:  Maps
    :param pad:  frame
    :Param mode: the mode corresponding to fusion
    :return:  Generate a good pixel image
    """

    center = getCenter(texture, pad)
    centerHor, centerVer = center[pad:16 - pad, :], center[:, pad:16 - pad]
    rig, top, lef, bot = get4side(texture, pad)
    # first block
    first = matrixCover(texture, center[pad:16 - pad, pad:16 - pad], (pad, pad))  # 1A
    # Array out all blocks
    result = matrixTile(first, (8, 6))
    # Clear the blank space on the bottom left and right sides
    transparent = np.zeros((16, 16, 4), dtype=np.uint8)
    matrixCover(result, transparent, (80, 16))
    # other blocks
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
    matrixCover(result, center[:, :16 - pad], (80, 48))  # 4F
    matrixCover(result, centerHor, (80 + pad, 48))
    replaceBlock(result, (4, 2), (5, 4))  # 5F
    matrixCover(result, first[16 - pad:, 16 - pad:], (96 - pad, 80 - pad))
    replaceBlock(result, (5, 2), (5, 5))  # 6F
    matrixCover(result, first[:pad, 16 - pad:], (80, 96 - pad))
    replaceBlock(result, (2, 2), (5, 6))  # 7F
    matrixCover(result, first[:pad, 16 - pad:], (80, 112 - pad))
    replaceBlock(result, (2, 2), (5, 7))  # 8F
    matrixCover(result, first[:pad, :pad], (80, 112))

    return result


def start(file: str, pad: int) -> Image.Image:
    image = Image.open(file)
    pixels = getPixelData(image)
    result = generate(pixels, pad)
    last = drawPixel(result)
    last.convert('P')
    return last


if __name__ == '__main__':
    file = "./fusion/fusion-createBlock/industrial_iron_block.png"
    border = 3  # border width, please try 1, 2, 3 or 4.
    last = start(file, border)
    last.save("./fusion/fusion-createBlock/industrial_iron_block_full.png")
