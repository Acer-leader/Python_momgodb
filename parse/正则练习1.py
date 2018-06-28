import re
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>
'''

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
if  result:
    print(result.group())
    print(result.group(1),result.group(2))
print('------------------------------------------------------')

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
if results:
    #print(result1)
    for result in results:
        #print(result)
        print(result[1],result[2])

content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    #print(result)
    print(result[1])
print('------------------------------')
html = re.sub('<a.*?>|</a>|<i.*?>|</i>','',html)
results = re.findall('<li.*?>(.*?)</li>',html,re.S)
print(html)
for result in results:
    print(result.strip())

print('-----------------------------------')

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
#创造对象  compile  编译封装。
pattern = re.compile('\d{2}:\d{2}')
print(re.sub(pattern,'',content1),re.sub(pattern,'',content2),re.sub(pattern,'',content3))






