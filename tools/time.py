import time
import datetime


def today_zero_time():
    """
    Returns the time of today at midnight.
    """
    # return int(time.mktime(time.strptime(time.strftime("%Y-%m-%d"), "%Y-%m-%d")))
    dt = datetime.datetime.now()
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(time.mktime(dt.timetuple()))


def last_week_last_day_time():
    """
    Returns the time of the last day of the last week. 注意是上周日0点的时间戳
    """
    dt = datetime.datetime.now()
    # print(dt.weekday())
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(time.mktime(dt.timetuple())) - 86400 * dt.isoweekday()


def last_month_last_day_time():
    """
    Returns the time of the last day of the last month.
    """
    dt = datetime.datetime.now()
    dt = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    # print(dt)
    # print(time.mktime(dt.timetuple()))
    return int(time.mktime(dt.timetuple())) - 86400
