# -*- coding: UTF-8 -*-

# python读取网页的库

import urllib.request

# 正则表达式有关模块
from bs4 import BeautifulSoup
import re
import os
def getHTML(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
def getImag(html):
    reg = '<img class="BDE_Image".*?"(.*?)"'
    pattern = re.compile(reg)
    html = html.decode('utf-8')
    imags = re.findall(pattern, html)
    t = 1
    for img in imags:
        urllib.request.urlretrieve(img,r'C:\Users\Administrator\Desktop\go\%s.jpg'  % t)
        t += 1
        print(u'开始保存：', '保存成功')
url = 'https://tieba.baidu.com/p/5629017987'
html = getHTML(url)
getImag(html)

