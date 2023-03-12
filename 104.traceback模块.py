# 文件名: 104.traceback模块.py
# 开发时间: 2022/7/7 22:07
import traceback
try:
    print(10/0)
except:
    traceback.print_exc()