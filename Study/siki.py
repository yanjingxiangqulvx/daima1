import requests
from bs4 import BeautifulSoup

def siki2(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print([title.text.strip() for title in soup.select('.course-info > .title > a')])

    soup_next = soup.select_one('.cd-icon-arrow-right')

    if soup_next:
        url = 'http://www.sikiedu.com' + soup_next.parent.get('href')
        siki2(url)


siki2('http://www.sikiedu.com/course/explore?page=1')