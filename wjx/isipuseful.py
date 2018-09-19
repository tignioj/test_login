import sys
import json
import requests
from random import randint
import re
def Is_ip_usful(ip_port):
    myipurl = "http://icanhazip.com/"

    try:
        my_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', ip_port['HTTP'])[0]
        #print(my_ip)
    except:
        my_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', ip_port['HTTPS'])[0]
        #print(my_ip)


    try:
        r = requests.get(url=myipurl, proxies=ip_port, timeout=4)
        #print("state:",r.status_code,"  ipnow:",r.text.replace('\n', ''), "    proxyip:",ip_port)
        ipnow = r.text.replace('\n', '')
        if(my_ip == ipnow):
            print("ipnow",ipnow, "my_ip",my_ip)
            with open('./usefulip_port.txt', 'a+', encoding = "utf-8") as f:
                f.write(ip_port)
        else:
            print("Not equal:", ip_port, "my_ip", ipnow)
    #except ZeroDivisionError as e:
    except:
        print("useless:", ip_port)


with open('./allip_list.txt', 'r', encoding="utf-8") as f:
    #line_nu=0
    for line in f.readlines():
        #if line_nu<10:#读取前五行   
            #line_nu+=1
            try:
                jsonip = json.loads(line)
                #print("to_json:",line.replace('\n',''),jsonip)
                Is_ip_usful(jsonip)
            except:
                print("except:",line)
        #else:
            #print("break???")
            #break
            
