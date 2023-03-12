# 文件名: 115.object类.py
# 开发时间: 2022/7/11 21:57
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)

stu=Student('张三',20)
print(dir(stu))
print(stu)
print(type(stu))