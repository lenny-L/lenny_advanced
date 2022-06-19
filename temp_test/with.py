# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:15
# @Author  : chenp
# @File    : with.py
"""
with语句：https://juejin.cn/post/6844903694937374733
"""

class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("进入")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type=None, exc_val=None, exc_tbs=None):
        print("退出")
        self.f.close()


if __name__ == '__main__':
    with File('file.txt', 'w') as f:
        print("正在写入...")
        f.write('Hello')
