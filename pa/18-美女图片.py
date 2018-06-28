# coding=utf-8
import urllib
import requests
from lxml import etree
import os


# 打开每个页面并从页面中获取每个图集的url：http://www.mmjpg.com/mm/1245
def load_page(url):
    print ('正在下载')
    headers = {
        'Host': 'www.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'http://www.mmjpg.com',
    }
    request = requests(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()

    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="pic"]/ul/li/a/@href')
    for link in link_list:
        print (link)
        get_all_image_url(link)


# 打开一个图集的url，获取该图集下的所有图片页面url：http://www.mmjpg.com/mm/1245/1
def get_all_image_url(url):
    headers = {
        'Host': 'www.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'http://www.mmjpg.com',
    }
    request = requests(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    title = content.xpath('//div[@class="article"]/h2')[0].text
    os.makedirs('imagee/' + title)
    for page in range(1, 42):
        url1 = url + '/'
        url2 = url1 + str(page)
        print (url2)
        get_perimage_url(url2, title)


# 从图集中每个图片页面的url中获取图片的地址http://img.mmjpg.com/2018/1245/2.jpg
def get_perimage_url(url, title):
    headers = {
        'Host': 'www.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': 'http://www.mmjpg.com',
    }
    request = requests(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="content"]//img/@src')
    for link in link_list:
        load_image(link, title)


# 下载图片并保存
def load_image(url, title):
    headers = {
        'Host': 'img.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': url,
    }
    print ('正在下载的图片')
    print (url)
    request = requests(url, headers=headers)
    response = urllib.urlopen(request)
    image = response.read()
    filename = url[-6:]
    with open('imagee/' + title + '/' + filename, 'wb') as f:
        f.write(image)
    print ("已经成功下载 " + filename)


def start_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        if page == 1:
            load_page(url)
        else:
            url = url + 'home/' + str(page)
            print (url)
            load_page(url)
    print ('爬取完毕，谢谢使用！本程序由难凉热血倾情提供！！！')


if __name__ == '__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))
    url = 'http://www.mmjpg.com/mm/1319/'
    os.makedirs('imagee')
    start_spider(url, start_page, end_page)
