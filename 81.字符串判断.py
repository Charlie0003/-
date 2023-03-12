# 文件名: 81.字符串判断.py
# 开发时间: 2022/6/30 20:18
s='hello,python'
# isidentifier 是否合法为合法标识符
print(s.isidentifier())
print('hello'.isidentifier())
print('张三_'.isidentifier())
print('python_123'.isidentifier())
# isspace 是否都是空白字符
print(',''\t'.isspace())
# isalpha 是否都是英文字母(abc,中文）
print('abc'.isalpha())
print('张三'.isalpha())
print('张三1'.isalpha())
# isdecimal 是否全部由十进制组成(非罗马，中文一二三)
print('123'.isdecimal())
# isnumeric 是否全部由十进制组成(罗马，中文一二三)
print('123四'.isnumeric())
# isalnum 是否全部由数字，字母组成
print('张三123'.isalnum())
print('!'.isalnum())