from wxpy import *
import time
import re
from selenium import webdriver

    

driver = webdriver.Chrome() 

d = []
class autoChoose(object):
    def __init__(self, account, password, cource):
        self.account = account
        self.password = password
        self.cource = cource



    def wxlogin(self):
        self.bot = Bot()
        self.xc = self.bot.mps().search("校查")[0]
        self.bot.enable_puid('wxpy_puid.pkl')
        #self.xc = self.bot.search(puid="f98059b9") #校查puid

        @self.bot.register(self.xc)
        def print_others(msg):
            #print(msg)
            d.append(msg)
            self.saveAnswer(msg)

    def saveAnswer(self,msg):
        title = driver.execute_script("return document.querySelectorAll('.infoList > ul > li> span')[0].innerText")
        chapter = driver.execute_script("return document.querySelectorAll('.infoList > ul > li> span')[1].innerText")
        self.rq = ''
        self.l = []

        #print("====save then find====")
        mystr = msg.raw['Content']
        pat = re.compile(r'\[(.*?)\n参考答案：(.*?)]]')
        q = pat.search(mystr)
        if q is None:
            pat = re.compile(r'\n参考答案：(.*?)]]')
            q = pat.search(mystr)
            l = re.split(r'[╔ \x01]+', q.group(1))
            rq = re.search(r'CDATA(.*)', mystr).group(0)
        else:
            l = re.split(r'[╔ \x01]+', q.group(2))
            pat1 = re.compile(r'CDATA.*\[CDATA\[(.*)')
            rq = pat1.search(q.group(1)).group(1)

        if(len(l) == 0):
            r = re.findall("(.*)\n答案；(.*)", mystr)[0]
            rq = r[0]
            l = re.split(r'[~]+', r[1])
            l.pop() #dele the lasted empty element

        print(">>>Reply:",rq, l)
        with open(title + chapter + '.txt', 'a+', encoding='utf-8') as f:
            f.write("题目:" + rq + '\n' "答案:")
            for i in l:
                f.write(i + " ")
                f.write("\n\n")
        #self.rq = rq
        self.l = l
        self.findAnswer()



    def findAnswer(self):
        print("====findAnswer=====")
        #print("findAnswer:",self.rq, self.l, self.sjnum)
        print("Choosing...:")

        self.sjtc = driver.execute_script("return $('.subject_node')[%d].getElementsByClassName('nodeLab')" % (self.sjnum))
        try:
            for j in self.l:
                i = 0
                while(i < len(self.sjtc)):
                    #print(self.sjtc[i].text.split('\n').pop(1), j)
                    if(self.sjtc[i].text.split('\n').pop(1) == j):
                        self.sjtc[i].click()
                        print("checked:",self.rq,j)
                    i+=1
        except:
            self.xc.send_msg(self.rq)
        finally:
            self.asjfinish = 1
        if(i >= len(self.sjtc)):
            self.asjfinish = 1


    #Clear all answer
    def cleanCheck(self):
        mycheckjs = """
        var ac = document.getElementsByClassName("examquestions-answer");
        for(var i = 0; i < ac.length; i++) {
            ac[i].previousElementSibling.firstElementChild.checked = false;
        }
        """
        driver.execute_script(mycheckjs)

    def handlefun(self,changeTo):
        handles = driver.window_handles
        #print("handlefun:", handles)
        driver.switch_to_window(handles[changeTo])

    def courseLogin(self):
        zhsLoginUrl = "https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/"
        driver.get(zhsLoginUrl)
        driver.find_element_by_id('lUsername').send_keys(self.account) #account
        driver.find_element_by_id('lPassword').send_keys(self.password)  #password
        driver.execute_script("formSignUp()")
        time.sleep(4)
        driver.execute_script(self.cource)
        #driver.find_element_by_xpath('//*[@id="j-assess-criteria_popup"]/div[9]/div/a').click()
        #driver.find_elements_by_class_name("j-popup-close")
        #1 is video page
        self.handlefun(1)
        time.sleep(3)
        driver.execute_script('document.getElementsByClassName("popbtn_yes")[0].click()')
        driver.execute_script('document.getElementsByClassName("j-popup-close")[1].click()')



    def openCource(self, num):
        self.chooseFinish = 0
        print("========================This is page %s =================================" % (num))
        print("===opencource switch to 2====")
        self.handlefun(2)
        time.sleep(2)
        #single page subject descrube
        self.sj = driver.find_elements_by_class_name("subject_describe")
        self.cleanCheck()
        #self.sj = driver.execute_script("return $('.subject_stem')")
        i = 0
        while(i < len(self.sj)):
            #patsj = re.compile(r'\n(.*)$') 
            #sj_str = patsj.search(self.sj[i].text).group(1) #match subject
            sj_str = self.sj[i].text
            print(sj_str)
            # 保持i一致以便于查找题目对应的选项
            #print("openCource: ", sj_str ,"number: ", i)
            #l, rq清空一次
            self.l = []
            self.rq = ''

            self.sjnum = i
            self.xc.send_msg(sj_str) # 收到答案后再执行findAnswer()
            self.rq = sj_str
            self.asjfinish = 0
            k = 0
            while(self.asjfinish!=1):
                time.sleep(1)
                k+=1
                if(k >= 60):
                    print("Timeout a sjfinish!")
                    return
            i+=1
            if(i >= len(self.sj)):
                self.chooseFinish = 1


    def saveTest(self):
            driver.execute_script("""
            submitAnswer(1);
            document.getElementsByClassName("popbtn_yes")[0].click();
            """)
    
    def loopOpenCourse(self):
        self.tp = driver.find_elements_by_class_name("name") 
        time.sleep(4)
        i = 0
        while(i < len(self.tp)):
        #while(i<= 0):
            self.tp[i].click()
            time.sleep(3)
            self.openCource(i)
            time.sleep(5)
            self.saveTest()
            #driver.close()
            k = 0
            while(self.chooseFinish != 1):
                time.sleep(2)
                k+=1
                if(k>60):
                    print("Timeout page submit!")
                    break
            print("===loopOpenCourse switch to 1====")
            self.handlefun(1)
            i+=1





    def main(self):
        self.wxlogin()
        self.courseLogin()
        self.loopOpenCourse()

        
if __name__=='__main__':
    account = ""
    password = ""
    #cource = "openVideo('2027882','7954','0');"
    cource = ""
    dt = autoChoose(account, password, cource)
    dt.main()