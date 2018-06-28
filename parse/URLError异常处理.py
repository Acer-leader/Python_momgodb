import urllib.request
#
# # requset = 'http://www.xxxxx.com'
# # try:
# #     urllib.request.urlopen(requset)
# # except urllib.error.URLError as e:
# #     print (e.reason)
#
# req = 'http://blog.csdn.net/cqcre'
# try:
#     urllib.request.urlopen(req)
# except urllib.request.error.HTTPError as e:
#     print(e.code)
#     print(e.reason)


# import urllib
# from urllib import request
req = urllib.request('http://blog.csdn.net/cqcre')
try:
    urllib.request.urlopen(req)
except urllib.request.error.HTTPError as e:
    if hasattr(e, "reason"):
        print(e.reason)
else:
    print("OK")
