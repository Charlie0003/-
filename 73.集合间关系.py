# 文件名: 73.集合间关系.py
# 开发时间: 2022/6/29 21:43
# 元素相同
s1={10,20,30,40}
s2={40,30,20,10}
print(s1==s2)
print(s1!=s2)
# 子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s2))
# 超集
print(s1.issuperset(s2))
print(s1.issuperset(s3))
# 交集
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s2))
s4={100,200}
print(s2.isdisjoint(s4))