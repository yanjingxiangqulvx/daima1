import os
import requests
from lxml import etree
import csv
import re
import datetime
import time
from openpyxl import Workbook
import csv



headers={
'cookie': '_zap=6898b967-8389-4b51-984f-0d0eb0a5c69a; d_c0="AJBbnabkJBKPTmOoUtZXeygAz2fRsqh8WhM=|1604493503"; capsion_ticket="2|1:0|10:1606297866|14:capsion_ticket|44:MDU2YjcwOTFkMjg0NGY0NmE2NWVkZjRhOWNhYzc3OGU=|f3cc1ef49f514d18088bef2ecb89715965fe4bd290c6ddd4c1187c6868a16937"; z_c0="2|1:0|10:1606297898|4:z_c0|92:Mi4xWTVPREdnQUFBQUFBa0Z1ZHB1UWtFaVlBQUFCZ0FsVk5LbmVyWUFBZng3LXdpYzhDN3lsTHhIVjF6TENZeklmV2RB|21e99a6d12d09bd1bb4b4a2e84258685313625228f36e9613e34fb50e98a61fa"; tst=h; tshl=; _xsrf=539210e5-9a26-445a-ac0d-4ce4ce2d0671; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1605787618,1606294778,1606557854,1606565067; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1606565121; KLBRSID=81978cf28cf03c58e07f705c156aa833|1606565138|1606565079',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

headers1={
'cookie': 'q_c1=ca2a3b4d27bf473ca0345415d12265d1|1577799835000|1576678428; _zap=69ce3c63-7044-44d9-ad77-eed640e8a4f4; d_c0="AEAkC4pqhhCPTkBkE1-CPssbaUmJhKLLkoA=|1576678423"; __utmv=51854390.100-1|2=registration_date=20180517=1^3=entry_date=20180517=1; _ga=GA1.2.1372291736.1577805468; __utmz=51854390.1586157746.11.11.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=51854390.1372291736.1577805468.1586157746.1589898462.12; z_c0="2|1:0|10:1592837225|4:z_c0|92:Mi4xT3RWOENRQUFBQUFBUUNRTGltcUdFQ1lBQUFCZ0FsVk5hUkxlWHdCT3o2Zm4xZllnNFN3ZUZVRkpKaThlQXF2bGl3|3359b62f363963a7cb255bae6ad86bec9ff8e99bbc1a9fb2863a0da4f557a57b"; capsion_ticket="2|1:0|10:1592837226|14:capsion_ticket|44:ZDM4YzQ3NzUwNzY4NGI1OGE3Yjk1MzA0MGY4OWRlOWQ=|665e9c1c18df05ddfb276e4c4bee0bf79a4eaccbc3dee9b650e5e23a09dc6140"; _xsrf=91f3c54d-d4b8-45bb-8981-62a291641148; SESSIONID=dzH0MVFgBL9yx1cln1WyvivHUvJwOGYJpzqmjN4EWBl; JOID=VlkcBkJ6BXakO-D6TXudY1xDvXVRG3cymHuztCY1TEfRT9ycKcZRd_oz7f5N4-tvNP3h_w69oc1ukkJ1E09GCls=; osd=UVARAU19DHujNOfzQHySZFVOunpWEno1l3y6uSE6S07cSNObIMtWeP064PlC5OJiM_Lm9gO6rspnn0V6FEZLDVQ=; q_c1=8022f284108848f5b86cfebeeece12b0|1594042354000|1577283701000; _gid=GA1.2.142072253.1594296730; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594522010,1594563206,1594563943,1594566766; tst=h; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1594567343; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1594567342|1594563081',
'referer': 'https://www.zhihu.com/question/406493288',
'sec-fetch-mode': 'navigate',#cors
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}


def get_parse(response):
    html=etree.HTML(response)
    # 获取知乎热榜排名标题热度
    ret = html.xpath("//section[@class='HotItem']")
    D=[]
    for item in ret:
        try:
            rank=item.xpath(".//div[@class='HotItem-index']/div/text()")[0]
            title=item.xpath(".//div[@class='HotItem-content']/a/@title")[0]
            rots=item.xpath(".//div[@class='HotItem-metrics HotItem-metrics--bottom']/text()")[0]
            rot = rots.replace(' 万热度', '') + '0000'
            href=item.xpath(".//div[@class='HotItem-content']/a/@href")[0]
            time=datetime.datetime.now().strftime('%Y-%m-%d')
            message=get_content(href)
            answers=str(message['answer'])
            answer = int(answers.replace(',',''))
            guanzhu=str(message['guanzhu'])
            liulan=str(message['liulan'])
            data=[rank,title,rot,href,answer,guanzhu,liulan,time]
            print(data)
            D.append(data)
        except:
            pass
    # print(D)
    save(D)


def get_content(href):
    try:
        response = requests.get(href, headers=headers1).text
        data={}
        html=etree.HTML(response)
        answer=html.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[1]/h4/span/text()')[0]
        data['answer']=answer
        guanzhu=re.findall('</div><strong class="NumberBoard-itemValue" title="(.*?)">(.*?)</strong></div>',response)[0][0]
        data['guanzhu']=guanzhu
        liulan = re.findall('</div><strong class="NumberBoard-itemValue" title="(.*?)">(.*?)</strong></div>', response)[0][0]
        data['liulan'] = liulan
        return data
    except:
        pass

def save(name):
    with open('./知乎热榜.csv', 'a', newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(name)

def main():
    list2=['排名','标题','热度','回答链接','回答数','关注数','浏览数','时间']
    if os.path.exists('知乎热榜.csv'):  # 判断文件是否存在，如果存在则删除
        os.remove('知乎热榜.csv')
        print('文件存在')
    else:
        print('文件不存在，则创建')
    with open('./知乎热榜.csv', 'a', newline='', encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(list2)
    list1=['','?list=zvideo']
    # list1 = ['', '?list=zvideo', '?list=science', '?list=digital', '?list=sport', '?list=fashion', '?list=car','?list=film', '?list=school', '?list=depth', '?list=focus']
    # 全站,视频，科学，数码，体育，时尚，汽车，校园，影视，汽车，国际
    for i in list1:
        url='https://www.zhihu.com/hot'+i
        # print(url)
        response=requests.get(url,headers=headers).text
        get_parse(response)
        time.sleep(10)


main()
wb = Workbook()
ws = wb.active
if os.path.exists('知乎热榜.xlsx'):
    os.remove('知乎热榜.xlsx')
with open('知乎热榜.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('知乎热榜.xlsx')