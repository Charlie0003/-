# 文件名: 80.字符串的劈分.py
# 开发时间: 2022/6/30 19:16
# split 从左侧开始劈
s='hello world Python'
lst=s.split()
print(lst)
s1='hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

# rsplit 从右侧开始劈
print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit(sep='|',maxsplit=1))