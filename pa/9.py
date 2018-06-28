# import urllib.request
#
# response = urllib.request.urlopen('http://www.guirend.cn/')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheaders('server'))
# code  返回状态码  404  网页不存在   500 服务器内部错误等
# reason  同父类一样返回错误的原因
# headers  返回 Requests Headers

import urllib.request
import urllib.error
import socket

try:
    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

