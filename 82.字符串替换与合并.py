# 文件名: 82.字符串替换与合并.py
# 开发时间: 2022/7/1 20:49
# replace(a,b,c) a:指定替换子串 b:替换子串的字符串(新字符串) c:最大替换次数
s='hello,python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',3))
# join(a) 将元组或列表字符串合并
lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))
t=('hello','java','Python')
print(''.join(t))
print('*'.join('Python'))