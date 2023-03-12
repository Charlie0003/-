# 文件名: 96.斐波那契数列.py
# 开发时间: 2022/7/5 22:10
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

for i in range(1,7):
    print(fib(i))