# 文件名: 67.什么是元组.py
# 开发时间: 2022/6/29 20:43
# 可变序列  列表和字典
lst=[10,20,45]
print(id(lst))
lst.append(200)
print(id(lst))
# 不可变序列 字符串和元组
s='hello'
print(id(s))
s=s+'world'
print(id(s))
print(s)