# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 10:57
# @Author  : lenny
# @desc    :


class DB(object):
    def __init__(self, name):
        print(f"this is __init__")
        self.name = name

    def __enter__(self):
        print(f"__enter__: {self.name}.open")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_tb)
        print(f"__exit__: {self.name}.close; exception: {exc_val}")


def logic():
    with DB("mysql") as mq, DB("postgres") as pg:
        print(f"exec in {mq.name}")
        print(f"exec in {pg.name}")
        raise Exception("logic error")


logic()

# first: init
# second: enter
# third: code
# fourth: exit
# final: exception
