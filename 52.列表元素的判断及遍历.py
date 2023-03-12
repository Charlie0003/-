# 文件名: 52.列表元素的判断及遍历.py
# 开发时间: 2022/6/26 19:01
print('p' in 'python')
print('m' not in 'python')

lst=[10,20,'hello','python']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)