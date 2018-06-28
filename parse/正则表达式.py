import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
result1 = re.match('^[A-Z][a-z]{4}\s[0-9]{3}\s[0-9]{4}\s[A-Z][a-z]{4}\w[A-Z][a-z]{3}',content)
print(result)
print(result1.group())
print(result.group())
print(result.span())
content1 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^\D{5}\s([0-9]{7})\D{6}',content1)
print(result2.group())
print(result2.group(1))
print(result2.span(1))

print('------------------------------')

content3 = '''Hello 1234567 World_This 
is a Regex Demo'''
result3 = re.match('^He.*?(\d+).*Demo$', content3,re.S)
print(result3.group())
print(result3.group(1))
print('------------------------------')

content4 = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content4)
print(result)
print(result.group())


















