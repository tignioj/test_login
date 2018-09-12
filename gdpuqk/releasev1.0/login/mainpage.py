import requests
import urllib
#拿到cookie之后用的
CookieText = "JSESSIONID=57BC9986368521AE9B3FA0C2DB267F24"
getURL = "http://jwsys.gdpu.edu.cn/xtgl/index_initMenu.html"


FormData = {
    "jsdm": "",
    "_t": "",
}

FormData = urllib.parse.urlencode(FormData).encode("utf-8")

headers = {
    "Host": "jwsys.gdpu.edu.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Cookie": CookieText
}

r = requests.get(url=getURL, headers=headers, params=FormData)
with open('2.html', 'w', encoding='utf-8') as f:
    f.write(r.text.strip())