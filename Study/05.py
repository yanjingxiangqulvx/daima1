import requests
from bs4 import BeautifulSoup

headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

# urls = [525, 536, 531, 505, 523]
urls = ['https://music.taihe.com/artist?pageNo={}'.format(str(i)) for i in range(1,3)]

for url in urls:
    html = requests.get(url, headers = headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, 'lxml')
    # s = soup.select('#__layout > div > div.container.page-container.page-main > div.list-box > div > div:nth-child(1) > div')
    # s = soup.select('div.el-col el-col-4')
    s = soup.find_all('div', 'list-item ellipsis')
    for i in s:
        print(i.text)
    #print(s)
