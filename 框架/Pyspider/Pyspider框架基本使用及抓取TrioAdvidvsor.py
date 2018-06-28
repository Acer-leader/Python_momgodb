#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/6/14
# Desc  :


import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
try:
  sk.connect(('www.sharejs.com',5000))
  print ('Server port 80 OK!')
except Exception:
  print ('Server port 80 not connect!')
sk.close()
