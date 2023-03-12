# 文件名: 93.函数参数总结.py
# 开发时间: 2022/7/4 21:41
# 形式参数
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun(10,20,30)
# 位置实参
lst=[11,22,33]
fun(*lst)
# 关键字参数
fun(a=10,b=20,c=30)
dic={'a':111,'b':222,'c':333}
fun(**dic)

def fun1(a,b=10):
    print('a=',a)
    print('b=',b)
def fun2(*args):
    print(args)
def fun3(**args2):
    print(args2)
fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)
# 从这颗星之后的参数，在函数调用时，只能采用关键字参数传递
def fun4(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
# 实参传递
# fun4(10,20,30,40)
fun4(a=10,b=20,c=30,d=40)
fun4(10,20,c=30,d=40)