# 文件名: 117.特殊属性.py
# 开发时间: 2022/7/12 20:56
# print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
x=C('Jack',20)
print(x.__dict__)
print(C.__dict__)
print(x.__class__)
print(C.__bases__)
print(C.__base__)
print(C.__mro__)
print(A.__subclasses__())