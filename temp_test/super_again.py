# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 15:45
# @Author  : lenny
# @desc    :
# class A:
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         print('self is {0} @A.add'.format(self))
#         self.n += m
#
#
# class B(A):
#     def __init__(self):
#         self.n = 3
#
#     def add(self, m):
#         print('self is {0} @B.add'.format(self))
#         super().add(m)
#         self.n += 3
#
#
# b = B()
# b.add(2)
# print(b.n)


def test():
    data = [1, 2, 3]
    # data = []
    return data and data[0] or None


a = test()
print(a)
