# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 14:36
# @Author  : chenp
# @File    : cron_job_1.py
import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def task():
    os.system("python3 test_job.py")


def task2():
    print("current time: {}".format(time.localtime()))
    print("this is task 2~")


def task3():
    print("this is task 3~")
    print(time.strftime("%Y-%m-%d %X",time.localtime()))


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 添加任务
    scheduler.add_job(task, 'cron', hour=16, minute=54)
    scheduler.add_job(task2, 'date', run_date='2021-07-21 16:52:22')
    scheduler.add_job(task3, 'interval', seconds=10)  # weeks=1, days=3, hours=8, minutes=20
    scheduler.start()


# cron 参数说明
# year
# int型或str，取值四位数的年份，如2020年
# month
# int型或str，取值范围为1-12月
# week
# int型或str，取值范围为第1-53周
# day_of_week
# int型或str，表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示(mon,tue,wed,thu,fri,sat,sun)
# day
# int型或str，取值范围为1-31日
# hour
# int型或str，取值范围为0-23时
# minute
# int型或str，取值范围为0-59分
# second
# int型或str，取值范围为0-59秒
# start_date
# datetime型或str，表示开始时间
# end_date
# datetime型或str，表示结束时间

