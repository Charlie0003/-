# 文件名: 39.for_in循环.py
# 开发时间: 2022/6/22 19:59
for item in 'Python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5):
    print('青叶很可爱')

sum=0
for i in range(1,101):
    if not(bool(i%2)):
        sum+=i
print('总和：',sum)