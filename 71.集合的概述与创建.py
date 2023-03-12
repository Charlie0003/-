# 文件名: 71.集合的概述与创建.py
# 开发时间: 2022/6/29 21:18
# 使用花括号
s={2,3,4,5,5,6,7,8,7}
print(s)

# set()
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,4,5,4,5,6,7,4,2,1])
print(s2,type(s2))
s3=set((1,2,3,32,212))
print(s3,type(s3))
s4=set('python')
print(s4,type(s4))
s5=set({12,3,4,21,431,2})
print(s5,type(s5))
s6=set()
print((s6),type(s6))