from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")


# 打开随机生成答案的js
with open('somelib/random.js', 'r', encoding='utf-8') as f:
    randomjs = f.read()


class WjxDemo(object):
    def __init__(self, url):
        self.url = url

    def open_questions_page(self):
        # 有窗口模式
        # self.driver = webdriver.Chrome()
        # 无窗口模式
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.url)

    def get_info(self):
        jsdict = r'''
        {
            'cookie': document.cookie,
            'html': document.documentElement.outerHTML
        }
        '''
        s = 'return ' + jsdict
        web_info = self.driver.execute_script(s.replace('\n', ''))
        return web_info

    def get_answer(self, times):
        answer_arr = []
        for i in range(times):
            answer_arr.append(self.driver.execute_script(randomjs + 'return sent_to_answer();'))
        return answer_arr
