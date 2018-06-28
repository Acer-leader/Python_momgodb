#  <dd>
#                         <i class="board-index board-index-1">1</i>
#     <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
#       <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
#         <p class="star">
#                 主演：张国荣,张丰毅,巩俐
#         </p>
# <p class="releasetime">上映时间：1993-01-01(中国香港)</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>

import requests
import re
import json
import time
from requests.exceptions import RequestException
#获取html文件源码
def get_one_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        }

        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#排名正则
#根据源码得到筛选信息
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name">'
                         + '<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)'
                         + '</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
#把帅选的信息写入文件
def write_to_json(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False,) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)