# 文件名: 32.分支结构 多分支结构.py
# 开发时间: 2022/6/21 17:39
score=int(input('请输入成绩'))
if score>=90 and score<=100:  #score>=90 and score<=100可以换成90<=score<=100
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('非法数据，无效')