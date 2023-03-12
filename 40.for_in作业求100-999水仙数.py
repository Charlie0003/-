# 文件名: 40.for_in作业求100-999水仙数.py
# 开发时间: 2022/6/22 20:56
# 水仙花数153=1*1*1+5*5*5+3*3*3
for item in range(100,3000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    #print(bai,shi,ge)
    if ge**3+shi**3+bai**3==item:
        print(item)