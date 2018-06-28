#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print (i, " 是素数")
    i = i + 1

print ("Good bye!")

num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)

'''
break 用法

'''
print ("--------------------")
for name in 'Wanghui':
    if name == 'h':
        break
    print('是我的姓：',name)

var = 10
while var > 0:
    print ('当前变量值:',var)
    var = var -1
    if var == 5:
        break

print ('Good Bye')


'''
去除满足条件的某些东西

'''
for i in range(0,10):
    if i%2 == 0:
        continue
    print ('0-10的奇数为：',i)
print ('Good Bye')


print ('----------------------------')

import random

math = random.randrange(0,100)
print (math)
if math>0 and math<65:
    for math in range(0,65):
        if math > 45:
            break
    print ('你获得的积分是800')
elif math<99 and math>=65:
    print('你得到现金红包为20')
elif math ==100:
    print ('得到金鼎一个')
print ('' \
      '' \
      '')
print ('谢谢参与')



"""
pass
语句的描述
"""
for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)

print ("Good bye!")

'''
number  数字类型

'''
var = 1
var2 = 10
var3 = 20
print (var)
print (var2)
del (var2)


"""
数学函数
"""
print (abs(10))


tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "A","b","c","d"
tup1 = ()
tup1 = (50,)


a = len(tup2)
print (a)

'''
python 的日期和时间

'''

# 引入时间模块
import time

ticks = time.time()

print ("当前时间:",ticks)

localtime = time.localtime(time.time())

print ("本地时间为:",localtime)

#格式化后的时间

localtime = time.asctime(time.localtime(time.time()))

print ("本地时间为:",localtime)
'''
定义函数  以及回调函数
'''
def printme(str):
    "打印字符串"
    print (str)
    return

printme("我要调用自己定义的函数")
printme("再次调用函数")

print ("---------------------")
total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
# 调用sum函数
sum(10, 20);
print ("函数外是全局变量 : ", total)
'''
类
'''
print ('------------------------------------------')
class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name:",self.name, ",Salary:",self.salary)


emp1 = Employee("王辉",10000000)

emp1.displayCount()
emp1.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


emp1.age = 7
print (emp1.age)
del emp1.age
print ('---------------------------------')
def print_two(*args):
 arg1, arg2 = args
 print ("arg1: %r, arg2: %r" % (arg1, arg2))
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
 print ("arg1: %r, arg2: %r" % (arg1, arg2))
# this just takes one argument
def print_one(arg1):
 print ("arg1: %r" % arg1)
# this one takes no arguments
def print_none():
 print ("I got nothin'.")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

print ('-----------------------------------------------------------------------------')

def cheese_and_crackers(cheese_count, boxes_of_crackers):
 print ("You have %d cheeses!" % cheese_count)
 print( "You have %d boxes of crackers!" % boxes_of_crackers)
 print ("Man that's enough for a party!")
 print ("Get a blanket.\n")
print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print ("------------------------------------------------------------------------")
class A(object):
    pass
if __name__ == '__main__':
    a = A()
    b = A()
    print (id(a) == id(b))
    print (a,b)

print ("------------------------------------------------------------------------")

import math
def Acer(str,math):
    for W in str and math == random(0,10):
        if W or math:
            print ("是真实的：",W)

print (Acer(str,8))

