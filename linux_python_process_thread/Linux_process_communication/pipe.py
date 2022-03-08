# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 11:23
# @Author  : lenny
# -*- coding: utf-8 -*-
import time
import os
import six

if six.PY2:
    six.string_types


# 1.simple example
# try:
#     pid = os.fork()
# except OSError, e:
#     pass
# time.sleep(20)


# 2.
# 创建子进程前声明的变量
# number = 7
# try:
#     pid = os.fork()
#
#     if pid == 0:
#         print("this is child process, pid: {}".format(pid))
#         number = number - 1
#         time.sleep(3)
#         print(number)
#     else:
#         print("this is parent process, pid: {}".format(pid))
#         time.sleep(3)
# except OSError as e:
#     pass


def child(wpipe):
    print('hello from child', os.getpid())
    while True:
        msg = 'how are you\n'.encode()
        os.write(wpipe, msg)
        time.sleep(1)


def parent():
    rpipe, wpipe = os.pipe()  # os.pipe()返回2个文件描述符(r, w)
    print "rpipe: {}, type: {}, wpipe: {}, type: {}".format(rpipe, type(rpipe), wpipe, type(wpipe))
    pid = os.fork()
    if pid == 0:
        os.close(rpipe)
        child(wpipe)
        assert False, 'fork child process error!'
    else:
        os.close(wpipe)
        print('hello from parent', os.getpid(), pid)
        fobj = os.fdopen(rpipe, 'r')
        while True:
            recv = fobj.readline()[:-1]
            print recv


parent()
