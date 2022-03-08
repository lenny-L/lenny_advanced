# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 19:14
# @Author  : lenny
# @desc    :

def test(data):
    try:
        print(data)
        try:
            print("222")
            # raise OSError("TEST ERROR")
            # print("test")
        except Exception as e:
            print("hello1")
        print("yyy")
        raise IOError("xxx")
            # raise IOError("test error")
    except Exception as e:
        print("hello2")


if __name__ == '__main__':
    test(111)

#