import xlwt
import csv
from bs4 import BeautifulSoup
import requests


douban_id = ['0', '20', '40', '60', '80']

url = ['https://book.douban.com/tag/%E6%BC%AB%E7%94%BB?start={}'.format(str(i)) for i in douban_id]

headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.42 Safari/537.36"
}


for x in url:
    html = requests.get(x, headers = headers)
    soup = BeautifulSoup(html.text, 'lxml')
    s = soup.select('h2 > a')
    for i in s:
        print(i.text)


wb = xlwt.Workbook()
ws = wb.add_sheet('Python',cell_overwrite_ok=True)
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style = xlwt.XFStyle()
style.alignment = alignment
ws.write_merge(0,0,0,19,'豆瓣读书漫画TOP100',style)
#写入数据wb.write(行，列，内容)

for i in range(1,20):
    for k in range(1,3):
        ws.write(i,k,s[i].text.strip())
wb.save('file1.xls')


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








