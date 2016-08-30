import requests
proxies = {
    "http": "http://192.168.31.1:3128",
    "https": "http://10.10.1.10:1080",
}
DOWNLOAD_URL = "https://movie.douban.com/top250"


def download_page(url):
    data = requests.get(url).content
    return data


def main():
    print(download_page(DOWNLOAD_URL))


if __name__ == '__main__':
    main()
