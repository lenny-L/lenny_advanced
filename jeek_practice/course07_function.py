# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:33
# @Author  : chenp
# @File    : course07_function.py


# 1.note1: 定好好的函数只有调用的时候才存在哟


def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is: {}'.format(largest_element))


find_largest_element([8, 1, -3, 2, 0])


# note2: 如果在函数内部调用其他函数，函数间哪个声明在前、哪个在后就无所谓，因为 def 是可执行语句，函数在调用之前都不存在，我们只需保证调用时，所需的函数都已经声明定义
def my_func(message):
    my_sub_func(message)  # 调用my_sub_func()在其声明之前不影响程序执行


def my_sub_func(message):
    print('Got a message: {}'.format(message))


my_func('hello world')


# note3: Python 不用考虑输入的数据类型，而是将其交给具体的代码去判断执行
# 多态特性：如以下函数，可以支持传入列表、字符串、数字等，"双刃剑"-> 传入参数的类型不确定，有时必须在函数内部对其做相应的判断处理
def my_sum(a, b):
    return a + b


result = my_sum(3, 5)
print(result)

# 嵌套特性：
# 1.函数的嵌套能够保证内部函数的隐私
# 2.提高程序的效率


def f1():
    print('hello')
    def f2():
        print('world')
    f2()
f1()



def factorial(input):
    # 合法性检查只需要一次
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)


print(factorial(5))


# 2.变量的作用域
# global：声明某变量是该函数外的某全局变量
MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    global MIN_VALUE
    MIN_VALUE += 1
validation_check(5)

# nonlocal: 声明某变量是其外函数的同名变量
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()


# 3.闭包：
# 资料：https://www.cnblogs.com/yssjun/p/9887239.html
# 一个函数定义中引用了函数外定义的变量，并且该函数可以在其定义环境外被执行(就是return给了函数外部)
# 3.1 特点：闭包中的引用的自由变量只和具体的闭包有关联，闭包的每个实例引用的自由变量互不干扰
#          一个闭包实例对其自由变量的修改会被传递到下一次该闭包实例的调用
def outer_func():
    loc_list = []

    def inner_func(name):
        loc_list.append(len(loc_list) + 1)
        print('%s loc_list = %s' % (name, loc_list))

    return inner_func


clo_func_0 = outer_func()
clo_func_0('clo_func_0')
clo_func_0('clo_func_0')
clo_func_0('clo_func_0')
clo_func_1 = outer_func()
clo_func_1('clo_func_1')
clo_func_0('clo_func_0')
clo_func_1('clo_func_1')

# 3.2 闭包陷阱
# 返回闭包列表fs之前for循环的变量的值已经发生改变了，而且这个改变会影响到所有引用它的内部定义的函数。因为在函数my_func返回前其内部定义的函数并不是闭包函数，只是一个内部定义的函数
# return之前fs中的三个函数都只是定义了而并未调用，在函数外部进行调用的时候i的值已经变成了2，而非0,1,2三个不同的数值

# def my_func(*args):
#     fs = []
#     for i in range(3):
#         def func():
#             return i * i
#         fs.append(func)
#     return fs

# def my_func(*args):
#     fs = []
#     j = 0
#     for i in range(3):
#         def func():
#             return j * j
#         fs.append(func)
#     j = 3
#     return fs

# def my_func(*args):
#     fs = []
#     for i in range(3):
#         func = lambda : i * i
#         fs.append(func)
#     return fs

# correct func：将i这个赋值给内函数的形参时会保留值，Python中对于函数形参的定义值会保存在内存中
def my_func(*args):
    fs = []
    for i in range(3):
        def func(_i=i):
            return _i * _i
        fs.append(func)
    return fs


fs1, fs2, fs3 = my_func()
print(fs1())
print(fs2())
print(fs3())


# 3.3 闭包的应用
# 单例、装饰器

def func_dec(func):
    def wrapper(*args):
        if len(args) == 2:
            func(*args)
        else:
            print('Error! Arguments = %s' % list(args))
    return wrapper

@func_dec
def add_sum(*args):
    print(sum(args))

add_sum = func_dec(add_sum)
args = range(1, 3)
add_sum(*args)

# 潜在的问题
def counter(cls):
    obj_list = []
    def wrapper(*args, **kwargs):
        new_obj = cls(*args, **kwargs)
        obj_list.append(new_obj)
        print("class:%s'object number is %d" % (cls.__name__, len(obj_list)))
        return new_obj
    return wrapper

@counter
class my_cls(object):
    STATIC_MEM = 'This is a static member of my_cls'
    def __init__(self, *args, **kwargs):
        print(self, args, kwargs)
        print(self.STATIC_MEM)

my_cls_obj = my_cls()

# 闭包的实现过程
# 。。。
print("----1----")


def outer_func(hello):
    def inner_func(base):
        return hello ** base
    return inner_func

outer_obj = outer_func(2)
print(outer_obj(3))

print([(lambda x: x * x)(x) for x in range(10)])
# 输出
hello = [(lambda x: x * x) for x in range(10)]
print(hello)
