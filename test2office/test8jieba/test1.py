"""
第三方包jieba
用于对中文进行'分词'
"""

import jieba

# 打开一个txt文件
with open('../file/text1.txt', 'r', encoding='utf-8') as file:
    s = file.read()

# jieba分词成列表
l = jieba.lcut(s)

# 去重得到set集合
s1 = set(l)

# 查找每个词出现的次数
c = []
for i in s1:
    if len(i) >= 2:
        c.append((l.count(i), i))
c.sort(reverse=True)
print(c[0:11])
