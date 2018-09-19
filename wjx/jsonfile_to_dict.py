import sys
import json



with open('./proxyip_json.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        try:
            jsonip = json.loads(line)
            print("to_json:",line.replace('\n',''),jsonip)
        except:
            print("except:",line)

