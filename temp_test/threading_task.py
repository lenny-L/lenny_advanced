# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 15:45
# @Author  : chenp
# @File    : threading_task.py

# import threading
# import time
#
#
# def test(i):
#     print("loop keeping... {}".format(i))
#
#
# if __name__ == '__main__':
#
#     start_time = time.time()
#     for i in range(100):
#         t = threading.Thread(target=test, args=(i,))
#         # test(i)
#     end_time = time.time()
#     print("total_time: {}".format(end_time - start_time))


import threading
import time

number = 0
lock = threading.Lock()


def plus(lk):
    global number
    lk.acquire()
    for _ in range(1000000):
        number += 1

    print("子线程%s运算结束后， number= %s" % (threading.current_thread().getName(), number))
    lk.release()


if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=plus, args=(lock,))
        t.start()
    time.sleep(2)
    print("主线程执行完毕后， number= ", number)
