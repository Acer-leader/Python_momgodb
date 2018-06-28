from lxml import etree

html = etree.parse('./XPath1.py',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
#获取子节点的子节点  //节点/节点   获取节点以下的节点   //节点//节点
html = etree.parse('./XPath1.py', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)
print(result[0])
#获取父节点 知道子节点
html = etree.parse('./XPath1.py', etree.HTMLParser())
result = html.xpath('//a[@href="link5.html"]/../@class')
print(result)
print('--------------------------------')
#文本内容获取
html = etree.parse('./XPath1.py',etree.HTMLParser())
result =html.xpath('//li[@class="item-0"]//text()')
print(result)

