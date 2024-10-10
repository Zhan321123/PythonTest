import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 假设你有一个很长的文本
text = """
Your long text goes here, which will be used to generate the word cloud.
...
"""

# 创建WordCloud对象
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=None).generate(text)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # 不显示坐标轴
plt.show()

"""---------------------------------"""

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
