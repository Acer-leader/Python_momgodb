

# Ajax的一方面的
#
# var xmlhttp;
# if (window.XMLHttpRequest) {
#     // code for IE7+, Firefox, Chrome, Opera, Safari
#     xmlhttp=new XMLHttpRequest();
# } else {// code for IE6, IE5
#     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
# }
# xmlhttp.onreadystatechange=function() {
#     if (xmlhttp.readyState==4 && xmlhttp.status==200) {
#         document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
#     }
# }
# xmlhttp.open("POST","/ajax/",true);
# xmlhttp.send();

from urllib.parse import urlencode
import requests
import json
base_url = 'https://m.weibo.cn/api/container/getIndex?'
# 头部信息
# Host: m.weibo.cn
# Referer: https://m.weibo.cn/u/2145291155?uid=2145291155
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
# X-Requested-With: XMLHttpRequest
#
headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
max_page = 15
def get_page(page):
    params = {
        'type':'uid',
        'value':'2145291155',
        'containerid': '1076032145291155',
        'page':page
    }
    # url= https://m.weibo.cn/api/container/getIndex?uid=2145291155&type=uid&ve=2145291155&containerid=1076032145291155&page=3alu
    #构造url
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json(),page
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(math,page:int):
    if math:
        items = math.get('data').get('cards')
        for index,item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


def write_to_file(content):
    with open('a.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

from pyquery import PyQuery as pq

if __name__ == '__main__':
        for page in range(1,max_page+1):
            shu = get_page(page)
            results = parse_page(*shu)
            for result in results:
                print(result)
                write_to_file(result)
