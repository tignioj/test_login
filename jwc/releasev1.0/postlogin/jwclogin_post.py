import requests
from bs4 import BeautifulSoup
import os
import urllib
class gdpujwc(object):
    def __init__(self, su, sp):
        self.session = requests.session()
        self.rootURL = "http://10.50.17.10"
        self.su = su
        self.sp = sp
    
    def get_view(self):
        getURL = self.rootURL + "/default3.aspx"
        self.r1 = self.session.get(getURL)
        soup = BeautifulSoup(self.r1.text, 'lxml')
        self.VIEWSTATE = soup.select("input[name='__VIEWSTATE']")[0].attrs['value']
        print(self.VIEWSTATE)
        self.CookieText = self.r1.headers['Set-Cookie']

    def get_code(self):
        getURL = self.rootURL + "/CheckCode.aspx"
        headers = {
            "Host": "10.50.17.10",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "Referer": "http://10.50.17.10/default3.aspx",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": self.CookieText
        }
        self.r2 = self.session.get(getURL, headers=headers)
        with open('code.png', 'wb') as f:
            f.write(self.r2.content)

    def login(self):
        #su = input('Input Username: ')
        #sp = input('Input Password: ')
        code = input('Input code: ')
        postURL = self.rootURL + "/default3.aspx"
        headers = {
            "Host": "10.50.17.10",
            "Connection": "keep-alive",
            "Content-Length": "390",
            "Cache-Control": "max-age=0",
            "Origin": "http://10.50.17.10",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://10.50.17.10/default3.aspx",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cookie": self.CookieText
        }
        
        data = {
            "__VIEWSTATE": self.VIEWSTATE,
            "tbYHM": self.su,
            "tbPSW": self.sp,
            "TextBox3": code,
            "RadioButtonList1" : "学生",
            "imgDL.x": "151",
            "imgDL.y": "5"
        }
        
        #data = r"__VIEWSTATE=dDw1NjkwNTA3NjQ7dDw7bDxpPDE%2BOz47bDx0PDtsPGk8Mz47aTwxND47aTwxNz47PjtsPHQ8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Oz47dDxwPDtwPGw8b25jbGljazs%2BO2w8d2luZG93LmNsb3NlKClcOzs%2BPj47Oz47dDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs7Pjs%2BPjs%2BPjtsPGltZ0RMOz4%2By6kA4C28m4Zv%2B8qNY7Y%2FILehplc%3D&tbYHM=1700502163&tbPSW=1700502163&RadioButtonList1=%D1%A7%C9%FA&imgDL.x=75&imgDL.y=11" + "&TextBox3={}".format(code)
        data=urllib.parse.urlencode(data).encode("utf-8")
        self.r3 = self.session.post(url=postURL, headers=headers, data=data)
        print(self.r3.text)
        with open('r3.html', 'w', encoding='utf-8') as f:
            f.write(self.r3.text)

    def print_page(self):
        headers = {
            "Host": "10.50.17.10",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://10.50.17.10/xsmainfs.aspx?xh=1700502163",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cookie": self.CookieText
        }
        getURL = self.rootURL + "/xstop.aspx"
        self.r4 = self.session.get(url=getURL, headers=headers)
        print(self.r4.text)
        with open('r4.html', 'w', encoding='utf-8') as f:
            f.write(self.r4.text.strip())

    def print_score(self):
        headers = {
            "Host": "10.50.17.10",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Referer": "http://10.50.17.10/xsleft.aspx?flag=xxcx",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cookie": self.CookieText
        }
        FormData = {
            "xh": self.su
        }
        FormData = urllib.parse.urlencode(FormData).encode("utf-8")
        getURL = self.rootURL + "/xscj.aspx"
        self.r5 = self.session.get(url=getURL, headers=headers, params=FormData)
        print(self.r5.text)
        with open('r5.html', 'w', encoding='utf-8') as f:
            f.write(self.r5.text.strip())

    def main(self):
        self.get_view()
        self.get_code()
        self.login()
        self.print_page()
        self.print_score()




if __name__=='__main__':
    su = "" # account
    sp = "" # password
    jwc = gdpujwc(su, sp)
    jwc.main()
