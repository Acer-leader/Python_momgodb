#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/6/11
# Desc  :


#包含一个 student类 一个sayhellow 函数 打印语句
class Student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0} " .format(self.name))

def sayHello():
    print('Hi')

print('我是01,叫我干毛')