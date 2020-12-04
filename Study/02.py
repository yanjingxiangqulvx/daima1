import urllib.request
from bs4 import BeautifulSoup

url = 'https://fanyi.baidu.com/?aldtype=16047'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)

# response = urllib.request.urlopen('https://www.douban.com/', None, 2)

html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# s = soup.find_all('a')
# print(soup.get_text())
# print(s)


s = soup.find_all('li')
for i in s:
       print(i.text)

# print(html)

# file = open('data02.txt', 'w', encoding = 'utf-8')
# file.write(html)
# file.close
