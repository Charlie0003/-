# 文件名: 45.二重循环break continue.py
# 开发时间: 2022/6/23 16:33
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()