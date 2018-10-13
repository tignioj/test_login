import sys
import requests
import time
import datetime
from random import randint
import urllib3
import re
from somelib import GetWebInfo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class WjxSubmit(object):
    def __init__(self, curID, times):
        self.subject_addr = "https://www.wjx.cn/jq/"+str(curID)+".aspx"
        self.times = int(times)

    # 提交前的准备
    def prepare(self):

        # 新建一个网页对象
        AWjxDemo = GetWebInfo.WjxDemo(self.subject_addr)
        AWjxDemo.open_questions_page()

        self.postURL = 'https://www.wjx.cn/joinnew/processjq.ashx'  # 提交的地址
        web_info = AWjxDemo.get_info()
        html = web_info['html']
        self.Cookie = web_info['cookie']
        self.rn = re.findall(r'rndnum="(\d+\.?\d+)"', html)[0]
        self.answer_list = AWjxDemo.get_answer(self.times)

    def post_start(self):
        for index, answer in enumerate(self.answer_list):
            # 后退一分钟，wjx禁止填写问卷时间过短
            s = (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S")
            submitdata = {
                'submitdata': answer
            }
            FormData = {
                'submittype': '1',
                'curID': curID,
                't': str(int(time.time()*1000)),
                'starttime': s,
                'rn': self.rn,  # 网页上js生成的随机数
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
                "Referer": self.subject_addr,
                'X-Forwarded-For': random_ip,
                "Cookie": self.Cookie
            }

            try:
                r = requests.post(url=self.postURL, headers=headers, data=submitdata, params=FormData, verify=False, timeout=5)
            except requests.exceptions.Timeout as e:
                print("Request timeout error, Please checkout your Internet.", r, e)
                break
            
            if(re.findall(r'complete', r.text)):
                print("success:%-3d, %-15s, %s" % (index+1, random_ip, r.text))
            else:
                print("没有提交成功，如果网页有验证码，请删掉原答卷，复制一份新的答卷后再重试,网页返回:", r.text)
                break

    def main(self):
        try:
            self.prepare()
            self.post_start()

        except:
            print("Error..., Re-prepare now")
            self.prepare()
            time.sleep(2)
            self.post_start()
        
        finally:
            pass


if __name__ == '__main__':
    print(""" 
    @name  问卷星Brute force
    @param curlID  问卷地址
    @param times   提交次数
    @description   用于问卷星快速随机提交答案（无验证码版）
    """)
    # 两个必填参数
    # curID  问卷id
    # times  提交次数
    curID = input('输入问卷ID:')
    times = input('输入提交次数:')
    wjx = WjxSubmit(curID, times)
    wjx.main()