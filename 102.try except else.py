# 文件名: 102.try except else finally.py
# 开发时间: 2022/7/6 21:38
try:
    a=int(input('请输入一个整数'))
    # ValueError: invalid literal for int() with base 10: 'a'
    b=int(input('请输入一个整数'))
    # ZeroDivisionError: division by zero
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('结果为',result)
finally:
    print('谢谢您的使用')