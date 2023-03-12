# 文件名: 89.函数的参数传递.py
# 开发时间: 2022/7/4 20:23
# 如果是可变对象，在函数体的修改不会影响实参的值
# 如果是不可变对象，在函数体的修改会影响实参的值
def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)
n1=10
n2=[20,30,40]
print('n1=',n1)
print('n2=',n2)
fun(n1,n2)
print('n1=',n1)
print('n2=',n2)