# 文件名: 54.列表元素的删除.py
# 开发时间: 2022/6/26 19:24
# remove 从列表移除第一个元素
lst=[0,10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
# pop 从列表移除指定元素
lst.pop(1)
print(lst)
lst.pop()
print(lst)
# 从列表移除至少一个元素(新列表对象）
new_list=lst[1:3]
print(new_list)
# 从列表移除至少一个元素
lst[1:3]=[]
print(lst)
# clear 清除列表中所有元素
lst.clear()
print(lst)
# del删除列表对象
del lst