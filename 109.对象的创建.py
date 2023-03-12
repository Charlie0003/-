# 文件名: 109.对象的创建.py
# 开发时间: 2022/7/9 21:23
class Student:
    # 类属性
    native_place='上海'
    def __init__(self,name,age):
        # 实例属性
        self.name=name
        self.age=age
    # 方法
    def eat(self):
        print(123)
    # 静态方法
    @staticmethod
    def mathod():
        print('staticmethod修饰')
    # 类方法
    @classmethod
    def cm(cls):
        print('classmethod修饰')

stu1=Student('张三',19)
# print(type(stu1),id(stu1),stu1)
# print(id(Student),type(Student),Student)
stu1.eat()
print(stu1.name)
print(stu1.age)
Student.eat(stu1)