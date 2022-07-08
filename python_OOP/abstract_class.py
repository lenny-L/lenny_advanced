# -*- coding: utf-8 -*-
# @Time    : 2022/7/8 9:36
# @Author  : lenny
# @desc    : 功能妙用待具体实践

import abc


class File(metaclass=abc.ABCMeta):  # abc.ABCMeta是实现抽象类的一个基础类

    @abc.abstractmethod
    def read(self):
        pass


class Txt(File):  # 子类继承抽象类，但是必须定义read方法将抽象类中的read方法覆盖

    def read(self):
        print("hello")


txt1 = Txt()
txt1.read()
txt2 = File()
txt2.read()
