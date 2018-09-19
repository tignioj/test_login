import sys
import random

with open('./proxyip2.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        print(line, type(line))

