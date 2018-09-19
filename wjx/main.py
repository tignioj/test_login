import sys
import requests
import time
import datetime
from random import randint
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import random


#分析前端，抓包构造随机题目
def return_random_data():
    s1_s5 = "1$"+str(random.randint(1,2))+"}2$"+str(random.randint(1,13))+"}3$"+str(random.randint(1,2))+"}4$"+str(random.randint(1,3))+"|"+str(random.randint(4,6))+"|"+str(random.randint(6,8))+"}5$"+str(random.randint(1,3))+"|"+str(random.randint(4,6))+"|"+str(random.randint(7,8))+"}"  #1-5
    s6_s8_a = "6$1}7$"+str(random.randint(1,3))+"}"
    s6_s8_bc = "6$"+str(random.randint(1,2))+"}7$1}"

    s8_enda = "8$1}9$"+str(random.randint(1,2))+"|"+str(random.randint(3,4))+"|"+str(random.randint(5,6))+"}10$1}11$-3}12$"+str(random.randint(1,3))+"|"+str(random.randint(4,6))+"|"+str(random.randint(6,9))
    s8_endb = "8$2}9$-3}10$-3}11$"+str(random.randint(1,3))+"|"+str(random.randint(4,6))+"|"+str(random.randint(6,8))+"}12$"+str(random.randint(1,3))+"|"+str(random.randint(4,6))+"|"+str(random.randint(6,9)) 

    submitdata1 = s1_s5 + s6_s8_a + s8_enda
    submitdata2 = s1_s5 + s6_s8_a + s8_endb
    submitdata3 = s1_s5 + s6_s8_bc + s8_enda
    submitdata4 = s1_s5 + s6_s8_bc + s8_endb

    datalist = [
        submitdata1,
        submitdata2,
        submitdata3,
        submitdata4
    ]
    data = random.choice(datalist)
    return data
    

def post_wjx():
    #需要需改的参数
    #1, curlID, 
    #2,CookitText, 
    #3, return_random_data()函数里面的返回的数据
    curID ='28322262'
    #submitdata = "1$1}2$2}3$1}4$6|4|1|2}5$2|3|4|6}6$1}7$1}8$1}9$1|2|3|6}10$1}11$-3}12$2|4|5|7"
    submitdata ={
        "submitdata": return_random_data()
    }
    s = (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S") #后退一分钟，wjx禁止填写问卷时间过短
    ss = s[:5] + s[6:] #去掉月份开头的0
    postURL = 'https://www.wjx.cn/joinnew/processjq.ashx' #提交的地址
    myurl = "https://www.wjx.cn/jq/"+curID+".aspx"
    
    getrnnum = requests.get(url=myurl, verify=False)
    rn = re.findall(r'rndnum="(\d+\.?\d+)"', getrnnum.text)
    #jacnumber = getrnnum.headers['Set-Cookie'] 
    FormData = {
        'submittype': '1',
        'curID' : curID,
        't' : str(int(time.time()*1000)),
        'starttime' : ss,#时间可以抓包从js脚本中获取，也可以用python生成
        'rn' : rn[0],#抓js
        'hlv' : '1'
    }
    timep = str(int(time.time()))
    #这个是关键，先电脑提交一次然后Fidder抓包https://www.wjx.cn/joinnew/processjq.ashx这个网址的提交的Cookie并且复制下来,把后面的十个数字去掉,由timep时间戳生成
    CookieText = ".ASPXANONYMOUS=WhK2mOR-1AEkAAAAMWJhMTRkYjgtNGVhZi00MjFhLWI0Y2EtZWJkM2MwYjJhNGQx_eFPY6euw-J0VHZr_xzmWY6lDCg1; UM_distinctid=165bef95dfd0-03944b23e5f2ce-5e442e19-240000-165bef95dfe317; WjxUser=UserName=13226304166&Type=1; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; mobileuser=13226304166; lllogcook=1; ASP.NET_SessionId=fkb3ul0is1zb1xw4pqapo3gm; _uab_collina=153730750060808047678333; _umdata=70CF403AFFD707DF0147BF6DF251CE6A72CFF14886A9A2C93E624F087F5F7EE6D236ADC55EC37436CD43AD3E795C914C9C19E3353392B3031423EB3C0A6C0FB8; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1537152332,1537280167,1537299011,1537327041; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1537368287933; SojumpSurvey=0102FB9A51AB4F1ED608FEFB3A6332711ED608001A4B623A67287537626500340078007200760071006D0062006F0065006B00670061007A007700700065006F006E0066007000610000012F00FF003E8FC3B40C88C5BDBF67BF3030D531F514CD0E; LastActivityJoin=28322262,101891400865; CNZZDATA4478442=cnzz_eid%3D580220188-1536504531-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1537371969; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=" + timep

    headers = {
        "Host": "www.wjx.cn",
        "Connection": "keep-alive",
        "Content-Length": "156",
        "Origin": "https://www.wjx.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Referer": "https://www.wjx.cn/jq/"+curID+".aspx",
        #随机ip绕过wjx验证码机制（同一ip短时间内提交多次需要验证码）
        'X-Forwarded-For' : str(randint(1,255)) + '.' + str(randint(1,255)) + '.' + str(randint(1,255)) + '.' + str(randint(1,255)), 
        "Cookie": CookieText
    }


    r = requests.post(url=postURL, headers=headers, data=submitdata, params=FormData,verify=False)
    print(r.text)



times=1
while(times <= int(sys.argv[1])):
    post_wjx() 
    times+=1
