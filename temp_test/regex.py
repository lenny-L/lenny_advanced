# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 17:36
# @Author  : lenny
# @desc    :

# !/usr/bin/env python
# coding=utf-8

import re

string = '3\8'
m = re.search('(\d+)\\\\', string)

if m is not None:
    print m.group(1)  # 结果为：3

string_temp = "C:\\Promram Files (x86)\\info2soft\\n"
x = re.search('\\\\', string_temp)
if x is not None:
    print x

n = re.search(r'(\d+)\\', string)

if n is not None:
    print n.group(1)  # 结果为：3
