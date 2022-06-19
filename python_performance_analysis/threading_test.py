# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 10:16
# @Author  : lenny
# @desc    :
import time
import threading


# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start job')
# print('end job')
def doWaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))

t = threading.Thread(target=doWaiting)
t.start()
# 确保线程t已经启动
time.sleep(1)
print('start join')
# 将一直堵塞，直到t运行结束。
t.join()
print('end join')