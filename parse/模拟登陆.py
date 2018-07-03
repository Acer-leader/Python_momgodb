#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/7/3
# Desc  : 模拟登陆百度爬取信息
from urllib import request
import urllib
from urllib import parse
from http import cookiejar
import re
URL_BAIDU_INDEX = u'http://www.baidu.com/'
URL_BAIDU_LOGIN = 'https://passport.baidu.com/v2/api/?login'
# 设置用户名、密码
username = '**********'
password = '*************'
# 设置cookie，这里cookiejar可自动管理，无需手动指定
cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
reqReturn = request.urlopen(URL_BAIDU_INDEX)

# 构造登录请求参数，该请求数据是通过抓包获得，对应[url=https://passport.baidu.com/v2/api/?login]https://passport.baidu.com/v2/api/?login[/url]请求
postData = {
    'username': '',
    'password': '',
}
postData = urllib.parse.urlencode(postData).encode('utf-8')
print(postData)
# 发送登录请求
loginRequest = request.Request(URL_BAIDU_LOGIN, postData)
print(loginRequest)
sendPost = request.urlopen(loginRequest)
print(sendPost)
# 查看贴吧个人主页 ，测试是否登陆成功
teibaUrl = 'http://tieba.baidu.com/home/main?un=%E5%BB%B6%E9%BE%99%E9%97%AE%E9%9B%A8&ie=utf-8&fr=pb&ie=utf-8'
content = request.urlopen(teibaUrl).read()
content = content.decode('utf-8')
# print (content)
# 正则表达式
zz = r'<div class="userinfo_userdata">(.+?)</div>'

# 匹配所有符合规则的内容存到content集合里面
html_other = re.findall(zz, content, re.S)  # re.S表示.可以代表\n
# print(html_other)
pat = re.compile(r'<.+?>')
html_other = pat.sub(",", str(html_other).strip('[\']'))
html = html_other.split(",")
for i in html:
    print(i)