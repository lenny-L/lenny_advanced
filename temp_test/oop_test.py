# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 14:27
# @Author  : chenp
# @File    : oop_test.py


class A(object):
    name = "hello"

    @staticmethod
    def sing():
        print("我是谁，为了谁")


a = A()
a.sing()
b = print("hello,world")
print(b)
print(a.name)
