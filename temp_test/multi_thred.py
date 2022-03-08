# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 17:34
# @Author  : lenny
# @desc    :

from concurrent.futures import ThreadPoolExecutor
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


start_time = time.time()
# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50)
time.sleep(3)
# 判断future1代表的任务是否结束
while future1.done():
    print "total time: ", time.time() - start_time - 3
    # 查看future1代表的任务返回的结果
    print(future1.result())
    # 关闭线程池
    pool.shutdown()
