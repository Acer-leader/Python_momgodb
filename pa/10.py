# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result),result)
from urllib.parse import urlencode

params = {
    'name':'wanghui',
    'age' : 27
}
base_url = 'http://www.baidu.com?'
url  = base_url + urlencode(params)
print(url)

#序列化和反序列化

from urllib.parse import parse_qs

query = 'name=wanghui&age=27'

print(parse_qs(query))

from urllib.parse import parse_qsl
print(parse_qsl(query))

from urllib.parse import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)