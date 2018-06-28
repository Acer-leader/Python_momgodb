# <div class="pgc-img"><img src="http://p3.pstatp.com/large/pgc-image/1527666308911b24b3f37af" img_width="750" img_height="1089" alt="「成都街拍」肤白貌美大长腿……成都街头的小姐姐们也太好看了吧！" inline="0">
# <p class="pgc-img-caption"></p></div>
import requests
from urllib.parse import urlencode
from multiprocessing.pool import Pool
import os
from hashlib import md5

GROUP_START =1
GROUP_END = 2
#分析url   构造url   变化的参数只有一个 就是 offset
def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload': 'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            #print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            #print(image_list)
            if image_list:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title':title
                    }
#创建文件夹
# item 就是刚才get_images() 方法返回的一个字典，在方法中我们首先根据 item 的 title 来创建文件夹，
# 然后请求这个图片链接，
# 获取图片的二进制数据，以二进制的形式写入文件，图片的名称可以使用其内容的 MD5 值，这样可以去除重复。
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list','large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main,groups)
    pool.close()
    pool.join()

