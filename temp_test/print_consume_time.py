# encoding = utf-8

import time


# def run():
#     start = time.time()
#     for i in range(1000):
#         j = i * 2
#         for k in range(j):
#             t = k
#             print(t)
#     end = time.time()
#     print('程序执行时间: ', end - start)
#
# run()

def run2():
    start = time.clock()
    for i in range(1000):
        j = i * 2
        for k in range(j):
            t = k
            # print(t)
    end = time.clock()
    print('CPU执行时间: ', end - start)


run2()
