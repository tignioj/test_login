import sys
import requests
import time
import datetime
from random import randint
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def return_random_data():
    data = "1$1}2$1}3$2}4$3}5$1}6$2}7$1|2|4}8$2|3|4|5|6|7|8|10|11}9$4}10$3}11$2}12$2}13$1}14$4}15$4|6|7"
    return data


def post_wjx(times):
    times = int(times)
    submitdata = {
        "submitdata": return_random_data()
    }
    # 后退一分钟，wjx禁止填写问卷时间过短
    s = (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S")
    postURL = 'https://www.wjx.cn/joinnew/processjq.ashx'  # 提交的地址
    subject_addr = "https://www.wjx.cn/jq/"+curID+".aspx"
    get_subject_headers = {
        "Host": "www.wjx.cn",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8"
    }

    r1 = requests.get(url=subject_addr, headers=get_subject_headers, verify=False)
    
    rn = re.findall(r'rndnum="(\d+\.?\d+)"', r1.text)
    # 从网页上拿到cookie
    setCookie = r1.headers['Set-Cookie']
    getCookie = re.findall(r'acw_tc=.*?;', setCookie)[0] + re.findall(r'\.ASP.*?;', setCookie)[0] + re.findall(r'jac.*?;', setCookie)[0]

    CookieText = getCookie

    for i in range(times):
        FormData = {
            'submittype': '1',
            'curID': curID,
            't': str(int(time.time()*1000)),
            'starttime': s,
            'rn': rn[0],   # 抓js
            'hlv': '1'
        }

        random_ip = str(randint(1, 255)) + '.' + str(randint(1, 255)) + '.' + str(randint(1, 255)) + '.' + str(randint(1, 255))

        headers = {
            "Host": "www.wjx.cn",
            "Connection": "keep-alive",
            "Content-Length": "156",
            "Origin": "https://www.wjx.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en, zh-CN;q=0.9, zh;q=0.8",
            "Referer": subject_addr,
            'X-Forwarded-For': random_ip,
            "Cookie": CookieText
        }

        try:
            r = requests.post(url=postURL, headers=headers, data=submitdata, params=FormData, verify=False, timeout=5)
        except requests.exceptions.Timeout as e:
            print("Request timeout error, Please checkout your Internet.", r, e)
            break

        if(re.findall(r'complete', r.text)):
            print("success:%-3d, %-15s, %s" % (i+1, random_ip, r.text))
        else:
            print("没有提交成功，如果网页有验证码，请删掉原答卷，复制一份新的答卷后再重试,网页返回:", r.text)
            break


if __name__ == '__main__':
    print(r"""
    @name         问卷星Brute force (无需selenium) 
    @param {str} curID  问卷ID
    @param {str} data   return_random_data()中的data数据
    @param {int} times  提交次数
    @description   用于问卷星快速提交答案（无验证码版, 非随机, 需要手动构建答案）
    """)
    curID = input('输入问卷ID:')
    times = input('输入提交次数:')
    post_wjx(times)