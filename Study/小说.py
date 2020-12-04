import requests
from lxml import etree
import time
import random
import docx


path = r'C:\Users\asus\Desktop\异世探险队/'
headers = {
    "Referer": "http://www.xbiquge.la/71/71121/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"
}

def get_urls():
    url = "http://www.xbiquge.la/71/71121/"
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    # 所有章节的url列表
    url_list = ['http://www.xbiquge.la' + x for x in html.xpath('//div[@id="list"]/dl/dd/a/@href')]
    return url_list

def get_text(url):
    rep = requests.get(url, headers=headers)
    rep.encoding = 'utf-8'
    dom = etree.HTML(rep.text)
    name = dom.xpath('//div[@class="bookname"]/h1/text()')[0]
    text = dom.xpath('//div[@id="content"]/text()')
    # 写入word
    document = docx.Document()
    document.add_paragraph(text)
    document.save('异界探险队.docx')
    # 存放本地并保存为txt格式
    # with open(path + f'{name}.txt, 'w', encoding='utf-8') as f:
    #     for con in text:
    #         f.write(con)
    # print(f'{name} 下载完成')

def main():
    urls = get_urls()
    for url in urls:
        get_text(url)
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    main()