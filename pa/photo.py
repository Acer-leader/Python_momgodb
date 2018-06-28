# -*- coding: UTF-8 -*-
import re
import os
import requests
import time


def get_url(url):
    kw = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    try:
        r = requests.get(url, headers=kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        print('wrong!!!!!!!!!!!')


def get_photourl(photo_url):
    kw = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
    try:
        r = requests.get(photo_url, headers=kw)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except:
        return 'wrong'


def get_photos(url, new_fpath):
    result = get_url(url)
    pattern = re.compile(r'src="https://images.pexels.com/photos/(\d+)/(.*?)\?h=350&auto=compress&cs=tinysrgb"', re.S)
    # 真正的下载链接是static，不是images开头

    items = re.findall(pattern, result.text)

    for item in items:
        try:
            photo_url = 'https://static.pexels.com/photos/' + str(item[0]) + '/' + str(item[1])
            # 把图片链接中的images，改成了static
            save(photo_url, item, new_fpath)
            time.sleep(1)
        except:
            continue


def makedir(new_fpath, i, key):
    E = os.path.exists(new_fpath)
    if not E:
        os.makedirs(new_fpath)
        os.chdir(new_fpath)
        print('文件夹' + key + '_page' + str(i + 1) + '创建成功！')
    else:
        print('文件夹已存在！')


def save(photo_url, item, new_fpath):
    Final_fpath = new_fpath + '/' + str(item[0]) + str(item[1])

    print('正在下载图片......')

    result = get_photourl(photo_url)
    if result != 'wrong':
        print('下载成功！')
    else:
        print('失败')

    E = os.path.exists(Final_fpath)

    if not E:
        try:
            with open(Final_fpath, 'wb') as f:
                f.write(result.content)
        except:
            print('下载失败！')
    else:
        print('图片已存在')


def main():
    key = input('请输入搜索关键词(英文)：')

    url = 'https://www.pexels.com/search/' + key + '/'

    num = int(input('请输入一共要下载的页数：'))  # 默认从第1页开始下载

    fpath = 'E:/python'
    for i in range(num):
        new_fpath = fpath + '/Photo2.0/' + key + '_page' + str(i + 1)
        makedir(new_fpath, i, key)
        if i >= 1:
            new_url = url + '?page=' + str(i + 1)
            get_photos(new_url, new_fpath)
        else:
            get_photos(url, new_fpath)
        time.sleep(3)


main()