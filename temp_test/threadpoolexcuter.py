# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 10:30
# @Author  : chenp
# @File    : threadpoolexcuter.py
import time
from concurrent.futures.thread import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
