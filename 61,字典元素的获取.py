# 文件名: 61,字典元素的获取.py
# 开发时间: 2022/6/28 17:57
scores={1:985,2:211,3:0}
# [a] get(a) 找到索引为a的
print(scores[2])
print(scores.get(2))
print(scores.get(4))
print(scores.get(4,-1))