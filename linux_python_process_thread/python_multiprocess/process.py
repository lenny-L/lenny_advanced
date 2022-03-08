# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 17:02
# @Author  : lenny
import multiprocessing
import time


def worker(interval):  # 单进程函数
    n = 5
    while n > 0:
        print("The time is {}".format(time.ctime()))
        time.sleep(interval)
        n -= 1


def worker_1(interval):
    print("worker_1")
    time.sleep(interval)
    print("end worker_1")


def worker_2(interval):
    print("worker_2")
    time.sleep(interval)
    print("end worker_2")


def worker_3(interval):
    print("worker_3")
    time.sleep(interval)
    print("end worker_3")


if __name__ == '__main__':  # 进程p调用start()时，自动调用run()
    # p = multiprocessing.Process(target=worker, args=(3,))
    p1 = multiprocessing.Process(target=worker_1, args=(2,))
    p2 = multiprocessing.Process(target=worker_2, args=(3,))
    p3 = multiprocessing.Process(target=worker_3, args=(4,))
    p1.start()
    p2.start()
    p3.start()
    # print("p.pid:", p.pid)
    # print("p.name:", p.name)
    # print("p.is_alive:", p.is_alive())
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print("END")


# Linux进程间通信：https://www.jianshu.com/p/c1015f5ffa74
# 进程间通信IPC主要方式-Python实现：https://juejin.cn/post/6883700723079446535#heading-0
