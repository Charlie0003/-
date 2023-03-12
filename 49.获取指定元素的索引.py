# 文件名: 49.获取指定元素的索引.py
# 开发时间: 2022/6/24 18:09
# index(a,b,c) a:第一个与他一样的索引 b,c:从b到c不包括c中寻找
lst=['hello','world',98,'hello']
print(lst.index('hello'))
# print(lst.index('Python'))
# print(lst.index('hello',1,3))
print(lst.index('hello',1,4))