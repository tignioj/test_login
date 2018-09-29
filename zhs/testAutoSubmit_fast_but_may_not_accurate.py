#coding:utf-8
from wxpy import *
from selenium import webdriver
import time
import re



bot = Bot()
driver = webdriver.Chrome() 

@bot.register()
def print_others(msg):
    if(msg.sender.name == "校查"):
        mystr = str(msg.raw['Content'])
        pat = re.compile(r'参考答案：(.*?)]]')
        r = pat.search(mystr)
        l = re.split(r'[╔ \x01]+', r.group(1))
        if(len(l) == 0):
            mystr = msg.raw['Content']
            print(mystr)
            r = re.findall("答案；.*", mystr)[0]
            l = re.split(r'[~ ；]+', r)
            l.pop()
            l.pop(0)

        saveAnswer(l)

rightAnswer = []

title = ''
chapter = ''
def saveAnswer(l):
    print(l)
    timep = str(int(time.time()))
    global rightAnswer
    print("Starting save...")
    try:
        for i in l:
            rightAnswer.append(i)
            with open('./answer/' + title + chapter +'.txt', 'a+', encoding='utf-8') as f:
                f.write(i + '\n')
        print("finish", timep)
    except:
        print("Fail to save answer!")
    finally:
        print("End saveAnswer()")




class autoChoose(object):
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.xc = bot.mps().search("校查")[0]

    def getChapterInfo(self):
        global title, chapter
        title = driver.execute_script("return document.querySelectorAll('.infoList > ul > li> span')[0].innerText")
        chapter = driver.execute_script("return document.querySelectorAll('.infoList > ul > li> span')[1].innerText")
        



    def find_choose(self):
        driver.implicitly_wait(30)
        self.chooseFinish = 0
        self.handlefun(2)
        time.sleep(1)
        print("===Start find all subject on this page===")
        self.all_choose = driver.find_elements_by_class_name("examquestions-answer")
        j = 0
        while(len(rightAnswer) == 0):
            time.sleep(1)
            j+=1
            if(j>=15):
                break
            
        while(len(self.all_choose)==0):
            print("Empty all_choose")
        self.cleanCheck()
        print("Choosing...")
        for answer in rightAnswer:
            i = 0
            while(i < len(self.all_choose)):
                print(self.all_choose[i].text, answer)
                if(self.all_choose[i].text == answer):
                    print("check", i, answer)
                    self.all_choose[i].click()
                i+=1

            if(i>=len(self.all_choose)):
                self.chooseFinish = 1
                print("Finish choose")
            else:
                print("Choose not finish")
                self.chooseFinish = 0

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
        print("handlefun:", handles)
        driver.switch_to_window(handles[changeTo])

    def loginFun(self):
        zhsLoginUrl = "https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/"
        driver.get(zhsLoginUrl)
        driver.find_element_by_id('lUsername').send_keys(self.account) #account
        driver.find_element_by_id('lPassword').send_keys(self.password)  #password
        driver.execute_script("formSignUp()")
        time.sleep(4)
        driver.execute_script("openVideo('2027843','7926','0')")
        #driver.find_element_by_xpath('//*[@id="j-assess-criteria_popup"]/div[9]/div/a').click()
        #driver.find_elements_by_class_name("j-popup-close")
        #1 is video page
        self.handlefun(1)
        driver.execute_script('document.getElementsByClassName("popbtn_yes")[0].click()')
        driver.execute_script('document.getElementsByClassName("j-popup-close")[1].click()')



    def openCource(self, num):
        print("======This is page %s ========" % (num))
        print("===opencource switch to 2====")
        self.handlefun(2)
        time.sleep(1)
        #single page subject descrube
        self.sj = driver.find_elements_by_class_name("subject_describe")
        i = 0
        while(i < len(self.sj)):
            sj_str = self.sj[i].text
            print(sj_str)
            self.xc.send_msg(sj_str)
            i+=1


    def saveTest(self):
            driver.execute_script("""
            submitAnswer(1);
            document.getElementsByClassName("popbtn_yes")[0].click();
            """)
    
    def loopOpenCourse(self):
        global rightAnswer
        self.tp = driver.find_elements_by_class_name("name") 
        time.sleep(2)
        i = 0
        while(i < len(self.tp)):
            time.sleep(10)
            rightAnswer = []
            self.tp[i].click()
            self.openCource(i)
            self.find_choose()
            time.sleep(3)
            self.saveTest()
            k = 0
            while(self.chooseFinish != 1):
                time.sleep(1)
                k+=1
                if(k>30):
                    break

            print("===loopOpenCourse switch to 1====")
            self.handlefun(1)
            i+=1




    def main(self):
        self.loginFun()
        self.loopOpenCourse()

        

if __name__=='__main__':
    account = ""
    password = ""
    dt = autoChoose(account, password)
    dt.main()