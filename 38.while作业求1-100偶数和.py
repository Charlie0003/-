# 文件名: 38.while作业求1-100偶数和.py
# 开发时间: 2022/6/22 19:46
#sum为总和，i为偶数
sum=0
i=1
while i<101:
    if not bool(i%2):
        sum+=i
    i+=1
print('总和:',sum)