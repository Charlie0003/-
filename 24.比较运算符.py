# 文件名: 24.比较运算符.py
# 开发时间: 2022/6/17 21:53
a,b=10,20
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

a=b=10
print(a==b)
print(a is b)

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
print(a is not b)
print(lst1 is not lst2)