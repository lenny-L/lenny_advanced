# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 10:55
# @Author  : lenny
# @desc    : "以后在重构类的时候不需要修改构造函数，只要额外添加你要处理的函数，然后使用@classmethod即可"


class DataTest2(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, string_date):
        # 这里第一个参数是cls， 表示调用当前的类名
        year, month, day = map(int, string_date.split('-'))
        date1 = cls(year, month, day)
        # 返回的是一个初始化后的类
        return date1

    def out_date(self):
        print "year :"
        print self.year
        print "month :"
        print self.month
        print "day :"
        print self.day


r = DataTest2.get_date("2016-8-1")
r.out_date()


# 初始类：
class DataTest(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    def out_date(self):
        print "year :"
        print self.year
        print "month :"
        print self.month
        print "day :"
        print self.day


# 新增功能：
class Str2IntParam(DataTest):
    @classmethod
    def get_date(cls, string_date):
        # 这里第一个参数是cls， 表示调用当前的类名
        year, month, day = map(int, string_date.split('-'))
        date1 = cls(year, month, day)
        # 返回的是一个初始化后的类
        return date1


# 使用：
r = Str2IntParam.get_date("2016-8-1")
r.out_date()
