# 处理毫秒或微秒级时间戳
import time
from datetime import datetime

timestr = '2019-01-14 15:22:18.123'
datetime_obj = datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f")
ret_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)

print(datetime_obj.timestamp())
print(ret_stamp)
