#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://jwsys.gdpu.edu.cn/xtgl/login_slogin.html")

# 点登录按钮，输入账号密码后登录
driver.find_element_by_id('yhm').send_keys("1700502163") #account
driver.find_element_by_id('mm').send_keys("88888888.")  #password
#driver.find_element_by_xpath('//*[@id="account_login"]/form/div/div[5]/button').click()
driver.find_element_by_id('dl').click()
time.sleep(1)
cookie_list = driver.get_cookies()
cookie_dict = {i["name"]:i["value"] for i in cookie_list}
print(cookie_dict)
driver.find_element_by_xpath("//nav[@id='cdNav']/ul/li[3]").click()
driver.execute_script("clickMenu('N253512','/xsxk/zzxkyzb_cxZzxkYzbIndex.html','自主选课','null')")
handles = driver.window_handles
driver.switch_to_window(handles[1])
#driver.execute_script("chooseCourseZzxk('74EF2DD7C8E31847E0530100007F17F1','G9001031','1')")
driver.execute_script("alert('嘿嘿')")
