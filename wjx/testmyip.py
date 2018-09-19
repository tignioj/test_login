from bs4 import BeautifulSoup
import requests

url = 'https://ip.cn/'
proxies = {
    'http': '223.145.229.20:6666',
}
r = requests.get(url, proxies=proxies, timeout=5)
print(r.text)