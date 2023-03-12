# 文件名: 131.文件对象的常用方法.py
# 开发时间: 2022/7/15 20:40
# file=open('a.txt','r')
# print(file.read())
# print(file.readline())
# print(file.readlines())
'''
file=open('b.txt','a')
file.write('hello')
lst=['Java','Python']
file.writelines(lst)
file.close()
'''
'''
file=open('a.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()
'''
file=open('a.txt','a')
file.write('hello')
file.flush()
file.write('world')
file.close()