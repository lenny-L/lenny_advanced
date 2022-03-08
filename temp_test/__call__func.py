# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 16:56
# @Author  : chenp
# @File    : __call__func.py

class X(object):
    def __init__(self, a, b, range):
        self.a = a
        self.b = b
        self.range = range
        print("init args, a:{}, b:{}, range:{}".format(self.a, self.b, self.range))

    def __call__(self, a, b):
        self.a = a
        self.b = b
        print("__call__ with ({}, {})".format(self.a, self.b))

    def test(self, x, y):
        print("hello, {} + {}".format(x, y))
        print("a, b, range".format(self.a, self.b, self.range))

    def __del__(self, a, b, range):
        # print("a, b, range".format(self.a, self.b, self.range))
        del self.a
        del self.b
        del self.range


hello = X(1, 2, 3)
hello.test("world", "222")