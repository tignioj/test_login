import sys
import requests
from time import time, strftime
import time
import datetime
import random
from random import randint
import urllib
import urllib.request
import urllib.parse
import zlib
import http.cookiejar
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ipFun():
    s = (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S") #后退一分钟，wjx禁止填写问卷时间过端
    ss = s[:5] + s[6:] #去掉月份开头的0
    postURL = 'https://www.wjx.cn/joinnew/processjq.ashx' #提交的地址
    myurl = "https://www.wjx.cn/jq/27811909.aspx"
    getrnnum = requests.get(url=myurl)
    rn = re.findall(r'rndnum="(\d+\.?\d+)"', getrnnum.text)
    FormData = {
        'submittype': '1',
        'curID' : '27811909',
        't' : str(int(time.time()*1000)),
        'starttime' : ss,#时间可以抓包从js脚本中获取，也可以用python生成，注意格式要正确
        'rn' : rn[0],#抓js
        'hlv' : '1'
    }
    timep = str(int(time.time()))
    CookieText = "UM_distinctid=164f49d1088f6-01e27f86e58d47-5e442e19-1fa400-164f49d108c951; WjxUser=UserName=13226304166&Type=1; _uab_collina=153509377854743253685308; actidev_26890172=1; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a73; .ASPXANONYMOUS=4QzPX4Z81AEkAAAAYjIwODk4ZWMtMjZlNC00NWNkLThkZmEtNjNmNWUzZGM1Yzk4-0B8YnDtcJaGY6Cq2kXJ0wPSGn01; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1535520572,1535608455,1535717060,1536246967; mobileuser=13226304166; SojumpSurvey=0102150296AE0B14D608FE15A2A7352D14D608011A4B623A67287537626500340078007200760071006D0062006F0065006B00670061007A007700700065006F006E0066007000610000012F00FFAA57D9F47E337275622DDA0E843CF04E1538D108; lllogcook=1; LastCheckUpdateDate=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1536246973316; ASP.NET_SessionId=d3vj5xzafkt55gm1nucgqfko; _umdata=E2AE90FA4E0E42DE20BE6166767D345BEBADB47067ED799C30AB60EBBBEDB1F4AC423B94F08E3504CD43AD3E795C914C3D58A2C5D7AEBF9B0C017E83D54B9908; CNZZDATA4478442=cnzz_eid%3D1911695664-1533107192-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1536248544; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=" + timep
    FormData = urllib.parse.urlencode(FormData).encode("utf-8")
    data = {
         #"submitdata" : "1$"+ str(random.randint(1,4))+  "}2$" + str(random.randint(1,2))+"}3$"+str(random.randint(1,3))+"}4$"+ str(random.randint(1,4)) +  "}5$" + str(random.randint(1,3))+ "}6$1|2|"+str(random.randint(3,5))+"}7$" #抓提交页面
         "submitdata" : "1$"+ str(random.randint(1,2)) +"}2$"+ str(random.randint(1,2))+"}3$"+ str(random.randint(1,2))+"}4$"+ str(random.randint(1,3))+"}5$" + str(random.randint(1,5))+"}6$" + str(random.randint(1,5))+"}7$1|2|"+ str(random.randint(3,5))+"}8$1|" + str(random.randint(2,4))+"}9$" + str(random.randint(1,3))+"}10$" + str(random.randint(1,2))+"}11$" + str(random.randint(1,2))+"}12$1}13$"
    }
    data = urllib.parse.urlencode(data).encode('utf-8') #转换成bites
    headers = {
        'Host':'www.wjx.cn',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wjx.cn',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        #'X-Forwarded-For' : str(MY_IP),
        'X-Forwarded-For' : str(randint(1,255)) + '.' + str(randint(1,255)) + '.' + str(randint(1,255)) + '.' + str(randint(1,255)), #随机ip绕过wjx验证吗机制（同一ip短时间内提交多次需要验证码）
        'Referer':'https://www.wjx.cn/jq/27811909.aspx', #问卷地址
        'Accept-Language': 'en,zh-CN,zh;q=0.9;q=0.8',
        'Content-length':'68',
        'scheme':'https',
        'Cookie':CookieText
    }
    r = requests.post(url=postURL, headers=headers, data=data, params=FormData,verify=False)
    print(r.text)



times=1
while(times < int(sys.argv[1])):
    ipFun() 
    times+=1
