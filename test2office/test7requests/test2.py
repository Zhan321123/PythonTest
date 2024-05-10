"""
爬虫requests
"""
import requests
import re

url = 'https://weather.cma.cn/'
resp = requests.get(url)
resp.encoding = 'utf-8'
text = resp.text

rank = re.findall('<div class="rank">(.*)</div>', text)
print(rank)
