"""
基于fusion模组的贴图绘制
"""
import numpy as np
from PIL import Image


def getPixelData(image: Image.Image) -> np.ndarray[tuple]:
  """获取图片像素数据"""
  if image.mode != 'RGBA':
    image = image.convert('RGBA')
  pixels = np.array(image)
  return pixels


def drawPixel(pixels: np.ndarray) -> Image.Image:
  """根据像素数据画图像"""
  image = Image.fromarray(pixels)
  return image


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
  if pad == 1:
    lt = [[(0, 0)]]
  elif pad == 2:
    lt = [[(0, 0), (1, 2)],
          [(2, 1), (1, 1)]]
  elif pad == 3:
    lt = [[(0, 0), (1, 2), (2, 4)],
          [(2, 1), (1, 1), (2, 3)],
          [(4, 2), (3, 2), (2, 2)]]
  else:
    lt = [[(0, 0), (1, 2), (2, 4), (3, 6)],
          [(2, 1), (1, 1), (2, 3), (3, 5)],
          [(4, 2), (3, 2), (2, 2), (3, 4)],
          [(6, 3), (5, 3), (4, 3), (3, 3)]]
  lt = np.array(lt)
  lb = np.array([[(point[0], 15 - point[1]) for point in sub] for sub in lt])
  lb = np.transpose(np.rot90(lb, -1), (1, 0, 2))
  rb = np.array([[(15 - point[0], 15 - point[1]) for point in sub] for sub in lt])
  rb = np.rot90(rb, 2)
  rt = np.array([[(15 - point[0], point[1]) for point in sub] for sub in lt])
  rt = np.transpose(np.rot90(rt, 1), (1, 0, 2))

  lt = texture[lt[..., 1], lt[..., 0]]
  lb = texture[lb[..., 1], lb[..., 0]]
  rb = texture[rb[..., 1], rb[..., 0]]
  rt = texture[rt[..., 1], rt[..., 0]]

  return lt, lb, rb, rt


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


def replaceCorner(texture: np.ndarray, corner: np.ndarray, direction: str):
  pad = len(corner)
  if direction == 'lt':
    texture[0:pad, 0:pad] = corner
  elif direction == 'lb':
    texture[16 - pad:16, 0:pad] = corner
  elif direction == 'rb':
    texture[16 - pad:16, 16 - pad:16] = corner
  elif direction == 'rt':
    texture[0:pad, 16 - pad:16] = corner
  else:
    raise ValueError('direction must be lt, lb, rb,rt')


def suture(blocks: [[np.ndarray]]) -> np.ndarray:
  """
  缝合blocks
  :param blocks:
  :return:
  """
  rows = [np.concatenate(row, axis=1) for row in blocks]
  result = np.concatenate(rows, axis=0)
  return result


def generateFusion(texture: np.ndarray, pad: int, mode: str = 'full') -> np.ndarray:
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
  lt, lb, rb, rt = get4Corner(texture, pad)

  # 第一个完整block
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

  b7 = matrixCover(b1, center[pad:16 - pad, pad:], (pad, pad), True)  # 7A
  matrixCover(b7, centerVer, (0, pad))
  matrixCover(b7, lef, (0, 0))
  replaceCorner(b7, rt, 'rt')
  replaceCorner(b7, rb, 'rb')

  b8 = matrixCover(b1, center[pad:, pad:16 - pad], (pad, pad), True)  # 8A
  matrixCover(b8, centerHor, (pad, 0))
  matrixCover(b8, top, (0, 0))
  replaceCorner(b8, lb, 'lb')
  replaceCorner(b8, rb, 'rb')

  b9 = matrixCover(b1, center[pad:, pad:16 - pad], (pad, pad), True)  # 1B
  matrixCover(b9, lef[pad:, :], (pad, 0))
  matrixCover(b9, rig[pad:, :], (pad, 16 - pad))

  b10 = matrixCover(b1, center[pad:, pad:], (pad, pad), True)  # 2B
  matrixCover(b10, top[:, pad:], (0, pad))
  matrixCover(b10, lef[pad:, :], (pad, 0))

  b5 = b10.copy()
  replaceCorner(b5, rb, 'rb')

  b11 = matrixCover(b1, center[pad:, :], (pad, 0), True)  # 3B
  matrixCover(b11, top, (0, 0))

  b12 = matrixCover(b1, center[pad:, :16 - pad], (pad, 0), True)  # 4B
  matrixCover(b12, top[:, :16 - pad], (0, 0))
  matrixCover(b12, rig[pad:, :], (pad, 16 - pad))

  b6 = b12.copy()
  replaceCorner(b6, lb, 'lb')

  b15 = matrixCover(b1, center[:16 - pad, :], (0, 0), True)
  matrixCover(b15, bot, (16 - pad, 0))
  replaceCorner(b15, lt, 'lt')
  replaceCorner(b15, rt, 'rt')

  b16 = matrixCover(b1, center[:, :16 - pad], (0, 0), True)
  matrixCover(b16, rig, (0, 16 - pad))
  replaceCorner(b16, lt, 'lt')
  replaceCorner(b16, lb, 'lb')

  b17 = matrixCover(b1, centerVer, (0, pad), True)  # 1C
  matrixCover(b17, lef, (0, 0))
  matrixCover(b17, rig, (0, 16 - pad))

  b18 = matrixCover(b1, center[:, pad:], (0, pad), True)  # 2C
  matrixCover(b18, lef, (0, 0))

  b19 = center

  b20 = matrixCover(b1, center[:, :16 - pad], (0, 0), True)  # 4C
  matrixCover(b20, rig, (0, 16 - pad))

  b21 = matrixCover(b18, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)
  replaceCorner(b21, rb, 'rb')

  b22 = matrixCover(b11, b1[16 - pad:, :pad], (16 - pad, 0), True)
  replaceCorner(b22, lb, 'lb')

  b23 = matrixCover(b18, b1[:pad, 16 - pad:], (0, 16 - pad), True)
  replaceCorner(b23, rt, 'rt')

  b24 = matrixCover(b11, b1[16 - pad:, 16 - pad:], (16 - pad, 16 - pad), True)
  replaceCorner(b24, rb, 'rb')

  b25 = matrixCover(b1, center[:16 - pad, pad:16 - pad], (0, pad), True)  # 1D
  matrixCover(b25, lef[:16 - pad, :], (0, 0))
  matrixCover(b25, rig[:16 - pad, :], (0, 16 - pad))

  b26 = matrixCover(b1, center[:16 - pad, pad:], (0, pad), True)  # 2D
  matrixCover(b26, lef[:16 - pad, :], (0, 0))
  matrixCover(b26, bot[:, pad:], (16 - pad, pad))

  b13 = b26.copy()
  replaceCorner(b13, rt, 'rt')

  b27 = matrixCover(b1, center[:16 - pad, :], (0, 0), True)  # 3D
  matrixCover(b27, bot, (16 - pad, 0))

  b28 = matrixCover(b1, center[:16 - pad, :16 - pad], (0, 0), True)  # 4D
  matrixCover(b28, bot[:, :16 - pad], (16 - pad, 0))
  matrixCover(b28, rig[:16 - pad, :], (0, 16 - pad))

  b14 = b28.copy()
  replaceCorner(b14, lt, 'lt')

  b29 = b27.copy()
  replaceCorner(b29, rt, 'rt')

  b30 = b20.copy()
  replaceCorner(b30, lt, 'lt')

  b31 = b27.copy()
  replaceCorner(b31, lt, 'lt')

  b32 = b20.copy()
  replaceCorner(b32, lb, 'lb')

  b33 = b19.copy()
  replaceCorner(b33, lt, 'lt')
  replaceCorner(b33, rb, 'rb')

  b34 = b33.copy()
  replaceCorner(b34, lb, 'lb')
  replaceCorner(b34, rt, 'rt')

  b35 = b19.copy()
  replaceCorner(b35, lt, 'lt')
  replaceCorner(b35, lb, 'lb')

  b36 = b19.copy()
  replaceCorner(b36, lt, 'lt')
  replaceCorner(b36, rt, 'rt')

  b37 = b36.copy()
  replaceCorner(b37, lb, 'lb')

  b38 = b36.copy()
  replaceCorner(b38, rb, 'rb')

  b39 = b19.copy()
  replaceCorner(b39, rb, 'rb')

  b40 = b19.copy()
  replaceCorner(b40, lb, 'lb')

  b41 = b19.copy()
  replaceCorner(b41, lb, 'lb')
  replaceCorner(b41, rt, 'rt')

  b42 = transparent

  b43 = b40.copy()
  replaceCorner(b43, rb, 'rb')

  b44 = b39.copy()
  replaceCorner(b44, rt, 'rt')

  b45 = b43.copy()
  replaceCorner(b45, lt, 'lt')

  b46 = b43.copy()
  replaceCorner(b46, rt, 'rt')

  b47 = b19.copy()
  replaceCorner(b47, rt, 'rt')

  b48 = b19.copy()
  replaceCorner(b48, lt, 'lt')

  if mode == 'full':
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
  elif mode == 'simple':
    arranged = [
      [b1, b34, b9, b4],
      [b3, b17, b2, b25],
      [b7, b8, b5, b6],
      [b15, b16, b13, b14]
    ]
  else:
    arranged = [[b1]]
  return suture(arranged)

