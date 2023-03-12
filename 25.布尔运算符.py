# 文件名: 25.布尔运算符.py
# 开发时间: 2022/6/17 22:10
a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b<2)

print(a==1 or b==2)
print(a==1 or b!=2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

f1=True
f2=False
print(not f1)
print(not f2)

s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)