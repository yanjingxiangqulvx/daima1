import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}
for i in range(4):
    url = 'https://music.taihe.com/v1/artist/list?pageNo={}&pageSize=48'
    req = requests.get(url,headers=headers)
    json_data = req.json()['data']['result']
    for info in json_data:
        print(json_data['name'])


from urllib.request import urlretrieve

def go(blocknum, blocksiz,totalsize):
    percent = blocknum * blocksiz / totalsize
    if percent > 1:
        percent = 1
    print("\r", "已下载{:.2%}".format(percent), end='',flush=True)

def jQuery111308708897649529181_1602661084853(obj):
    url = obj['url']
    print('开始下载')

    urlretrieve(url, './music.mp3', go)

    print('\n下载完成')

jQuery111308708897649529181_1602661084853({
    "url": "http://m801.music.126.net/20201015160802/a310fcb275f5b56d2ed00198d3388be1/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/4387351108/698b/39d2/91d9/dabe5d3eb8e4efaeeb43dcfc72c70f52.mp3",
    "size": 11037301,
    "br": 320000
})