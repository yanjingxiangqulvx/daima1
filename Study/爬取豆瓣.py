import csv
import requests
import lxml.etree as etree
import xlwt


def get_source(page):
    List = []
    url = 'https://movie.douban.com/top250?start={}'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    print(url)
    res = requests.get(url=url, headers=headers)
    print(res.status_code)
    html = etree.HTML(res.text)
    for i in range(1, 26):
        list = []
        name = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]/text()".format(i))
        info = html.xpath("/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()".format(i))
        score = html.xpath(
            "/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[2]/text()".format(i))
        slogan = html.xpath(
            "/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[2]/span/text()".format(i))
        try:
            list.append(name[0])
        except:
            list.append('----')
        try:
            list.append(info[0].replace(' ', '').replace('\n', ''))
        except:
            list.append('----')
        try:
            list.append(info[1].replace(' ', '').replace('\n', ''))
        except:
            list.append('----')
        try:
            list.append(score[0])
        except:
            list.append('----')
        try:
            list.append(slogan[0])
        except:
            list.append('----')

        List.append(list)

    return List


n = 1
LIST = []
for i in range(0, 100, 25):
    print('第{}页'.format(n))
    n += 1
    List = get_source(i)
    LIST.append(List)


def excel_write(LIST):
    book = xlwt.Workbook()
    sheet = book.add_sheet(u'sheetname', cell_overwrite_ok=True)
    r = 1
    for i in LIST:  # 有10页
        for j in i:  # 有25条数据
            c = 2
            for x in j:  # 有5组数据
                print(x)
                sheet.write(r, c, x)
                c += 1
            r += 1

    book.save(r'douban1.xls')  # 保存代码

excel_write(LIST)

csvfile = open('csv_test.csv',encoding='utf-8',mode='w',newline='')
#将文件加载到csv对象中
writer = csv.writer(csvfile)
for i in LIST:
    writer.writerows(i)
#关闭csv对象
csvfile.close()
excel_write(LIST)