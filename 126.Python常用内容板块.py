# 文件名: 126.Python常用内容板块.py
# 开发时间: 2022/7/13 21:35
import sys
import time
import urllib.request
import math
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())
print(math.pi)