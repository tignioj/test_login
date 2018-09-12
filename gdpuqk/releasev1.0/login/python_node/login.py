import requests
from bs4 import BeautifulSoup
import time
import urllib
import os
class gdpuqk(object):
    def __init__(self):
        self.session = requests.session() #登陆用session

    def getcsrftoken_and_cookie(self):
        getURL = "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html"
        self.r1 = self.session.get(getURL)
        soup = BeautifulSoup(self.r1.text, "lxml")
        self.csrftoken = soup.select("#csrftoken")[0].attrs['value']
        self.CookieText = self.r1.headers['Set-Cookie']
        print(self.csrftoken, self.CookieText)

    def getpublickey(self):
        getURL = "http://jwsys.gdpu.edu.cn/xtgl/login_getPublicKey.html?time=1536597159227&_"
        headers = {
            "Host": "jwsys.gdpu.edu.cn",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Referer": "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cookie": self.CookieText
        }
        FormData = {
            "time": str(int(time.time()*1000)),
            "_": str(int(time.time()*1000) -100)
        }
        FormData=urllib.parse.urlencode(FormData).encode("utf-7")
        self.r2 = self.session.get(url=getURL, headers=headers, params=FormData)
        self.exponent = self.r2.json()['exponent']
        self.modulus = self.r2.json()['modulus']
        print(self.exponent, self.modulus)
    
    def getenmm(self):
        mycommand = 'node total.js ' + self.modulus
        self.mm = os.popen(mycommand).read()
        print(self.mm)


    def login(self):
        postURL = "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html"
        headers = {
            "Host": "jwsys.gdpu.edu.cn",
            "Connection": "keep-alive",
            "Content-Length": "460",
            "Cache-Control": "max-age=0",
            "Origin": "http://jwsys.gdpu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cookie": self.CookieText
        }

        data = {
            "csrftoken": self.csrftoken,
            "yhm": "1700502163",
            "mm": self.mm,
            "mm": self.mm
        }
        data=urllib.parse.urlencode(data).encode("utf-8")
        self.r3 = self.session.post(url=postURL, headers=headers, data=data)

        with open('2.html', 'w', encoding='utf-8') as f:
            f.write(self.r3.text.strip())


    def main(self):
        self.getcsrftoken_and_cookie()
        self.getpublickey()
        self.getenmm()
        self.login()


if __name__=='__main__':
    qk = gdpuqk()
    qk.main()

