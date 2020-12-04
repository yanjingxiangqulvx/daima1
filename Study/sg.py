import requests
import json
import re
from bs4 import BeautifulSoup
url = 'https://music.taihe.com/v1/song/tracklink?sign=8f0641f066c6924a368eabb2c0d367b0&TSID={}'
urll = 'https://music.taihe.com/artist/A10048883'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}
def save_file(filename, content):
  with open(file=filename, mode="wb") as f:
    f.write(content)

def download_file(search_end):
    # reqq = requests.get(urll, headers=headers)
    # ret = re.compile(r'href="/song/(.*?)"', re.M|re.I).findall(reqq.text)
    # for i in range(0,2,1):
        reqqq = requests.get(url.format(search_end),headers=headers)
        singer_list = json.loads(reqqq.text)['data']
        response = requests.get(singer_list['path'])
        content = response.content
        print('正在下载《'+singer_list['title']+'》...')
        save_file(singer_list['title'] + '.mp3', content)
        response = requests.get(singer_list['lyric'])
        content = response.content
        save_file(singer_list['title'] + '.lrc', content)
        print('下载完成')

def search_file(name):
    song_list = []
    singer_list = []
    album_list = []
    search_url = 'https://music.taihe.com/search?word=' + name
    reqqq = requests.get(search_url,headers=headers)
    soup = BeautifulSoup(reqqq.text,'lxml')
    search_song_list = soup.find_all(class_="song ellipsis clearfix")
    search_singer_list = soup.find_all(class_="artist ellipsis")
    search_sing_list = soup.find_all(class_="album ellipsis")
    for i in search_song_list:
        song_list.append(i.text.replace(' \n','').replace(' ',''))
    for i in search_singer_list:
        singer_list.append(i.text.replace('\n','').replace(' ',''))
    for i in search_sing_list:
        album_list.append(i.text.replace(' \n','').replace(' ',''))
    temp = 1
    for i in range(0,len(singer_list),1):
        print(str(temp) + ':  歌曲名：' + song_list[i] + '   歌手名：' + singer_list[i] + '   专辑名：' + album_list[i])
        temp += 1
    print('请输入要下载的歌的序号：',end='')
    no = input()
    search_end_list = soup.find_all(class_='pr t clearfix')
    ret= []
    for i in search_end_list:
        no = int(no) - 1
        if int(no) == 0:
            ret = re.compile(r'href="/song/(.*?)"', re.M | re.I).findall(str(i))
    download_file(ret[0])


if __name__ == "__main__":
    print('请输入歌曲名：',end='')
    search_file(input())