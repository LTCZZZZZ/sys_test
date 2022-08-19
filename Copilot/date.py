import datetime
import time

# 获取两个日期之间的天数
def get_days(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return (date2 - date1).days


print(get_days('2019-01-01', '2020-01-02'))


# 获取两个日期之间的所有日期字符串
def get_days_list(date1, date2):
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    days = []
    while date1 <= date2:
        days.append(date1.strftime('%Y-%m-%d'))
        date1 += datetime.timedelta(days=1)
    return days


print(get_days_list('2019-01-01', '2020-01-02'))
