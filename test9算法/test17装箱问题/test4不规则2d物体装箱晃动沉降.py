import math
import random
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, box
from shapely.affinity import rotate, translate

from test8文件.test1io import increasePath
from test9算法.test2排序.test3特殊排序 import followOrderSort

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def rectangleIntersection(rec1: (float, float, float, float), rec2: (float, float, float, float)) -> bool:
  """
  矩形相交
  :param rec1: (x_low, y_low, x_high, y_high)
  :param rec2: (x_low, y_low, x_high, y_high)
  """
  if rec1[0] > rec2[2] or rec1[2] < rec2[0] or rec1[3] < rec2[1] or rec1[1] > rec2[3]:
    return False
  return True


def polygonIntersection(poly1: Polygon, poly2: Polygon) -> bool:
  """
  多边形相交
  :param poly1: Polygon
  :param poly2: Polygon
  """
  if rectangleIntersection(poly1.bounds, poly2.bounds) and poly1.intersects(poly2):
    return True
  return False


def outOfBox(obj: Polygon, boxObj: (float, float, float, float)) -> (bool, bool):
  """
  检测obj是否在box内，obj比box小
  :param obj:
  :param boxObj: (x_low, y_low, x_high, y_high)
  :return: (x轴出界, y轴出界)
  """
  x_out, y_out = False, False
  if obj.bounds[0] < boxObj[0] or obj.bounds[2] > boxObj[2]:
    x_out = True
  if obj.bounds[1] < boxObj[1] or obj.bounds[3] > boxObj[3]:
    y_out = True
  return x_out, y_out


def gravitation(obj: Polygon, others: list[Polygon], k: float = 1) -> (float, float):
  """
  引力
  :param obj: Polygon
  :param others: list[Polygon]
  :param k: float, 系数
  :return: (Fx, Fy)
  """
  objG = obj.area
  otherGs = [other.area for other in others]
  ds = [(obj.centroid.x - other.centroid.x) ** 2 + (obj.centroid.y - other.centroid.y) ** 2 for other in others]
  Fxs = [k * objG * otherG / (ds[i] + 1e-6) for i, otherG in enumerate(otherGs)]
  Fxs = [-Fx if obj.centroid.x > others[i].centroid.x else Fx for i, Fx in enumerate(Fxs)]
  Fys = [k * objG * otherG / (ds[i] + 1e-6) for i, otherG in enumerate(otherGs)]
  Fys = [-Fy if obj.centroid.y > others[i].centroid.y else Fy for i, Fy in enumerate(Fys)]
  return sum(Fxs), sum(Fys)


def objsIntersection(objs: list[Polygon]) -> bool:
  """
  多个物体是否有相交
  :param objs: list[Polygon]
  """
  for i in range(len(objs)):
    for j in range(i + 1, len(objs)):
      if polygonIntersection(objs[i], objs[j]):
        return True
  return False


def generateObject(numSides=5, minSize=10, maxSize=40, maxConcavity=0.15) -> Polygon:
  """
  生成接近现实物体的多边形：凸形为主，尺寸协调，边缘平滑，默认参数下平均面积：400
  :param minSize: 最小尺寸
  :param maxSize: 最大尺寸
  :param maxConcavity: 凹形程度 (0, 1]，越小越平滑
  :return:
  """
  center = (0, 0)
  angles = []
  baseAngle = 2 * 3.14159 / numSides
  for i in range(numSides):
    angle = i * baseAngle + random.uniform(-0.15 * baseAngle, 0.15 * baseAngle)
    angles.append(angle)

  avgRadius = random.uniform(minSize / 2, maxSize / 2)
  radii = [avgRadius * random.uniform(0.7, 1.3) for _ in range(numSides)]  # 半径扰动稍大，增加形状多样性

  verts = []
  for angle, radius in zip(angles, radii):
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    verts.append((x, y))

  # 轻微凹形处理
  if numSides >= 4:
    ao_index = random.randint(0, numSides - 1)
    prev_vert = verts[(ao_index - 1) % numSides]
    next_vert = verts[(ao_index + 1) % numSides]
    concavity = random.uniform(0, maxConcavity)
    new_x = verts[ao_index][0] * (1 - concavity) + (prev_vert[0] + next_vert[0]) / 2 * concavity
    new_y = verts[ao_index][1] * (1 - concavity) + (prev_vert[1] + next_vert[1]) / 2 * concavity
    verts[ao_index] = (new_x, new_y)

    # 按角度排序，避免自交
  verts = sorted(verts, key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))

  try:
    obj = Polygon(verts)
    if obj.area < minSize * minSize * 0.05:  # 过滤过小物体
      return generateObject(numSides, minSize, maxSize, maxConcavity)
    return obj
  except Exception as e:
    print(e)
    return generateObject(numSides, minSize, maxSize, maxConcavity)


def scatter(objects: list[Polygon], boxObj: Polygon, maxTimes=1000):
  n = len(objects)
  sn = 0
  while objsIntersection(objects):
    sn += 1
    if sn > maxTimes:
      break
    for i in range(n):
      intersectsObj = []
      for j in range(n):
        if i != j and polygonIntersection(objects[i], objects[j]):
          intersectsObj.append(objects[j])
      if len(intersectsObj) == 0:
        continue
      selfArea = objects[i].area
      fx, fy = gravitation(objects[i], intersectsObj, k=0.1)
      m = translate(objects[i], -fx / selfArea, -fy / selfArea)
      outX, outY = outOfBox(m, boxObj.bounds)
      if not outX and not outY:
        objects[i] = m
      elif outX or outY:
        objects[i] = translate(objects[i], 0 if outX else -fx / selfArea, 0 if outY else -fy / selfArea)


def shakingAndSettlement(objects: list[Polygon], boxObj: Polygon, shakingDistance: float = 1, maxTimes=1000):
  """
  随机晃动
  :param objects:
  :param boxObj:
  :param shakingDistance:
  :param maxTimes:
  :return:
  """
  n = len(objects)
  _, high = getHighestPoint(objects)
  for i in range(maxTimes):
    for i in range(n):
      m = rotate(objects[i], random.uniform(-5, 5), origin=(0, 0))
      m = translate(m, random.uniform(-shakingDistance, shakingDistance), random.uniform(0, shakingDistance))
      outX, outY = outOfBox(m, boxObj.bounds)
      # if outY:

    scatter(objects, boxObj)
    _, h2 = getHighestPoint(objects)
    # if high - h2 < 0.01:
    #   break
    high = h2
    print(f"当前高度: {high}")


def getDownPoints(objects: list[Polygon]) -> [float]:
  """
  获取物体的底点
  :param objects: list[Polygon]
  """
  return [obj.bounds[1] for obj in objects]


def getHighestPoint(objects: list[Polygon]) -> (Polygon, float):
  """
  获取最高点
  :param objects: list[Polygon]
  """
  highestPoint = 0
  highestObj = objects[0]
  for obj in objects:
    if obj.bounds[3] > highestPoint:
      highestPoint = obj.bounds[3]
      highestObj = obj
  return highestObj, highestPoint


def figure(objs: list[Polygon], boxObj: Polygon):
  chestW, chestH = boxObj.bounds[2] - boxObj.bounds[0], boxObj.bounds[3] - boxObj.bounds[1]
  plt.figure(figsize=(8, 6))
  plt.plot([0, chestW, chestW, 0, 0], [0, 0, chestH, chestH, 0], 'b-', linewidth=2)
  for obj in objs:
    verts = list(obj.exterior.coords)
    x, y = zip(*verts)
    plt.fill(x, y, alpha=0.7)
  plt.grid(True, linestyle='--', alpha=0.5)
  plt.axis('equal')  # 等比例显示，避免形状变形
  plt.tight_layout()
  plt.savefig(increasePath(Path("./result.png")))


if __name__ == '__main__':
  chestW, chestH = 200, 250
  chest = box(0, 0, chestW, chestH)
  n = 50
  objs = [generateObject(numSides=random.randint(3, 7)) for _ in range(n)]
  objAreas = [obj.area for obj in objs]

  objsArea = sum(objAreas)
  chestArea = chest.area
  print(f"箱子面积：{chestArea:.1f}, 物体面积：{objsArea:.1f}, 理想利用率：{objsArea / chestArea:.2%}")

  # 随机放置物体
  for i in range(n):
    while True:
      obj = translate(objs[i], random.randint(0, chestW), random.randint(0, chestH))
      if obj.within(chest):
        break
    objs[i] = obj

  # 散开
  scatter(objs, chest, maxTimes=1000)
  print("散开完成")
  figure(objs, chest)

  # 晃动
  shakingAndSettlement(objs, chest, shakingDistance=2, maxTimes=10)
  print("晃动完成")

  figure(objs, chest)
