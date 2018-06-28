# 利用 Selenium 抓取淘宝商品并用 PyQuery 解析得到商品的图片、名称、价格、购买人数、
# 店铺名称、店铺所在地信息，并将其保存到MongoDB。  以及数据库，csv格式等

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

KEYWORD = input('请输入要检索的物品：')

def index_page(page):
    """
    抓取索引页
    :param page:页码
    :return:
    """
    print('正在爬取第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input'))
            )

            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        index_page(page)

from pyquery import PyQuery as pq
def get_products():
    """
    提交商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price ').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),
        }
        print(product)
        write_txt(product)
        save_mysql(product)
        save_to_mongo(product)
        save_image(product)

import os
from hashlib import md5
import requests
def save_image(item):
    if not os.path.exists(item.get('shop')):
        os.mkdir(item.get('shop'))
        try:
            local_image_url = item.get('image')
            response = requests.get('http:' + local_image_url)
            file_path = '{0}/{1}.{2}'.format(item.get('shop'),md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
                    print('Success to Save image')
            else:
                print('Already Downloaded', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image')


import pymongo
MONGO_URL = '127.0.0.1'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
def save_to_mongo(result):
    """
    保存到Mongodb 名字淘宝

    :return:结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到Mongodb成功')
    except Exception:
        print('存储到Mongodb失败')

def write_txt(content):
    try:
        with open('tao.csv','a',encoding='utf-8') as f:
            f.write(str(content)+ '\n') #要存到txt，csv 字典格式不能直接写入 转换成json  或者 字符串
            print('写入成功')
    except Exception:
        print('写入失败')

import pymysql
sql_db = pymysql.connect(host = 'localhost',user = 'root',password = 'root123',port = 3306,db = 'tao',charset='utf8')
cursor = sql_db.cursor()
def save_mysql(content):
    table = 'ipad'
    keys = ','.join(content.keys())
    values = ','.join(['%s'] * len(content))
    sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
    try:
        if cursor.execute(sql,tuple(content.values())):
            print('Successful')
            sql_db.commit()
    except:
        print('Failed')
        sql_db.rollback()
    #sql_db.close()


def main():
    """
    遍历每一页
    :return:
    """
    MAX_PAGE = input("MAX_PAGE:")
    MAX_PAGE = int(MAX_PAGE)
    for i in range(1,MAX_PAGE+1):
        index_page(i)
    browser.close()
if __name__ == '__main__':
    main()
