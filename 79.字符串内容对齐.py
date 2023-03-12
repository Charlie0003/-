# 文件名: 79.字符串内容对齐.py
# 开发时间: 2022/6/30 18:52
s='hello,python'
# center(a,b) 左右填充b,左边优先，宽度小于原字符则原样输出
print(s.center(20,'*'))
print(s.center(10,'*'))
# ljust(a,b) 右填充
print(s.ljust(20,'*'))
print(s.ljust(10,'*'))
# rjust(a,b) 左填充
print(s.rjust(20))
print(s.rjust(10))
# zfill(a) 左,用0填充
print(s.zfill(20))
print(s.zfill(10))
print('-8989'.zfill(8))