import requests
import random
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
submitdata = "\'submitdata:\'" + data

r = requests.post(url = 'http://www.baidu.com', data=submitdata)