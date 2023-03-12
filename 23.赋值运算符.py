# 文件名: 23.赋值运算符.py
# 开发时间: 2022/6/17 21:31
i=3+4
print(i)
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)
a/=3
print(a,type(a))
a//=2
print(a,type(a))
a%=3
print(a)

a,b,c=20,30,40
print(a,b,c)

a,b=10,20
print(a,b)
a,b=b,a
print(a,b)