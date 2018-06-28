#robots.txt  实例   爬虫协议   机器人协议
# User-agent:*
# Disallow:/
# Allow:/public/
# User-agent:Baiduspider
# set_url()，用来设置 robots.txt 文件的链接。如果已经在创建 RobotFileParser 对象时传入了链接，那就不需要再使用这个方法设置了。
# read()，读取 robots.txt 文件并进行分析，注意这个函数是执行一个读取和分析操作，如果不调用这个方法，接下来的判断都会为 False，所以一定记得调用这个方法，这个方法不会返回任何内容，但是执行了读取操作。
# parse()，用来解析 robots.txt 文件，传入的参数是 robots.txt 某些行的内容，它会按照 robots.txt 的语法规则来分析这些内容。
# can_fetch()，方法传入两个参数，第一个是 User-agent，第二个是要抓取的 URL，返回的内容是该搜索引擎是否可以抓取这个 URL，返回结果是 True 或 False。
# mtime()，返回的是上次抓取和分析 robots.txt 的时间，这个对于长时间分析和抓取的搜索爬虫是很有必要的，你可能需要定期检查来抓取最新的 robots.txt。
# modified()，同样的对于长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和分析 robots.txt 的时间。
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'https://www.jianshu.com/p/11046c89367d'))
# print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
print('----------------------------------------------------------------------------------')
rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

