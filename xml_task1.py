import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
res = []

for item in root.iter('item'):
    res.append({
        'pubDate': item.find('pubDate').text,
        'title': item.find('title').text,
    })

with open("news.json", "w") as file_news_json:
    file_news_json.write(json.dumps(res))