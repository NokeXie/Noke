import requests
import json
def get_news():  # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note

#print(get_news())
print(json.dumps(get_news()[0],ensure_ascii=True))
print(json.dumps(get_news()[0],ensure_ascii=False))
print(json.dumps(get_news()[1],ensure_ascii=True))
print(json.dumps(get_news()[1],ensure_ascii=False))