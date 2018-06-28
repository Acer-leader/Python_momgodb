#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)

c += a
print ("2 - c 的值为：", c)

c *= a
print ("3 - c 的值为：", c)

c /= a
print ("4 - c 的值为：", c)

c = 8
c%=a
print ("5 - c 的值为：", c)

c **= a
print ("6 - c 的值为：", c)

c //= a
print ("7 - c 的值为：", c)



print ('------------------------------------')

L = [1,2,4,32,8,64,128,16,9]

x = 5
found = False
i =0
while not found and i < len(L):
    if 2 **5 == L[i]:
        found = True
    else:
        i = i+1
    if found:
         print ('at index',i)
    else:
         print (x,'not found')

