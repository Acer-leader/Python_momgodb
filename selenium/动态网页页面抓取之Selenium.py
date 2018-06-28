from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
# def bai_du(keyword):
#     try:
#         browser.get('https://www.baidu.com')
#         input = browser.find_element_by_id('kw')
#         input.send_keys(keyword)
#         input.send_keys(Keys.ENTER)
#         wait = WebDriverWait(browser, 10)
#         wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#         print(browser.current_url)
#         print(browser.get_cookies())
#         print(browser.page_source)
#     finally:
#         browser.close()
#
# <div class="search-combobox-input-wrap">
# <input id="q" name="q" aria-label="请输入搜索文字" accesskey="s" autofocus="autofocus" autocomplete="off" class="search-combobox-input" aria-haspopup="true" aria-combobox="list" role="combobox" x-webkit-grammar="builtin:translate" tabindex="0">
# </div>
import time
def tao_bao(keyword,key):
        browser.get('https://www.taobao.com')
        input_first = browser.find_element_by_id('q')
        def next_bao(key):
            input_first = browser.find_element_by_id('q')
            input_first.send_keys(key)
        next_bao(key)
       #input_first.send_keys(Keys.ENTER)
        time.sleep(2)
        input_first.clear()
        input_first.send_keys(keyword)
        button = browser.find_element_by_class_name('btn-search')
        button.click()
        # input_second = browser.find_element_by_css_selector('#q')
        # input_third = browser.find_element_by_xpath('//*[@id="q"]')
        # print(input_first,input_second,input_third)
        #browser.close()
tao_bao('韩红充气娃娃','胡翔是什么人')

