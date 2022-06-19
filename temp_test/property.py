# -*- coding: utf-8 -*-
# @Time    : 2022/4/22 10:24
# @Author  : lenny
# @desc    : 将一个方法伪装成为属性


# 一、@property装饰器


class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age.deleter
    def age(self):
        print("删除年龄数据！")


obj = People("jack", 18)
print(obj.age)  # 获取值
obj.age = 19  # 重新赋值
print("obj.age: ", obj.age)
del obj.age  # 删除属性


# 二、property()方法


class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    def del_age(self):
        print("删除年龄数据！")

    # 核心在这句
    age = property(get_age, set_age, del_age, "年龄")


obj = People("jack", 18)
print(obj.age)
obj.age = 19
print("obj.age:  ", obj.age)
del obj.age
