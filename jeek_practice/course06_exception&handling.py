# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 10:54
# @Author  : chenp
# @File    : course06_exception&handling.py


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except ValueError as err:
    print('Value Error: {}'.format(err))
# except (ValueError, IndexError) as err:  # 多个异常捕获1
#     print('Error: {}'.format(err))
# except ValueError as err:  # 多个异常捕获2
#     print("Value Error: {}".format(err))
# except IndexError as err:
#     print("IndexError Error: {}".format(err))
except Exception as err:  # 捕获所有非上述异常
    print('other Error: {}'.format(err))
except:
    print('other Error')

print('continue')

# import sys
# try:
#     f = open('file.txt', 'r')
# except OSError as err:
#     print('OS error: {}'.format(err))
# except:
#     print('Unexpected error:', sys.exc_info()[0])
# finally:  # 无论如何都会执行finally，哪怕上述有return
#     f.close()


# 用户自定义异常
class MyInputError(Exception):
    """..."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)
except MyInputError as err:
    print("error: {}".format(err))


# 使用场景：不确定某个代码块是否能正确运行
# 能用流程控制的不要用异常处理
