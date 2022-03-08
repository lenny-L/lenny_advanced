# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 17:57
# @Author  : chenp
# @File    : jicheng.py


class A():

    aaa = "hello"

    def sing(self):
        print("我会唱歌")


class B(A):

    bbb = "world"

    def sing(self):
        print("我会跳舞")


b = B()
b.sing()
print(b.aaa)