"""
字典生成词云图

command：
生成词云图
"""

import matplotlib
from wordcloud import WordCloud

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = {
    'Python': 96,
    'Java': 87,
    'C++': 46,
    'C#': 20,
    'PHP': 10,
    'Go': 17,
    'Ruby': 1,
    'Swift': 13,
    'Scala': 11,
    'Kotlin': 1,
    'Rust': 1,
}

# 创建词云图
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(data)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # 不显示坐标轴
plt.show()
