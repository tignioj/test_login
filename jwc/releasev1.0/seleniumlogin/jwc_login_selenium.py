from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()
driver.get("http://10.50.17.10/default3.aspx");

time.sleep(1)
cookie_list = driver.get_cookies()
cookie_dict = {i["name"]:i["value"] for i in cookie_list}
print(cookie_dict)
verification = input("Input verication code: ")
js = 'document.getElementById("tbYHM").value = "1700502163";document.getElementById("tbPSW").value = "1700502163";document.getElementById("TextBox3").value = \'{}\';'.format(verification)
driver.execute_script(js)
driver.execute_script('''
    document.getElementById("imgDL").click();
''')
