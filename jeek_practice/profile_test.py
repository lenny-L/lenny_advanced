# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 18:19
# @Author  : chenp
# @File    : profile_test.py

import python_performance_analysis


def a():
    sum = 0
    for i in range(1, 10001):
        sum += i
    return sum


def b():
    sum = 0
    for i in range(1, 100):
        sum += a()
    return sum


if __name__ == "__main__":
    python_performance_analysis.run("b()")
