
# 1在这里我们就利用了 execute_script() 方法将进度条下拉到最底部，然后弹出 alert 提示框。
# 所以说有了这个，基本上 API 没有提供的所有的功能都可以用执行 JavaScript 的方式来实现了。
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get('https://zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

#2获取节点信息   该属性page_source可以获取网页的源代码
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
#获取节点的属性
print(logo.get_attribute('class'))
input = browser.find_element_by_id('zu-top-add-question')
#该节点的文本
print(input.text)
#该节点的id
print(input.id)
#该节点的坐标
print(input.location)

print(input.tag_name)
#该节点的大小
print(input.size)
