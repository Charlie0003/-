# 文件名: 33.分支结构 嵌套if.py
# 开发时间: 2022/6/21 17:55
answer=input('你是会员吗?y/n')
money=float(input('请输入您的购物金额'))
if answer=='y':
    if money>=200:
        print('8折',money*0.8)
    elif money>=100:
        print('9折',money*0.9)
    else:
        print('不打折',money)
else:
    if money>=200:
        print('9.5折',money*0.95)
    else:
        print('不打折',money)