# 文件名: 120.类的浅拷贝.py
# 开发时间: 2022/7/13 20:23
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
# 变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
# 类对象的浅拷贝
disk=Disk()
computer=Computer(cpu1,disk)
import copy
print(disk)
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)