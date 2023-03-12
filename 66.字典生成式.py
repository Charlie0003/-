# 文件名: 66.字典生成式.py
# 开发时间: 2022/6/28 20:09
items=['fruit','book','vegetable']
prices=[99,89,109,0,0]
d={item.upper():price   for item,price in zip(items,prices)}
print(d)