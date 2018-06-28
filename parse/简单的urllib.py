# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
#from urllib import request
#from urllib import parse
#response = urllib.request.urlopen("https://www.52pojie.cn/forum.php?mod=guide&view=newthread")
#print(response.read())

'''
post 传输方式
'''

# values = {"username":"617034221@qq.com","password":"123456"}
# data = urllib.parse.urlencode(values).encode('utf-8')
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# response = urllib.request.urlopen(url,data)
# print(response.read().decode())

'''
Get 传输方式
'''
values = {}
values['name'] = '617034221@qq.com'
values['password'] = '1234560'
data = urllib.parse.urlencode(values).encode('utf-8')
url = "http://www.guirend.cn/"
response = urllib.request.urlopen(url)
print(response.read().decode())