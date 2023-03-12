# 文件名: 78.字符串大小写转换.py
# 开发时间: 2022/6/30 18:32
s='hello,python'
# 全部转成大写(upper)
a=s.upper()
print(s,id(s))
print(a,id(a))
# 全部转成小写(lower)
b=s.lower()
print(s,id(s))
print(b,id(b))
print(b==s)
print(b is s)
# 大写转小写，小写转大写(swapcase)
s2='hello,Python'
print(s2.swapcase())
# 每个英语单词开头大写,其他小写(title)
print(s2.title())
# 第一个字符转为大写,其他小写(capitalize)
print(s2.capitalize())