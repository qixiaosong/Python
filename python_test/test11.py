from bs4 import BeautifulSoup
import requests

url = 'https://www.douban.com'
r = requests.get(url)
#soup = BeautifulSoup(web_data.text, 'lxml')
print(r.status_code, r.encoding)
print(r.headers['Content-Type'])
