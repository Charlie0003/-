# 文件名: 62.字典的增删改.py
# 开发时间: 2022/6/28 18:03
scores={1:985,2:211,3:0}
print(1 in scores)
print(2 not in scores)

del scores[3]
print(scores)
# scores.clear()
# print(scores)
scores[3]=985
print(scores)
scores[3]=211
print(scores)
