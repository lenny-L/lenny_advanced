# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 10:24
# @Author  : lenny
# @File    : super_func.py

# class A(object):
#     def add(self, x):
#         y = x + 1
#         print(y)
#
#
# class B(A):
#     def add(self, x):
#         super().add(x)
#
#
# b = B()
# b.add(2)


# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print("parent")
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild, self)首先找到FooChild的父类，然后把类FooChild的对象转换为类FooParent的对象
#         super(FooChild, self).__init__()
#         print("Child")
#
#     def bar(self, message):
#         super(FooChild, self).bar(message)
#         print("Child bar function")
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar("hello, world!")


class A(object):
    def __init__(self):
        print("enter A")
        print(self)  # this will print <__main__.D object at 0x...>
        print("leave A")


class B(A):
    def __init__(self):
        print("enter B")
        print(self)  # this will print <__main__.D object at 0x...>
        super(B, self).__init__()
        print("leave B")


class C(A):
    def __init__(self):
        print("enter C")
        print(self)  # this will print <__main__.D object at 0x...>
        super(C, self).__init__()
        print("leave C")


class D(B, C):
    pass


d = D()
