"""
1 若干矩形装入固定尺寸的箱子，所需最少箱子数
2 若干矩形装入一个箱子，所需最小尺寸箱子
"""
import math
import itertools
import operator
from collections import deque

import matplotlib
import numpy as np
from matplotlib import pyplot as plt


# 保持Point和Rectangle类不变
class Point(object):
  __slots__ = ('x', 'y')

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return (self.x == other.x and self.y == other.y)

  def __repr__(self):
    return "P({}, {})".format(self.x, self.y)

  def distance(self, point):
    return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

  def distance_squared(self, point):
    return (self.x - point.x) ** 2 + (self.y - point.y) ** 2


class Rectangle(object):
  __slots__ = ('width', 'height', 'x', 'y', 'rid')

  def __init__(self, x, y, width, height, rid=None):
    assert (height >= 0 and width >= 0)
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.rid = rid

  @property
  def bottom(self):
    return self.y

  @property
  def top(self):
    return self.y + self.height

  @property
  def left(self):
    return self.x

  @property
  def right(self):
    return self.x + self.width

  @property
  def corner_top_l(self):
    return Point(self.left, self.top)

  @property
  def corner_top_r(self):
    return Point(self.right, self.top)

  @property
  def corner_bot_r(self):
    return Point(self.right, self.bottom)

  @property
  def corner_bot_l(self):
    return Point(self.left, self.bottom)

  def __lt__(self, other):
    return self.area() < other.area()

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False
    return (self.width == other.width and
            self.height == other.height and
            self.x == other.x and
            self.y == other.y)

  def __hash__(self):
    return hash((self.x, self.y, self.width, self.height))

  def __iter__(self):
    yield self.corner_top_l
    yield self.corner_top_r
    yield self.corner_bot_r
    yield self.corner_bot_l

  def __repr__(self):
    return "R({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)

  def area(self):
    return self.width * self.height

  def move(self, x, y):
    self.x = x
    self.y = y

  def contains(self, rect):
    return (rect.y >= self.y and
            rect.x >= self.x and
            rect.y + rect.height <= self.y + self.height and
            rect.x + rect.width <= self.x + self.width)

  def intersects(self, rect, edges=False):
    if edges:
      if (self.bottom > rect.top or self.top < rect.bottom or
          self.left > rect.right or self.right < rect.left):
        return False
    else:
      if (self.bottom >= rect.top or self.top <= rect.bottom or
          self.left >= rect.right or self.right <= rect.left):
        return False
    return True

  def intersection(self, rect, edges=False):
    if not self.intersects(rect, edges=edges):
      return None

    bottom = max(self.bottom, rect.bottom)
    left = max(self.left, rect.left)
    top = min(self.top, rect.top)
    right = min(self.right, rect.right)

    return Rectangle(left, bottom, right - left, top - bottom)


class PackingAlgorithm(object):
  def __init__(self, width, height, rot=True, *args, **kwargs):
    self.width = width
    self.height = height
    self.rot = rot  # 旋转控制参数
    self.rectangles = []

  def reset(self):
    self.rectangles = []

  def fitness(self, width, height):
    raise NotImplementedError

  def add_rect(self, width, height, rid=None):
    raise NotImplementedError


class MaxRects(PackingAlgorithm):
  def __init__(self, width, height, rot=True, *args, **kwargs):
    super(MaxRects, self).__init__(width, height, rot, *args, **kwargs)
    self._max_rects = [Rectangle(0, 0, self.width, self.height)]

  def _rect_fitness(self, max_rect, width, height):
    if width <= max_rect.width and height <= max_rect.height:
      return 0
    else:
      return None

  def _select_position(self, w, h):
    if not self._max_rects:
      return None, None

    # 生成适合度计算迭代器
    fitn = ((self._rect_fitness(m, w, h), w, h, m) for m in self._max_rects
            if self._rect_fitness(m, w, h) is not None)

    # 只有当允许旋转时才考虑旋转情况
    fitr = []
    if self.rot and w != h:  # 避免相同尺寸时的无效旋转
      fitr = ((self._rect_fitness(m, h, w), h, w, m) for m in self._max_rects
              if self._rect_fitness(m, h, w) is not None)

    fit = itertools.chain(fitn, fitr)

    try:
      _, w, h, m = min(fit, key=operator.itemgetter(0))
    except ValueError:
      return None, None

    return Rectangle(m.x, m.y, w, h), m

  def _generate_splits(self, m, r):
    new_rects = []

    if r.left > m.left:
      new_rects.append(Rectangle(m.left, m.bottom, r.left - m.left, m.height))
    if r.right < m.right:
      new_rects.append(Rectangle(r.right, m.bottom, m.right - r.right, m.height))
    if r.top < m.top:
      new_rects.append(Rectangle(m.left, r.top, m.width, m.top - r.top))
    if r.bottom > m.bottom:
      new_rects.append(Rectangle(m.left, m.bottom, m.width, r.bottom - m.bottom))

    return new_rects

  def _split(self, rect):
    max_rects = deque()

    for r in self._max_rects:
      if r.intersects(rect):
        max_rects.extend(self._generate_splits(r, rect))
      else:
        max_rects.append(r)

    self._max_rects = list(max_rects)

  def _remove_duplicates(self):
    contained = set()
    for m1, m2 in itertools.combinations(self._max_rects, 2):
      if m1.contains(m2):
        contained.add(m2)
      elif m2.contains(m1):
        contained.add(m1)

    self._max_rects = [m for m in self._max_rects if m not in contained]

  def fitness(self, width, height):
    assert (width > 0 and height > 0)

    rect, max_rect = self._select_position(width, height)
    if rect is None:
      return None

    return self._rect_fitness(max_rect, rect.width, rect.height)

  def add_rect(self, width, height, rid=None):
    assert (width > 0 and height > 0)

    rect, _ = self._select_position(width, height)
    if not rect:
      return None

    self._split(rect)
    self._remove_duplicates()

    rect.rid = rid
    self.rectangles.append(rect)
    return rect

  def reset(self):
    super(MaxRects, self).reset()
    self._max_rects = [Rectangle(0, 0, self.width, self.height)]


class MaxRectsBssf(MaxRects):
  def _rect_fitness(self, max_rect, width, height):
    if width > max_rect.width or height > max_rect.height:
      return None
    return min(max_rect.width - width, max_rect.height - height)


class EncloseFixedRatio:
  def __init__(self, rectangles=None, rotation=True, pack_algo=MaxRectsBssf):
    self._rectangles = rectangles if rectangles else []
    self._rotation = rotation  # 旋转控制参数
    self._pack_algo = pack_algo
    self._max_width = None
    self._max_height = None

  def add_rect(self, width, height):
    self._rectangles.append((width, height))

  def set_max_dimensions(self, max_width=None, max_height=None):
    self._max_width = max_width
    self._max_height = max_height

  def _get_min_max_dimensions(self):
    if not self._rectangles:
      return (0, 0, 0, 0, 0)

    total_area = sum(w * h for w, h in self._rectangles)

    if self._rotation:
      max_side = max(max(w, h) for w, h in self._rectangles)
      min_width = max(min(w, h) for w, h in self._rectangles)
      max_possible_width = sum(max(w, h) for w, h in self._rectangles)
      max_possible_height = sum(max(w, h) for w, h in self._rectangles)
    else:
      max_side = max(h for w, h in self._rectangles)
      min_width = max(w for w, h in self._rectangles)
      max_possible_width = sum(w for w, h in self._rectangles)
      max_possible_height = sum(h for w, h in self._rectangles)

    if self._max_width and self._max_width < max_possible_width:
      max_possible_width = self._max_width
    if self._max_height and self._max_height < max_possible_height:
      max_possible_height = self._max_height

    return (total_area, min_width, max_side, max_possible_width, max_possible_height)

  def _refine_candidate(self, width, height):
    packer = self._pack_algo(width, height, rot=self._rotation)

    for w, h in self._rectangles:
      if not self._rotation:
        if not packer.add_rect(w, h):
          return None
      else:
        if not packer.add_rect(w, h):
          return None

    if len(packer.rectangles) != len(self._rectangles):
      return None

    new_height = max(rect.top for rect in packer.rectangles)
    new_width = max(rect.right for rect in packer.rectangles)

    return (new_width, new_height, packer)

  def find_min_container(self, ratio):
    if not self._rectangles:
      return (0, 0, [])

    total_area, min_width, max_side, max_possible_width, max_possible_height = self._get_min_max_dimensions()

    # 计算最小高度下限
    min_h_area = math.sqrt(total_area / ratio)
    min_h = max(min_h_area, max_side)

    # 计算最大高度上限
    if ratio * max_possible_height < min_width:
      max_h = max_possible_width / ratio
    else:
      max_h = max_possible_height

    # 二分法搜索
    low, high = min_h, max_h
    best_solution = None
    best_area = float('inf')
    eps = 1e-3  # 精度控制

    while high - low > eps:
      mid_h = (low + high) / 2
      mid_w = ratio * mid_h

      # 检查是否超过最大限制
      if self._max_width and mid_w > self._max_width:
        high = mid_h
        continue
      if self._max_height and mid_h > self._max_height:
        low = mid_h
        continue

      # 验证当前尺寸是否可行
      result = self._refine_candidate(mid_w, mid_h)
      if result:
        w, h, packer = result
        current_area = w * h
        if current_area < best_area:
          best_area = current_area
          best_solution = (w, h, packer)
        high = mid_h
      else:
        low = mid_h

    # 最后检查一次最佳可能值
    final_w = ratio * high
    final_result = self._refine_candidate(final_w, high)
    if final_result:
      w, h, packer = final_result
      current_area = w * h
      if current_area < best_area:
        best_solution = (w, h, packer)

    if best_solution:
      w, h, packer = best_solution
      positions = [
        (rect.x, rect.y, rect.width, rect.height)
        for rect in packer.rectangles
      ]
      return (w, h, positions)
    else:
      return None


def showRectInBox(boxWH: [int, int, int, int], boxSize: [int, int]):
  matplotlib.use('TkAgg')
  plt.figure()
  ax = plt.gca()
  for x, y, w, h in boxWH:
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor='green', edgecolor='blue'))
    ax.text(x + w / 2, y + h / 2, f"{w}x{h}", color='black', ha='center', va='center')
  ax.autoscale_view()
  ax.set_aspect('equal', adjustable='box')
  ax.set_xlim(0, boxSize[0])
  ax.set_ylim(boxSize[1],0)
  plt.show()


# 使用示例
if __name__ == "__main__":
  # 创建一些矩形
  # rectangles = [
  #   (10, 20), (15, 5), (8, 12), (20, 15), (5, 5),
  #   (10, 10), (5, 10), (5, 10), (5, 10), (5, 10),
  # ]
  np.random.seed(42)
  rectangles = np.random.randint(1, 100, size=(20, 2))

  # 创建求解器，允许旋转，使用最佳短边适配算法
  encloser = EncloseFixedRatio(rotation=False, pack_algo=MaxRectsBssf)
  for w, h in rectangles:
    if w>h:
      encloser.add_rect(w, h)
    else:
      encloser.add_rect(h, w)

  # 设置最大尺寸限制（可选）
  # encloser.set_max_dimensions(max_width=100, max_height=100)

  # 查找宽高比为16:9的最小容器
  ratio = 16 / 9
  result = encloser.find_min_container(ratio)

  if result:
    width, height, positions = result
    print(f"最小箱子尺寸: 宽 {width:.2f}, 高 {height:.2f} (宽高比 {ratio:.2f})")
    print(f"箱子面积: {width * height:.2f}")
    print(f"空间利用率: {(sum(w * h for w, h in rectangles))/(width * height):.2%}")
    print("矩形位置:")
    for i, (x, y, w, h) in enumerate(positions):
      print(f"  矩形 {i + 1}: 位置({x:.2f}, {y:.2f}), 尺寸 {w:.2f}x{h:.2f}")
    showRectInBox(positions, [width, height])
  else:
    print("无法找到满足条件的箱子")
