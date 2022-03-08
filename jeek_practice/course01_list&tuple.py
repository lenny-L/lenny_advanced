# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 20:09
# @Author  : lenny
# @File    : course01_list&tuple.py


"""
列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）
    列表增加元素只会修改原有元素，不会创建新的列表，而元祖不可变，如要增删则会创建新的元组，
而元组是静态的，长度大小固定，无法增加删减或者改变（immutable）
"""


# l = [3, 2, 3, 7, 8, 1]
# l.index(2)
# l.reverse()
# l.sort()
# tup = (3, 2, 3, 7, 8, 1)
# tup.count(3)
# tup.index(7)
# reversed(tup)
# sorted(tup)


# 分割线

# l = [1, 2, 3]
# print(l.__sizeof__())
# tup = (1, 2, 3)
# print(tup.__sizeof__())


# import time
#
# start = time.clock()
# a = []
# for i in range(10000):
#     print(i)
# end = time.clock()
# print(end-start)


# d = {'b': 1, 'a': 2, 'c': 10}
# d_sorted_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排序
# d_sorted_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的升序排序
# print(d_sorted_by_key)
# print(d_sorted_by_value)
#
# print("hello, world!")
#
# add = lambda x, y: x + y


def handle():
    def find_product_price(products, product_id):
        for id, price in products:
            if id == product_id:
                return price
        return None

    products = [
        (143121312, 100),
        (432314553, 30),
        (32421912367, 150)
    ]

    print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))

    # 输出
    # The
    # price
    # of
    # product
    # 432314553 is 30

    # list version
    def find_unique_price_using_list(products):
        unique_price_list = []
        for _, price in products:  # A
            if price not in unique_price_list:  # B
                unique_price_list.append(price)
        return len(unique_price_list)

    products = [
        (143121312, 100),
        (432314553, 30),
        (32421912367, 150),
        (937153201, 30)
    ]
    print('number of unique price is: {}'.format(find_unique_price_using_list(products)))

    # set version
    def find_unique_price_using_set(products):
        unique_price_set = set()
        for _, price in products:
            unique_price_set.add(price)
        return len(unique_price_set)

    products = [ (143121312, 100), (432314553, 30), (32421912367, 150), (937153201, 30)]
    print('number of unique price is: {}'.format(find_unique_price_using_set(products)))
    # 输出number of unique price is: 3

    import time
    id = [x for x in range(0, 100000)]
    price = [x for x in range(200000, 300000)]
    products = list(zip(id, price))

    # list version time
    start_using_list = time.perf_counter()
    find_unique_price_using_list(products)
    end_using_list = time.perf_counter()
    print("time elapse using list: {}".format(end_using_list - start_using_list))
    # time elapse using list: 83.92836947739124

    # set version time
    start_using_set = time.perf_counter()
    find_unique_price_using_set(products)
    end_using_set = time.perf_counter()
    print("time elapse using set: {}".format(end_using_set - start_using_set))
    # time elapse using set: 0.015320159494876862


if __name__ == '__main__':
    handle()