#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Pycharm.
# User: y1wanghui@163.com
# Date  : 2018/6/14
# Desc  :


import pytesseract as pt
from PIL import Image
image = Image.open('C:/timg.jpg')
text = pt.image_to_string(image)
print(text)