# 文件名: 127.第三方模块使用.py
# 开发时间: 2022/7/13 21:46
import schedule
import time
def job():
    print('哈哈')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)