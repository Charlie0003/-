# 文件名: 65.字典的特点.py
# 开发时间: 2022/6/28 19:59
# key 不允许重复
d={0:'kitty',0:'nora'}
print(d)
# value 可以重复
d={0:'kitty',100:'kitty'}
print(d)
# 字典是无序的
lst=[10,20,30]
lst.insert(1,100)
print(lst)
# key必须是不可变
'''
d={lst:100}
print(d)
'''
