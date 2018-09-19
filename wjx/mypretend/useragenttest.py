import random,requests,time,re
import user_agent
def get_random_header():
    headers={'User-Agent':random.choice(user_agent.list),'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",'Accept-Encoding':'gzip'}
    return headers
get_random_header()