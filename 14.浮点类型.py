# 文件名: 14.浮点类型.py
# 开发时间: 2022/6/17 11:26
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))