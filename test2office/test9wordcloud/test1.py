import jieba
from wordcloud import WordCloud

with open('../file/text1.txt', 'r', encoding='utf-8') as file:
    s = file.read()

stopwords = ['成为', '依据']

wc = WordCloud(background_color='white', font_path='msyh.ttc', stopwords=stopwords,
               width=800,height=600)

wc.generate(s)

wc.to_file('file/wordcloud1.png')