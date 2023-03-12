# 文件名: 92.函数的参数定义.py
# 开发时间: 2022/7/4 21:19
def fun(*args):
    print(args)
    print(args[0])
fun(10)
fun(10,29)
fun(10,29,38)

def fun1(**args):
    print(args)
fun1(a=10)
fun(a=20,b=30,c=40)