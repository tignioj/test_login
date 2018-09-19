
import random
import requests
import re
import time
myurl = "https://www.wjx.cn/jq/28229263.aspx"
timep = str(int(time.time()))
headers = {
    "Host": "www.wjx.cn",
    "Connection": "keep-alive",
    "Content-Length": "145",
    "Origin": "https://www.wjx.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Referer": "https://www.wjx.cn/jq/28229263.aspx",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Cookie": ".ASPXANONYMOUS=WhK2mOR-1AEkAAAAMWJhMTRkYjgtNGVhZi00MjFhLWI0Y2EtZWJkM2MwYjJhNGQx_eFPY6euw-J0VHZr_xzmWY6lDCg1; UM_distinctid=165bef95dfd0-03944b23e5f2ce-5e442e19-240000-165bef95dfe317; WjxUser=UserName=13226304166&Type=1; spiderregkey=baidu.com%c2%a7%e7%9b%b4%e8%be%be%c2%a71; mobileuser=13226304166; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1537152339885; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1536507338,1536557084,1537152332,1537280167; CNZZDATA4478442=cnzz_eid%3D580220188-1536504531-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1537280104; LastActivityJoin=28229263,101887345747; jac28229263=35719279; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=" + timep
    #1537284348
}

getrnnum = requests.get(url=myurl, headers=headers, verify=False)
rn = re.findall(r'rndnum="(\d+\.?\d+)"', getrnnum.text)