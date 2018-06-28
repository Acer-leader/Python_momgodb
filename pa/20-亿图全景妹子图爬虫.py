# coding=utf-8
import urllib.request
import requests
from lxml import etree
import os


# 打开每个页面并从页面中获取每个图集的url：http://www.yeitu.com/meinv/xinggan/2.html
def load_page(url):
    print ('打开页面' + url)
    headers = {
        "Host": "www.yeitu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
        }
    request = requests.get(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="wf"]/ul/li/a/@href')
    for link in link_list:
        print (link)
        get_all_image_url(link)
# 打开一个图集的url，获取该图集下的所有图片页面url：http://www.yeitu.com/meinv/xinggan/20180326_13960.html
def get_all_image_url(url):
    headers = {
        "Host": "www.yeitu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
    }
    request = requests.get(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    title = content.xpath('//div[@id="title"]/h1')[0].text
    max = content.xpath('//div[@id="pages"]/a')[10].text
    print (max)
    print (title)
    os.makedirs('yituimage/' + title)
    for page in range(2, int(max)):
        url1 = url[0:-5] + '_' + str(page) + '.html'
        print (url1)
        get_perimage_url(url1, title)


# 从图集中每个图片页面的url中获取图片的地址http://img.mmjpg.com/2018/1245/2.jpg
def get_perimage_url(url,title):
    headers = {
        "Host": "www.yeitu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
    }
    request = requests.get(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="img_box"]/a/img/@src')
    for link in link_list:

        link = link[0:-10]
        load_image(link, title)


# 下载图片并保存
def load_image(url, title):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
    }

    print (url)
    request = requests.get(url, headers=headers)
    response = urllib.request.urlopen(request)
    image = response.read()
    filename = url[-6:]
    with open('yituimage/' + title + '/' + filename, 'wb') as f:
        f.write(image)
    print ("已经成功下载 " + filename)


# http://www.yeitu.com/meinv/xinggan/2.html
def start_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        url1 = url + '/meinv/xinggan/20180417_14053' + '_' + str(page) + '.html'
        print (url1)
        load_page(url1)
    print ('爬取完毕，谢谢使用！本程序由难凉热血倾情提供！！！')


if __name__ == '__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))
    url = 'http://www.yeitu.com'
    if not os.path.isdir('yituimage'):
        os.makedirs('yituimage')
    start_spider(url, start_page, end_page)




