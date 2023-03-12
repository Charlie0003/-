# 文件名: 72.集合的相关操作.py
# 开发时间: 2022/6/29 21:30
s={10,20,30,40,50}
# 判断操作
print(10 in s)
print(10 not in s)
print(10 in s)
print(100 not in s)
# 新增操作
s.add(80)   #一个
print(s)
s.update({100,200,300})    # 至少一个
print(s)
s.update([2000,3000])
s.update((56,390,29,218))
print(s)
# 删除操作
s.remove(100)
print(s)
#s.remove(500)  KeyError: 500
s.discard(500)
s.discard(300)
s.pop() # 不能添加参数
print(s)
s.clear()
print(s)