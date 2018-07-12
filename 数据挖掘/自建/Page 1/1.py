#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/7/12
# Desc  : 亲和性分析示例
import numpy as np
dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
print(X[:5])


features = ["bread", "milk", "cheese", "apples", "bananas"]
num_apple_people = 0
for num in X:
    if num[3] == 1:  # 说明这个人买了苹果 就是 1
        num_apple_people += 1
print("{0}个人买了苹果" .format(num_apple_people))

num_apple_bananas_rule = 0
num_bananas_rule = 0
for num in X:
    if num[3] == 1:  # 这个人买了苹果
        if num[4] == 1: #这个人不仅买了苹果而且买了香蕉
            num_apple_bananas_rule += 1
        else:
            num_bananas_rule += 1  # 这个人只买了苹果没买香蕉
print("{0}个人买了香蕉和苹果".format(num_apple_bananas_rule))
print("{0}个人只卖了苹果".format(num_bananas_rule))

support = num_apple_bananas_rule
confidence =num_apple_bananas_rule / num_apple_people
print("支持买苹果有卖香蕉的人数{0},置信度为{1:.3f}." . format(support,confidence))
print("置信度的百分比函数{0:.1f}%.".format(100 * confidence))