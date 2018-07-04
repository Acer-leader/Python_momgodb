
import random

def Math(a,b):
    if a > b and a > 40:
        print(a+b)
    else:
        print(b-a)
x = random.randint(1,100)
y = random.randint(1,100)
print(x,y)
if x > y and x > 40:
    print('计算加法运算')
else:
    print('计算减法运算')
    Math(x,y)
print('----------------------------')
print('运算计算完毕')
print('----------------------------')
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) + "*" +str(j) + "=" + str(i*j)+"        ")
    print('   ')



import re
pat = "yue"
string = "http://yum.iqianyue.com"
print(re.search(pat,string))



print('这是acer \"的问候.')

list = [0,11,2,3,4,5,6,7]
print(list[:5])








































