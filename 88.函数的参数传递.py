# 文件名: 88.函数的参数传递.py
# 开发时间: 2022/7/4 20:11
# 位置实参
#   形参
def plus(a,b):
    c=a+b
    return c
#   实参值
resurt=plus(10,20)
print(resurt)

# 关健实参
res=plus(b=20,a=10)
print(res)
