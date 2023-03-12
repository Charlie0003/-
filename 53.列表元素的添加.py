# 文件名: 53.列表元素的添加.py
# 开发时间: 2022/6/26 19:08
# append 添加1个元素在末尾
lst=[10,20,30]
print(lst,id(lst))
lst.append(40)
print(lst,id(lst))
# expend 添加至少1个元素在末尾
lst2=['hello','world']
lst.extend(lst2)
print(lst)
# insert 添加1个元素在任意位置
lst.insert(1,90)
print(lst)
# 切片 添加至少1个元素在任意位置
lst3=[True,False,'hello']
lst[1:]=lst3
print(lst)

