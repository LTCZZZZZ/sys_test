import jwt
import time

secretKey = '3X85VZJIwQMQOqqN95bN'
baseShareUrl = 'https://easyv.cloud/workspace/shareScreen/eyJzY3JlZW5JZCI6NTI5OTQwfQ'

payload = {
    "limit": 1,  # 只允许访问一次
    "exp": int(time.time()) + 30 * 60   # 30分钟过期
}

token = jwt.encode(payload, secretKey, algorithm="HS256")
URL = baseShareUrl + '?_easyv_token=' + token
print("大屏链接: ", URL)
