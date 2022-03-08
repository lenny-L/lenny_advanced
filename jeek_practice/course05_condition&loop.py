# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 10:59
# @Author  : chenp
# @File    : course05_condition&loop.py


# name_price: 产品名称(str)到价格(int)的映射字典
# name_color: 产品名字(str)到颜色(list of str)的映射字典
# for name, price in name_price.items():
#     if price >= 1000:
#         continue
#     if name not in name_color:
#         print('name: {}, color: {}'.format(name, 'None'))
#         continue
#     for color in name_color[name]:
#         if color == 'red':
#             continue
#         print('name: {}, color: {}'.format(name, color))

# Exercises
attributes = ['name', 'dob', 'gender']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male'],
    ['nancy', '2001-02-01', 'female']
]
l1 = []
for value in values:
    d = {}
    for i in range(3):
        d[attributes[i]] = value[i]
    l1.append(d)
l2 = [dict(zip(attributes, value)) for value in values]  # 精简版
print(l2)