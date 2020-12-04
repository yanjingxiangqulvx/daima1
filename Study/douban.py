import requests
import csv
import xlwt
from bs4 import BeautifulSoup

url = 'https://music.douban.com/artists/genre_page/4/1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.42 Safari/537.36"
}
# urls = ['https://music.douban.com/artists/genre_page/4/={}'.format(str(i)) for i in range(1,6)]
# for x in urls:
#     re = requests.get(x, headers=headers)
#     req=BeautifulSoup(re.text,'lxml')

response=requests.get(url,headers=headers)
req=BeautifulSoup(response.text,'lxml')

s = req.select('div.ll > a')
a = req.select('div.ll > div')
for i in a:
    print(i.text)
for i in s:
    print(i.text)

wb = xlwt.Workbook()
ws = wb.add_sheet('Python',cell_overwrite_ok=True)
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()
style.alignment = alignment
ws.write_merge(0,0,0,19,'豆瓣民谣音乐人TOP100',style)

#写入数据wb.write(行，列，内容)
for i in range(1,2):
    for k in range(20):
        ws.write(i,k,s[k].text)
wb.save('file.xls')


#若存在文件，则打开csv文件；若不存在，则新建文件
#若不设置newline='',则每行数据会隔一行空白行
csvfile = open('csv_test.csv',encoding='utf-8',mode='w',newline='')
#将文件加载到csv对象中
writer = csv.writer(csvfile)
for i in s:
    writer.writerows([i.text])
# writer.writerows(data)
#关闭csv对象
csvfile.close()
