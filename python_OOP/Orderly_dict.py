# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 9:31
# @Author  : lenny
# @desc    :

# import collections
#
# my_order_dict = collections.OrderedDict()
# my_order_dict["name"] = "lowman"
# my_order_dict["age"] = 45
# my_order_dict["money"] = 998
# my_order_dict["hourse"] = None
#
# for key, value in my_order_dict.items():
#     print(key, value)


# import collections
#
# my_order_dict = collections.OrderedDict(name="lowman", age=998, money=45, hourse=None, sex="hapi")
#
# for key, value in my_order_dict.items():
#     print(key, value)
import collections

get_url_resp = {
    "BBB": {
        "url": {
            "POST": "/v1/cascade/volume"
        },
        "fail_flag": {
            "status": "error"
        },
        "order": "abc"
    },
    "AAA": {
        "url": {
            "POST": "/v1/cascade/volume_qos"
        },
        "fail_flag": {
            "is_deleted": "1"
        },
        "order": "aac"
    },
}
# 将排序值取出来
# sort
# 将sort后的值插入到新字典，再for循环
from collections import Iterable

aaa = sorted(get_url_resp.items(), key=lambda k_v: k_v[1]['order'])
get_url_resp = collections.OrderedDict(sorted(get_url_resp.items(), key=lambda k_v: k_v[1]['order']))
print(get_url_resp)
for x, y in get_url_resp.items():
    print(x, y)
# L = [{'status': 1, 'com': 3}, {'status': 2, 'com': 6}, {'status': 5, 'com': 2}, {'status': 1, 'com': 1},
#      {'status': 1, 'com': 4}, {'status': 1, 'com': 2}]
# L.sort(key=lambda x: (x['status'], x['com']))
# L = dict(L)
# print(L)
# all_provider_flavor_statistic = {"cpu": 0, "memory": 0, "root_gb": 0}
#
# aaa = {'ali': {'root_gb': 0, 'cpu': 0, 'memory': 0}, 'hwyun': {'root_gb': 0, 'cpu': 0, 'memory': 0},
#        'tencent': {'root_gb': 0, 'cpu': 0, 'memory': 0}, 'ctyun': {'root_gb': 0, 'cpu': 0, 'memory': 0},
#        'openstack': {'root_gb': 0, 'cpu': 0, 'memory': 0}, 'vmware': {'root_gb': 0, 'cpu': 0, 'memory': 0}}
#
#
# z = aaa.copy()
# z.update(all_provider_flavor_statistic)
# print z
