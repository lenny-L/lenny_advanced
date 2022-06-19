# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 11:01
# @Author  : chenp
# @File    : test.py
class CLanguage():

    def __init__(self):
        hobbit = "eat"
        self.name = "test XX"
    # 定义__call__方法
    def __call__(self, name, add):
        print("调用__call__()方法", name, add)
        print(self.name)
    print("test YY")


clangs = CLanguage()
# clangs("hello, word", "test")
clangs.__call__("hello", "world")

