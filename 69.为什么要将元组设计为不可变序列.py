# 文件名: 69.为什么要将元组设计为不可变序列.py
# 开发时间: 2022/6/29 21:08
t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

t[1].append(40)
print(t,id(t[1]))