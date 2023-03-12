# 文件名: 94.变量的作用域.py
# 开发时间: 2022/7/4 22:06
def fun(a,b):
    # a,b,c 为局部变量
    c=a+b
    print(c)

# print(c,a)

# name 为全局变量
name='张三'
def fun2():
    print(name)
fun2()

def fun3():
    global age
    age=20
    print(age)
fun3()
print(age)