# -*- coding: UTF-8 -*-

#1.获取整个页面的数据
import re        #包含正则表达式
import urllib.request    #引入相关模块，Urlllib 模块提供了读取web数据页面的接口，我们可以像读取本地的文件一样读取www和ftp上的数据
'''
定义函数
'''
def getHtml(url):
    page = urllib.request.urlopen(url) #这个方法打开一个URL地址
    html = page.read()         #read()方法用于读取URL上面的数据
    return html
#2.筛选想要的数据
def getImg(html):
    pattern = re.compile(r'src="https://static.pexels.com/photos/(\d+)/(.*?)\?h=350&auto=compress&cs=tinysrgb"', re.S)
    imglist = re.findall(pattern,html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,r'C:\Users\Administrator\Desktop\go\%s.jpg' % x)
        x+=1

url = 'https://static.pexels.com/photos/160699/girl-dandelion-yellow-flowers-160699.jpeg?cs=srgb&dl=beautiful-beauty-dandelion-160699.jpg&fm=jpg'
html = getHtml(url) #getHtml()函数用于传递一个网址并且把这个页面下载下来
getImg(html)

