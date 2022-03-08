# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 17:06
# @Author  : lenny
# @File    : course03_str.py

# 一、基本概念


### 二、常见操作函数
# strip()
# split()
# find()


### 三、格式化
# %
# .format()

import time

start_time = time.perf_counter()
s = ''
for n in range(0, 100000):
    s += str(n)

end_time = time.perf_counter()
print("total time1: {}".format(end_time - start_time))

start_time = time.perf_counter()
# s = ''
# for n in range(0, 100000):
#     s += str(n)

l = []
for n in range(0, 100000):
    l.append(str(n))

s = ' '.join(l)
end_time = time.perf_counter()
print("total time2: {}".format(end_time - start_time))

