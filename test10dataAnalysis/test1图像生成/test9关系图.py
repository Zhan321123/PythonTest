"""
继承关系图

暂不妙
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import networkx as nx

# 假设我们有一个关系字典
relations_dict = {
    'misc': ['tk', 'window', 'widget', 'ttk'],
    'widget': ['button', 'label', 'entry'],
    'ttk': ['notebook', 'labelFrame'],
    'button': ['master', 'text', 'command']
}

G = nx.DiGraph()

for person, relatives in relations_dict.items():
    for relative in relatives:
        G.add_edge(person, relative)

pos = nx.spring_layout(G)  # 布局算法
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.title('继承图')
plt.show()
