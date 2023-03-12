# 文件名: 56.列表元素的排序.py
# 开发时间: 2022/6/26 19:46
# sort 升序
lst=[10,20,98,54,12]
print(lst)
lst.sort()
print(lst)
# reverse=True 降序
lst.sort(reverse=True)
print(lst)
# sort 升序，新列表对象
lst=[10,20,98,54,12]
new_list=sorted(lst)
print(lst)
print(new_list)
new_list2=sorted(lst,reverse=True)
print(new_list2)