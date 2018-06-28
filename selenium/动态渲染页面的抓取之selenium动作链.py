# < !doctype
# html >
# < html
# lang = "en" >
# < head >
# < meta
# charset = "utf-8" >
# < title > 可放置小部件（Droppable
# Widget）演示 < / title >
# < link
# rel = "stylesheet"
# href = "//apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css" >
# < style >
# # draggable {
# width: 100
# px;
# height: 100
# px;
# background:  # ccc;
# }
# # droppable {
# position: absolute;
# left: 250
# px;
# top: 0;
# width: 125
# px;
# height: 125
# px;
# background:  # 999;
# color:  # fff;
# padding: 10
# px;
# }
# < / style >
#     < script
# src = "//apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js" > < / script >
#                                                                 < script
# src = "//apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js" > < / script >
#                                                                      < / head >
#                                                                          < body >
#                                                                          < div
# id = "droppable" > 请放置到这里！ < / div >
#                                < div
# id = "draggable" > 请拖拽我！ < / div >
#
#                              < script >
# $("#draggable").draggable();
# $("#droppable").droppable({
# drop: function()
# {
#     alert("dropped");
# }
# });
# < / script >
#     < / body >
#        < / html >
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'

browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()