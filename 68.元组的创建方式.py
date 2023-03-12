# 文件名: 68.元组的创建方式.py
# 开发时间: 2022/6/29 20:53
# 使用小括号
t=('pyton','world',98)
print(t,type(t))
t2='pyton','world',98
print(t2,type(t2))
t3=('python',)

# 内置函数tuple
t1=tuple(('pyton','world',98))
print(t1,type(t1))

# 空元组创建方式
lst=[]
lst1=list()

dic={}
dic1=dict()

t4=()
t5=tuple()
print(lst,lst1)
print(dic,dic1)
print(t4,t5)