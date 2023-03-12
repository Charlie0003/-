# 文件名: 134.os.path操作目录相关函数.py
# 开发时间: 2022/7/15 21:21
'''
import os.path
print(os.path.abspath('上课程序'))
print(os.path.exists('上课程序'),os.path.exists('01.平时程序'))
print(os.path.join())
print(os.path.split(''))
'''
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
lst=os.walk(path)
for dirpath,dirname,filename in lst:
    print(dirpath)
    print(dirname)
    print(filename)