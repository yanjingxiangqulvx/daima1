import requests
headers = {"user-agent": "Mozilla/5.0"}


def getSid():
    url = 'https://music.taihe.com/v1/artist/list?pageSize=' + input('歌手数量: ')
    response = requests.get(url, headers=headers)
    singer = response.json()['data']['result']
    for i in range(len(singer)):
        print(str(i + 1) + '\t' + singer[i]['name'])
    return singer[int(input('序号: ')) - 1]['artistCode']


def getTSIDBySid(sid):
    url = 'https://music.taihe.com/v1/artist/song?artistCode=' + sid + '&pageSize=' + input('歌曲数量: ')
    response = requests.get(url, headers=headers)
    data = response.json()['data']['result']
    for i in range(len(data)):
        print(str(i + 1) + '\t' + data[i]['title'])
    return data[int(input('序号: ')) - 1]['TSID']


def getSongByTSID(TSID):
    url = 'https://music.taihe.com/v1/song/tracklink?TSID=' + TSID
    response = requests.get(url, headers=headers).json()
    print(response['data']['title'])
    return response['data']['path']


print(getSongByTSID(getTSIDBySid(getSid())))