# -*- coding: utf-8 -*-
# @Time    : 2022/3/25 9:13
# @Author  : lenny
# @desc    :


def test():
    try:
        1 > 2
        raise
    except Exception as e:
        print("hello")
        raise
    finally:
        a = 1 + 2
        print("world", a)


test()

try:
    a = "mystr"
    if (not a.isdigit()):
        raise ValueError("这里出错")
except ValueError as e:
    print("有异常发生")
    raise Exception
else:
    print("执行 else 块中的代码")
finally:
    print('welcome, world1!')
    print('welcome, world2!')
    print('welcome, world3!')
    print('welcome, world4!')
