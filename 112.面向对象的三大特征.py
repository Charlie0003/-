# 文件名: 112.面向对象的三大特征.py
# 开发时间: 2022/7/10 21:31
'''
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动')
car=Car('宝马*5')
car.start()
print(car.brand)
'''
# 封装
class Student:
    def __init__(self,name,age):
        self.name=name
        # __不希望在外部使用
        self.__age=age
    def show(self):
        print(self.name,self.__age)
stu=Student('张三',20)
stu.show()
print(stu.name)
# print(stu.__age)
print(dir(stu))
print(stu._Student__age)