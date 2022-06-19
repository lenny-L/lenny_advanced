# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 9:25
# @Author  : lenny
# @desc    :

import threading
import time


def set_telephone(telephone):
    local.telephone = telephone
    print(threading.current_thread().name + " 放入的手机是", local.telephone + "\n")
    time.sleep(1)
    get_telephone()


def get_telephone():
    print(threading.current_thread().name + " 取出的手机是", local.telephone + "\n")


if __name__ == '__main__':
    local = threading.local()
    for i in range(3):
        thread = threading.Thread(target=set_telephone, name='学生' + str(i), args=('手机' + str(i),))
        thread.start()
