# 文件名: 113.面向对象的三大特征.py
# 开发时间: 2022/7/11 21:34
# 继承
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofrear):
        super().__init__(name,age)
        self.teachofrear=teachofrear

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,10)
stu.info()
teacher.info()
'''
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass
'''
