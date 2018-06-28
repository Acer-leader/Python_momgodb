# coding=utf-8
import urllib.request
from lxml import etree
import os



# 打开每个页面并从页面中获取每个图集的url：http://www.mmjpg.com/mm/1245
def load_page(url):
    print ('打开页面' + url)
    headers = {
        "Host": "www.mzitu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
        }
    request = urllib.request(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for link in link_list:
        print (link)
        get_all_image_url(link)


# 打开一个图集的url，获取该图集下的所有图片页面url：http://www.mmjpg.com/mm/1245/1
def get_all_image_url(url):
    headers = {
        "Host": "www.mzitu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.mzitu.com/page/2/",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    request = urllib.Request(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    title = content.xpath('//div[@class="content"]/h2')[0].text
    max = content.xpath('//div[@class="pagenavi"]/a/span')[4].text
    print (max)
    print (title)
    os.makedirs('image/' + title)
    for page in range(1, int(max)):
        url1 = url + '/'
        url2 = url1 + str(page)
        print (url2)
        get_perimage_url(url2, title)


# 从图集中每个图片页面的url中获取图片的地址http://img.mmjpg.com/2018/1245/2.jpg
def get_perimage_url(url,title):
    headers = {
        "Host": "www.mzitu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.mzitu.com/page/2/",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    request = urllib.Request(url, headers=headers)
    response = urllib.urlopen(request)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="main-image"]/p/a/img/@src')
    for link in link_list:
        load_image(link, title)


# 下载图片并保存
def load_image(url, title):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": url,
    }

    print (url)
    request = urllib.Request(url, headers=headers)
    response = urllib.urlopen(request)
    image = response.read()
    filename = url[-6:]
    with open('image/' + title + '/' + filename, 'wb') as f:
        f.write(image)
    print ("已经成功下载 " + filename)


# http://www.mzitu.com/page/2/
def start_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        url1 = url + 'page/' + str(page) + '/'
        print (url1)
        load_page(url1)
    print ('爬取完毕，谢谢使用！本程序由难凉热血倾情提供！！！')


if __name__ == '__main__':
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))
    url = 'http://www.mzitu.com/'
    if not os.path.isdir('image'):
        os.makedirs('image')
    start_spider(url, start_page, end_page)




