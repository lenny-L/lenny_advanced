# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 10:56
# @Author  : lenny
# @desc    :


# 预置知识：python的代码是从上到下执行，函数定义是不会执行的，调用时才会执行
# 作用：为被装饰的对象增加新的功能或者附加限制条件或者帮助输出
def outer(func):
    def inner():
        print("我是内层函数！")

    return inner


def foo():
    print("我是原始函数！")


outer(foo)  # inner
outer(foo)()  # inner()
outer(foo())  # 先执行foo()，然后inner
outer(foo())()  # 先执行foo()，然后执行inner()

print "<---1--->"


def outer(func):
    def inner():
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result

    return inner


@outer
def f1():
    print("业务部门1的数据接口......")


f1()
"""
语法规则：
1. 被装饰的函数的名字会被当作参数传递给装饰函数
2. 装饰函数(如:inner)执行它自己内部的代码后，会将它的返回值赋值给被装饰的函数

@outer等于outer(f1), f1-->outer(f1)-->inner, 故f1() == inner()
f1这个函数名更改成指向inner这个函数名指向的函数体内存地址，f1不再指向它原来的函数体的内存地址; func保存了老的函数f1在内存中的地址
"""


# 不封装一层会导致f1还未被调用就已经执行了, 因为@outer f1==outer(f1)==return result==func()
# def outer(func):
#     print("认证成功！")
#     result = func()
#     print("日志添加成功")
#     return result
#
#
# @outer
# def f1():
#     print("业务部门1数据接口......")
print "<---2--->"


def outer(func):
    def inner(*args, **kwargs):
        print("执行前...")
        func(*args, **kwargs)
        print("执行后...")

    return inner


@outer
def test(a, b):
    print(a)
    print(b)


test(1, {"hello": 222})
print "<---3--->"


# 多个装饰
def outer1(func):
    def inner(*args, **kwargs):
        print("认证成功！")
        result = func(*args, **kwargs)
        print("日志添加成功")
        return result

    return inner


def outer2(func):
    def inner(*args, **kwargs):
        print("一条欢迎信息。。。")
        result = func(*args, **kwargs)
        print("一条欢送信息。。。")
        return result

    return inner


@outer1
@outer2
def f1(name, age):
    print("{}正在连接业务部门{}数据接口......".format(name, age))


f1("jack", 18)
print "<---4--->"


# 自带参数的装饰器
# 认证函数
def auth(request, kargs):
    print("---认证成功！")


# 日志函数
def log(request, kargs):
    print("---日志添加成功")


# 装饰器函数。接收两个参数，这两个参数应该是某个函数的名字。
def Filter(auth_func, log_func):
    # 第一层封装，f1函数实际上被传递给了main_fuc这个参数
    def outer(main_func):
        # 第二层封装，auth和log函数的参数值被传递到了这里
        def wrapper(request, kargs):
            # 下面代码的判断逻辑不重要，重要的是参数的引用和返回值
            before_result = auth(request, kargs)
            if (before_result != None):
                return before_result

            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result

            after_result = log(request, kargs)
            if (after_result != None):
                return after_result

        return wrapper

    return outer


# 注意了，这里的装饰器函数有参数哦，它的意思是先执行filter函数
# 然后将filter函数的返回值作为装饰器函数的名字返回到这里，所以，
# 其实这里，Filter(auth,log) = outer , @Filter(auth,log) =  @outer
@Filter(auth, log)
def f1(name, age):
    print("%s 正在连接业务部门1数据接口......" % name)


# 调用方法
f1("jack", 18)
