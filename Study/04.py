import requests
import json

urls =  ['https://music.taihe.com/v1/artist/list?pageNo={}&pageSize=48'.format(str(i)) for i in range(1,3)]
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}
for url in urls:
    req = requests.get(url,headers=headers)
    html = req.text.encode('utf-8')
    singer_list = json.loads(html)['data']['result']
    for i in singer_list:
        print(i['name'])

# json.loads(...)方法，将字符串格式的json数据转化为字典格式，然后利用字典的键-值索引和列表索引配合使用解析json数据或者使用get()方法和列表索引解析。