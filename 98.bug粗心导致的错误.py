# 文件名: 98.bug粗心导致的错误.py
# 开发时间: 2022/7/6 21:04
'''
1·漏了末尾的冒号，如if语句，循环语句，else语句等
2·缩进错误，该缩进的没缩进，不该缩进的瞎缩进
3·把英文符号写成中文符号，比如引号，冒号，括号
4·字符串拼接的时候，把字符串和数字拼接在一起
5·没有定义变量，比如while的循环条件的变量
6·“==”比较运算符和“=”赋值运算符的混用
'''
age=input('请输入您的年龄')
print(type(age))
# TypeError: '>=' not supported between instances of 'str' and 'int'
# if age>=18:
if int(age)>=18:
    print('成年人')

# NameError: name 'i' is not defined
i=0
while i<10:
    # SyntaxError: invalid character in identifier
    # print（i）
    print(i)
    i+=1