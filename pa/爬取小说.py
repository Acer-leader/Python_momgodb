import requests
from lxml import etree
from multiprocessing.dummy import Pool
import os
import re

# 小说的章节地址
chapter_url = "https://www.biqudu.com/43_43821/"

# 忽略警告 https请求设置verify=False时 有时候会报错 设置这条语句可以解决
requests.packages.urllib3.disable_warnings()


def get_response(url):
    '''
    ：根据指定URL获取响应数据、
    ：返回xpath选择器格式的数据
    '''
    html = requests.get(url, verify=False)
    return etree.HTML(html.text)


def get_chapter_content(selector):
    '''
    ：传入xpath选择器格式的数据获取想要的数据
    ：返回一个包含章节标题，和章节地址的数组
    '''
    html = []
    # 根据xpath获取title
    title = selector.xpath('//*[@id="list"]/dl/dd/a/text()')
    # 根据xpath获取url
    href = selector.xpath('//*[@id="list"]/dl/dd/a/@href')
    # 这里以12开始遍历是因为前面几个数据是不要的
    for i in range(12, len(title)):
        tit = title[i]
        url = "https://www.biqudu.com" + href[i]
        chapter = {"title": tit, "url": url}
        html.append(chapter)
    return html


def save_content(url):
    '''
    ：根据传进来的URL获取数据并保存
    ：这里的URL传入的事一个字典存储的地址和相对应保存文件的名称
    '''
    # 保存下载文件的文件夹
    folder = 'novel'
    # 获取选择器
    html = get_response(url['url'])
    # 提取出想要的内容
    con = html.xpath('//*[@id="content"]/text()')
    # 判断文件夹是否存在 不存在就创建
    if not os.path.exists(folder):
        os.mkdir(folder)
    # 去掉非法字符
    fileName = re.sub('[\/:*?"<>|]', '-', url['name'])
    # 保存文件
    with open(folder + "/" + fileName + ".txt", "w+", encoding="utf-8") as f:
        # 得到的是一个list 这里转换为str
        content = ''.join(con)
        # 遍历字符串 保存为每行不好过50个字符
        for i in range(0, len(content), 50):
            f.write(content[i:i + 50] + "\n")


def get_content(html):
    '''
    ：并行爬取保存数据
    '''
    urls = []

    for con in html:
        url = con['url']
        name = con['title']
        urls.append({'name': name, 'url': url})
    # 线程个数
    pool = Pool(4)
    # 使用map进行并行爬取，save_content为爬取保存函数，
    # urls为一个list,里面存储的为网址列表和对应的保存名字
    pool.map(save_content, urls)
    pool.close()
    pool.join()


def main():
    selector = get_response(chapter_url)

    html = get_chapter_content(selector)

    get_content(html)


if __name__ == '__main__':
    main()