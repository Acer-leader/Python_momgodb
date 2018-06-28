# 那么为了防止这种情况的发生，我们就需要设置代理来解决这个问题，
# 在 Requests 中需要用到 proxies 这个参数。
import requests
# proxies = {
#     'http':'http://192.168.0.147',
#     'https':'http://10.10.1.10:1080',
# }
# requests.get('https://www.taobao.com',proxies=proxies)

# proxies = {
#     'https':'http://user:password@10.10.1.10:3128/',
# }
# requests.get('https://www.taobao.com', proxies=proxies)
#
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# print(requests.get('https://www.taobao.com',timeout = 1).status_code)
#
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
