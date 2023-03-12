# 文件名: 108.定义Python中的类.py
# 开发时间: 2022/7/9 21:10
# 类名称首字母大写，其余小写
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

# print(id(Student),type(Student),Student)