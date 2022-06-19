# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 16:03
# @Author  : chenp
# @File    : class_obj.py
import dis


def test():
    class X:
        data = 100

        def get(self):
            return self.data


print(dis.dis(test))
