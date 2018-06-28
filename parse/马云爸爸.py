from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 15
def get_page(page):
    params = {
        'type':'uid',
        'value':'2145291155',
        'containerid': '1076032145291155',
        'page':page
    }
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


def save_mongo(result):
    if collection.insert(result):
        print('Save to Mongodb success')

if __name__ == '__main__':
        for page in range(1,max_page+1):
            math = get_page(page)
            results = parse_page(*math)
            for result in results:
                print(result)
                save_mongo(result)
