#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/6/29
# Desc  : 设计一个算法，计算出n阶乘中尾部零的个数,11! = 39916800，因此应该返回 2
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        sum = 0
        while n != 0:
            n//=5
            sum += n
        return sum