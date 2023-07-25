import time
import logging
import inspect
from apscheduler.schedulers.blocking import BlockingScheduler

# 详见 https://www.cnblogs.com/zhaoyingjie/p/9664081.html

# date
# 最基本的一种调度，作业只会执行一次。它的参数如下：
# run_date(datetime | str) – 作业的运行日期或时间
# timezone(datetime.tzinfo | str) – 指定时区
# 举个栗子：
# # 2016-12-12运行一次job_function
# sched.add_job(job_function, 'date', run_date=date(2016, 12, 12), args=['text'])
# # 2016-12-12 12:00:00运行一次job_function
# sched.add_job(job_function, 'date', run_date=datetime(2016, 12, 12, 12, 0, 0), args=['text'])

# interval
# 间隔调度，参数如下：
# weeks(int) – 间隔几周
# days(int) – 间隔几天
# hours(int) – 间隔几小时
# minutes(int) – 间隔几分钟
# seconds(int) – 间隔多少秒
# start_date(datetime | str) – 开始日期
# end_date(datetime | str) – 结束日期
# timezone(datetime.tzinfo | str) – 时区
# 举个栗子：
# # 每两个小时调一下job_function
# sched.add_job(job_function, 'interval', hours=2)

# cron
# 参数如下：
# year(int | str) – 年，4
# 位数字
# month(int | str) – 月(范围1 - 12)
# day(int | str) – 日(范围1 - 31)
# week(int | str) – 周(范围1 - 53)
# day_of_week(int | str) – 周内第几天或者星期几(范围0 - 6或者mon, tue, wed, thu, fri, sat, sun)
# hour(int | str) – 时(范围0 - 23)
# minute(int | str) – 分(范围0 - 59)
# second(int | str) – 秒(范围0 - 59)
# start_date(datetime | str) – 最早开始日期(包含)
# end_date(datetime | str) – 最晚结束时间(包含)
# timezone(datetime.tzinfo | str) – 指定时区
# 举个栗子：
# # job_function将会在6,7,8,11,12月的第3个周五的1,2,3点运行
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
# # 截止到2016-12-30 00:00:00，每周一到周五早上五点半运行job_function
# sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2016-12-31')


def get_logger(logger_name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(levelname)s %(asctime)s : %(message)s', "%Y-%m-%d %H:%M:%S")
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)

    vlog = logging.getLogger(logger_name)
    vlog.setLevel(level)
    vlog.addHandler(fileHandler)

    return vlog


def func1(logger):
    # logger = get_logger(inspect.stack()[0][3], 'cron_func1.log')
    logger.warning(f"func1: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print('func1', time.strftime('%Y-%m-%d %H:%M:%S'))


def func2(logger):
    # logger = get_logger(inspect.stack()[0][3], 'cron_func2.log')
    logger.error(f"func2: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print('func2', time.strftime('%Y-%m-%d %H:%M:%S'))


def func3():
    print('func3', time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(3)
    raise Exception('func3 error')


# 注意，这个一般来说得放在函数外面，否则因为同名问题，函数会创建多个对象且无法销毁，执行n次循环会打印n的累加次日志
# 目前暂未搞清楚具体的原因机制
logger1 = get_logger('func1', 'cron_func1.log')
logger2 = get_logger('func2', 'cron_func2.log')

# for i in range(4):
#     func1()
#     func2()

scheduler = BlockingScheduler()
# 如果设定start_date可以达到让程序从整点开始运行的目的
scheduler.add_job(func1, 'interval', seconds=5, start_date='2023-07-25', args=[logger1, ])
scheduler.add_job(func2, 'interval', seconds=3, args=[logger2, ])
# scheduler.add_job(func2, 'cron', hour=0, args=[logger2, ])

# 其中一个job任务出错，不影响其他任务的执行，且在下次该执行的时间点仍会正常执行
scheduler.add_job(func3, 'cron', second=5, args=[])
# scheduler.add_job(func1, 'cron', second=0)
scheduler.start()

# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass

print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

