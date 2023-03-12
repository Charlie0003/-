# 文件名: 101.bug被动掉坑.py
# 开发时间: 2022/7/6 21:26
try:
    a=int(input('请输入一个整数'))
    # ValueError: invalid literal for int() with base 10: 'a'
    b=int(input('请输入一个整数'))
    # ZeroDivisionError: division by zero
    result=a/b
    print(result)
except ZeroDivisionError:
    print('除数不为0')
except ValueError:
    print('只能输数字')
print('程序结束')