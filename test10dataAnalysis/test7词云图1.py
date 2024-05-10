"""
英文句子长文本生成词云图

command:
根据text长文本对象生成词云图
"""
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