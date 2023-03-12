# 文件名: 41.break流程控制语句.py
# 开发时间: 2022/6/23 13:00
'''
for item in range(3):
    pwd=input('请输入密码')
    if pwd=='123456':
        print('密码正确')
        break
    else:
        print('密码错误')
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