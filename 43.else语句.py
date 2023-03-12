# 文件名: 43.else语句.py
# 开发时间: 2022/6/23 13:21
'''
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='123456':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次密码均输入错误')
'''

a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='123456':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1
else:
    print('三次密码均输入错误')