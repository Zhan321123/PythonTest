"""
wordcloud库绘制词云图
FIXME 中文编码问题
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def wordOfText(ax: plt.Axes, ts: str):
    """通过长文本创建词云图"""
    wordcloud = WordCloud(width=800, height=400,  # 设置图片宽高
                          background_color='white', stopwords=None,  # 停用词
                          colormap=matplotlib.colormaps['rainbow']  # 色带
                          ).generate(ts)
    ax.imshow(wordcloud)
    ax.axis("off")  # 不显示坐标轴


def wordOfFrequencies(ax: plt.Axes, pds: dict):
    """通过词频创建词云图"""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(pds)
    ax.imshow(wordcloud)
    ax.axis("off")


if __name__ == '__main__':
    text1 = """
    this is a test text, for every line, we can use it to test the word cloud. 
    You can use it to test the word cloud.
    But it is not easy to use.
    """
    text2 = {
        'Python': 96, 'Java': 87, 'C++': 46, 'C#': 20, 'PHP': 10, 'Go': 17, 'Ruby': 1, 'Swift': 13,
        'Scala': 11, 'Kotlin': 1, 'Rust': 1,
    }

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs = axs.flatten()
    wordOfText(axs[0], text1)
    wordOfFrequencies(axs[1], text2)

    plt.show()
