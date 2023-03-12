# 文件名: 84.字符串切片.py
# 开发时间: 2022/7/2 12:58
s='hello,Python'
s1=s[:5]
s2=s[6:]
s3='!'
news=(s1+s3+s2)
print(news)
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(news))
print(s[1:5:1])
print(s[::2])
print(s[::-1])
print(s[-6::1])