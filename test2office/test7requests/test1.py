"""
爬取图片
"""
import requests
url = 'https://i.mcmod.cn/editor/upload/20231222/1703256969_2_KgMF.png'

resp = requests.get(url)

with open('l.png','wb')as file:
    file.write(resp.content)