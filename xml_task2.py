import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
res = []

for item in root.iter('item'):
    content = {}
    for son in item:
        content[son.tag] = son.text
    res.append(content)

with open("news_2.json", "w") as file_news2_json:
    file_news2_json.write(json.dumps(res))