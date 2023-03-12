# 文件名: 44.循环嵌套.py
# 开发时间: 2022/6/23 15:40
'''
print()
for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')
    print()
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t') #'*',end='\t'
    print()