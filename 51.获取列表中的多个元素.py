# 文件名: 51.获取列表中的多个元素.py
# 开发时间: 2022/6/24 21:24
lst = [10, 20, 30, 40, 50, 60, 70, 80]
# print(lst[1:6:1])
print(id(lst))
lst2 = lst[1:6:1]
print(id(lst2))
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])

print(lst)
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])