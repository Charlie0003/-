# 文件名: 110.类属性，类方法，静态方法使用方式.py
# 开发时间: 2022/7/10 21:01
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

# 类属性
# print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='北京'
print(stu1.native_place)
print(stu2.native_place)
# 类方法
Student.cm()
# 静态方法
Student.mathod()