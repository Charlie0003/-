# 文件名: 95.递归函数.py
# 开发时间: 2022/7/5 21:59
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))