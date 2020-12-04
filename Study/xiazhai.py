import requests
import json
import jsonpath

# 获取歌手的歌曲id
urll = ['https://music.taihe.com/v1/artist/song?&artistCode=A10048883&pageNo={}&pageSize=50'.format(str(a)) for a in range(1,2)]
header = {
     'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.42 Safari/537.36'
 }
for x in urll:
    reqq = requests.get(x, headers = header)
    htmll = reqq.text.encode('utf-8')
    # singer_id = json.loads(htmll)['data']['result']
    data = json.loads(htmll)
    singer_td = jsonpath.jsonpath(data, "$..id")


# mp3_id = ['T10038826793', 'T10038920637', 'T10044518961', 'T10038826794', 'T10038957307']
urls = ['https://music.taihe.com/v1/song/tracklink?&TSID={}'.format(str(i)) for i in singer_td]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

for url in urls:
    req = requests.get(url,headers=headers)
    html = req.text.encode('utf-8')

    singer_list = json.loads(html)['data']['path']
    singer_name = json.loads(html)['data']['title']
    print(singer_list)
    print(singer_name)
    # print(singer_list)

# mp3下载本地
    mp3_xz = requests.get(singer_list)
    with open(r'C:\Users\asus\Desktop\mp3\%s.mp3'%singer_name, 'wb')as f:
        f.write(mp3_xz.content)
        print('正在下载《' + singer_name + '》...')
        print('下载完成')



