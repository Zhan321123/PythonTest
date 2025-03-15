import math
import random

# 生成 20 个随机坐标点
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(20)]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# 贪心算法
start = 0  # 起始点
visited = [start]
unvisited = list(range(1, len(points)))
total_distance = 0

while unvisited:
    min_distance = float('inf')
    min_index = None
    for i in unvisited:
        dist = distance(points[visited[-1]], points[i])
        if dist < min_distance:
            min_distance = dist
            min_index = i
    visited.append(min_index)
    unvisited.remove(min_index)
    total_distance += min_distance

# 回到起始点
total_distance += distance(points[visited[-1]], points[start])
visited.append(start)

print("近似最短路径：", [points[i] for i in visited])
print("路径总长度：", total_distance)