# 在 Chrome 59 版本开始已经开始支持了 Headless 模式，也就是无界面模式，这样爬取的时候就不会弹出浏览器了，
# 如果要使用此模式请把 Chrome 升级到 59 版本及以上，启用 Headless 模式的方式如下：
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# 首先创建一个 ChromeOptions 对象，添加一个 headless 参数，然后在初始化Chrome 对象的时候通过 chrome_options 传递这个 ChromeOptions 对象，这
# 样我们就可以成功启用 Chrome 的 Headless 模式了。
# 这样在运行时浏览器的界面就不会弹出了。

from  selenium import webdriver
from pyquery import PyQuery as pq
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://www.baidu.com/')
html = browser.page_source
print(pq(html))