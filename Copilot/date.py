import datetime


# 获取两个日期之间的天数
def get_days_between(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    return (date2 - date1).days


print(get_days_between('2019-01-01', '2019-02-02'))


# 获取两个日期之间的所有日期，返回datetime类型
def get_days_between_datetime(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    days = (date2 - date1).days
    return [date1 + datetime.timedelta(days=i) for i in range(days + 1)]


print(get_days_between_datetime('2019-01-01', '2019-02-02'))
