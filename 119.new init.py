# 文件名: 119.new init.py
# 开发时间: 2022/7/12 21:16
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用,cls id为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用,self id为{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象id为{0}'.format(id(object)))
print('Person这个类对象id为{0}'.format(id(Person)))

p1=Person('张三',20)
print('p1这个Person类实例对象id为{0}'.format(id(p1)))
