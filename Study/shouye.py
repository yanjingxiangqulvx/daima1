import requests

url = 'https://www.iqiyi.com/'
# param = {"wd":"爱奇艺"}

headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.42 Safari/537.36"
}

response = requests.get(url, headers = headers)
print(response.text)


