"""
不重复元素合集 set()
    .add(element) 添加元素
    .update(Sequence[element]) 添加多个元素

    .remove(element) 删除元素，如果元素不存在，则报错
    .discard(element) 删除元素，如果元素不存在，则不报错
    .pop() 删除并返回集合中的第一个元素
    .clear() 清空集合

    .difference(set) 返回两个集合的差集
    .intersection(set) 返回两个集合的交集
    .union(set) 返回两个集合的并集

    .isdisjoint(set) 判断两个集合是否没有交集
    .issubset(set) 判断当前集合是否是另一个集合的子集
    .issuperset(set) 判断当前集合是否是另一个集合的父集
    .symmetric_difference(set) 返回两个集合的对称差集



"""

s = set()
s.add(1)
s.add(2)
s.add(1)
print(s)

s.update([1,2,3,4])
print(s)

s.remove(1)
# s.remove(1)
s.discard(1)