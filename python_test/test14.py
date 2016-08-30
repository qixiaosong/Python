import requests
proxies = {
    "http": "http://192.168.31.1:3128",
    "https": "http://10.10.1.10:1080",
}
r = requests.get('https://www.baidu.com')
'''
print(r.encoding)
print(r.headers)
print(r.cookies)
print(r.text)
'''