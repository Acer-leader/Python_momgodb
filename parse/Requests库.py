import requests   #引入库

# Urllib 库的方法为urlopen()而 Requests库是 get()方法

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
# print(requests.post('http://httpbin.org/post'))
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

print('------------------------------------------------')
r = requests.get('http://httpbin.org/get')
data = {
    'name':'wanghui',
    'age':22
}
r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
#得到字典格式  直接调用json 格式
r = requests.get('http://httpbin.org/get')

print(r.json())
print(type(r.json()))