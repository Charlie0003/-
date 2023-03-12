# 文件名: 76.字符串的创建与驻留机制.py
# 开发时间: 2022/6/30 17:55
# 字符串的驻留机制
a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

s1='abc%'
s2='abc%'
print(s1 is s2)