import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
print('---------------------------------')
r = requests.get('https://github.com/favicon.ico')
with open('git_hub.jpg','wb') as  f:
    f.write(r.content)
print(r.text)
print(r.content)

#模拟上传
files = {'file': open('git_hub.jpg','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)