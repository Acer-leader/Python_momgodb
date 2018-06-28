# 有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，
# 那么站点根本不会响应，所以为了完全模拟浏览器的工作，
# 我们需要设置一些Headers 的属性。
#
# 首先，打开我们的浏览器，调试浏览器F12，我用的是Chrome，打开网络监听，示意如下，
# 比如知乎，点登录之后，我们会发现登陆之后界面都变化了，出现一个新的界面，实质上这个页面包含了许许多多的内容，
# 这些内容也不是一次性就加载完成的，实质上是执行了好多次请求，一般是首先请求HTML文件，然后加载JS，CSS 等等，
# 经过多次请求之后，网页的骨架和肌肉全了，整个网页的效果也就出来了。
import urllib.request
# import urllib.parse
#设置Headers
# url = 'http://www.baidu.com/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username':'cqc','password':'123456'}
# headers = {'User-Agent':user_agent}
data = urllib.parse.urlencode(values).encode('utf-8')
# response = urllib.request.urlopen(url,data,headers)
# page = response.read().decode()
# print(page)
#Proxy 代理的设置

# enable_proxy = True
# proxy_handler = urllib.request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#      opener = urllib.request.build_opener(proxy_handler)
# else:
#      opener = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opener(opener)

#Timeout的设置
print('-----------------------------------------------------')
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url,data,timeout=10)
print(response.read().decode())