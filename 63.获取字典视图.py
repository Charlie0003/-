# 文件名: 63.获取字典视图.py
# 开发时间: 2022/6/28 18:08
scores={1:985,2:211,3:0}
keys=scores.keys()
print(keys,type(keys))
print(list(keys))

values=scores.values()
print(values,type(values))
print(list(values))

items=scores.items()
print(items,type(items))
print(list(items))