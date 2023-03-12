# 文件名: 123.模块的导入.py
# 开发时间: 2022/7/13 21:01
'''
import math
print(id(math))
print(type(math))
print(math)
print(math.pi)
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001))
print(math.floor(9.9999))
'''
'''
from math import pi
from math import pow
print(pi)
print(pow(2,3))
''''''
import calc
print(calc.add(1,2))
'''
from calc import add
print(add(1,2))