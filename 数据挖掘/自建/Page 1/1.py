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

from collections import defaultdict
# Now compute for all possible rules
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(int)

'''
为了计算所有规则的置信度和支持度，首先创建几个字典，用来存放计算结果。这里使用
defaultdict，好处是如果查找的键不存在，返回一个默认值
sample 为 X 的数值

#特征索引值、支持度字典、置信度字典以及特征列表。
'''
for sample in X:
    for premise in range(len(features)):
        if sample[premise] == 0: continue
        # Record that the premise was bought in another transaction
        num_occurences[premise] += 1
        for conclusion in range(len(features)):
            if premise == conclusion:  # It makes little sense to measure if X -> X.
                continue
            if sample[conclusion] == 1:
                # This person also bought the conclusion item
                valid_rules[(premise, conclusion)] += 1
            else:
                # This person bought the premise, but not the conclusion
                invalid_rules[(premise, conclusion)] += 1
support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurences[premise]


#次循环所有商品俩个的支持程度
#for premise, conclusion in confidence:
def print_rule(premise, conclusion, support, confidence, features):
                #特征索引值、支持度字典、置信度字典以及特征列表。
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print("Rule:如果一个人买了{0} 他们也买了{1}".format(premise_name,conclusion_name))
    print("-支持度-Support:{0}".format(support[(premise,conclusion)]))
    print("-confidence-置信度：{0:.3f}".format(confidence[(premise,conclusion)]))
    print("置信度的百分比函数{0:.1f}%.".format(100 * confidence[(premise,conclusion)]))
print_rule(3, 4, support, confidence, features)

