# 文件名: 17.类型转换int str.py
# 开发时间: 2022/6/17 12:54
name='张三'
age=20

print(type(name),type(age))
print("我叫"+name+',今年'+str(age)+'岁')

a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))
print(int(f1),type(int(f1)))
print(int(ff),type(int(ff)))

s1='128.98'
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
print(float(i),type(float(i)))