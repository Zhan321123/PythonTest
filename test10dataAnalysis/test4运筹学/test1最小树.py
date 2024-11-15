"""
运筹学-最小树问题
遍历法
"""
import itertools


def minTree(lines: dict):
    """
    遍历法求解最小树问题
    使用简单，但是太多线路就很慢
    :param lines: 所有线路及其值, ep:{'a-b':10, 'b-c':20, 'a-c':30}
    """
    # 数据初始化
    points = set()
    for line in lines:
        l, r = line.split('-')
        points.add(l)
        points.add(r)
    points = list(points)
    points.sort()
    # 问题检查
    print("问题检查{")
    print(f'\t点集:{points}')
    print(f'\t{len(points)}个点，{len(lines)}条线路')
    print("}")
    # 计算
    liness = list(itertools.permutations(list(lines)))
    hasRoad = []
    road = dict()
    for i in liness:
        passPoints = []
        passRoads = []
        length = 0
        for line in i:
            l, r = line.split('-')
            if (l not in passPoints) | (r not in passPoints):
                passPoints.extend([l, r])
                passRoads.append(line)
                length += lines[line]
        if len(passRoads) == len(points) - 1:
            passRoads.sort()
            pr = ''.join(passRoads)
            if pr not in hasRoad:
                hasRoad.append(pr)
                road[str(passRoads)] = length
    # 输出结果
    minValue = min(road.values())
    minRoad = [key for key, value in road.items() if value == minValue]
    print("最小树结果{")
    print(f'\t最短距离为:{minValue}')
    print('\t最短路径为:')
    for i in minRoad:
        print(f'\t{i}')
    print("}")


if __name__ == '__main__':
    ls = {'a-b': 18, 'a-g': 18, 'a-f': 19, 'b-g': 20,
          'g-f': 15, 'f-e': 3, 'e-d': 9, 'g-d': 15,
          'b-c': 8, 'c-d': 20}  # 所有线路
    minTree(ls)
