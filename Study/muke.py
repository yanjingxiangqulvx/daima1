import requests
from bs4 import BeautifulSoup

headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

# urls = [525, 536, 531, 505, 523]
urls = ['https://www.imooc.com/course/list?page={}'.format(str(i)) for i in range(1,29)]

for url in urls:
    html = requests.get(url, headers = headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, 'lxml')
    s = soup.select('h3.course-card-name')
    for i in s:
        print(i.text)