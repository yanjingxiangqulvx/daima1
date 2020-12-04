import requests
import json
import re

list = []
urls = ['https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?tdsourcetag=s_pctim_aiomsg'.format(str(i)) for i in range(80,82)]
for i in urls:
    res = requests.get(i).text
    res = re.findall(r'"mainImg":"(.*?)",', res)
    for j in res:
        if len(j) == 0:
            continue
        list.append(j.replace('\\', ''))
        print(j.replace('\\', ''))


print(list)


# img下载本地
for i in list:
    img_xz = requests.get(i)
    with open(r'C:/Users/asus/Desktop/img/' + i.split('/')[-1], 'wb')as f:
        f.write(img_xz.content)
        print('下载完成')