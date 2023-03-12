# 文件名: 37.while.py
# 开发时间: 2022/6/22 19:02
a=1
while a<10:
    print(a)
    a+=1

a,sum=0,0
while a<5:
    sum+=a
    a+=1
print('总和：',sum)