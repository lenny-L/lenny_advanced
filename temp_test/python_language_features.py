# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 17:06
# @Author  : chenp
# @File    : python_language_features.py

def foo(x):
    pass


class A(object):

    # 实例方法
    def foo(self, x):
        print("foo")
        print(x)

    # 类方法
    @classmethod
    def class_foo(cls, x):
        print("class foo, {}".format(x))

    # 静态方法
    @staticmethod
    def static_foo(x):
        print("static foo, {}".format(x))


# a = A()
# a.foo("hello")
# A.class_foo("hello")
A.static_foo("hello")
