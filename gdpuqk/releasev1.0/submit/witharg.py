import requests
import time
import urllib
kcmc = '戏剧鉴赏'
kch_id = 'G2901010'
jxb_ids = '74B1CF268C3F3FFBE0530100007F80D4'
su = '1700502133' 
CookieText = "JSESSIONID=BCC6B5D391AC6E32110B77EF6A7404EC"

i=0
while(True):
    data = {
        "jxb_ids":jxb_ids, #
        "kch_id": kch_id, #
        "kcmc": kcmc, #
        "xsbxfs":"0",
        "rwlx":"2",
        "rlkz":"1",
        "rlzlkz":"0",
        "sxbj":"1",
        "xxkbj":"0",
        "qz":"0",
        "cxbj":"0",
        "xkkz_id":"71F3F2CB80672553E0530100007FE95A", #
        "njdm_id":"2017",
        "zyh_id":"0502",
        "kklxdm":"10",
        "xklc":"1",
        "xkxnm":"2018",
        "xkxqm":"3",
    }

    FormData = {
        "gnmkdm": "N253512",
        "su": su  #
    }

    FormData = urllib.parse.urlencode(FormData).encode("utf-8")
    data = urllib.parse.urlencode(data).encode('utf-8') #转换成bites


    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en,zh-CN;q=0.9,zh;q=0.8",
        "Content-Length":"310",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":CookieText,
        "Host":"jwsys.gdpu.edu.cn",
        "Origin":"http://jwsys.gdpu.edu.cn",
        "Proxy-Connection":"keep-alive",
        "Referer":"http://jwsys.gdpu.edu.cn/xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=1700502163",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest"
    }

    postURL = "http://jwsys.gdpu.edu.cn/xsxk/zzxkyzb_xkBcZyZzxkYzb.html"

    
    r = requests.post(url=postURL, headers=headers, data=data, params=FormData, timeout=3)

    print("times:",i,r.json())
    if(r.json()['flag'] == '1' ):
        print("success")
        break
    i+=1


