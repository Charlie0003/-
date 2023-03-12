# 文件名: 86.字符串的编码与解码.py
# 开发时间: 2022/7/2 22:23
s='青叶'
# 4-8:编码
# GBK:一个中文占两个字符
print(s.encode(encoding='GBK'))
# UTF-8:一个中文占三个字符
print(s.encode(encoding='UTF-8'))
# 9-:解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))