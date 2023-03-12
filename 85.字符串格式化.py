# 文件名: 85.字符串格式化.py
# 开发时间: 2022/7/2 13:17
name='张三'
age=20
# 占位符  %s:字符串 %d/%i:整数 %f:浮点数
print('我叫%s，今年%d岁' % (name,age))
# 大括号{}
print('我叫{0}，今年{1}岁'.format(name,age))
# 格式化
print(f'我叫{name}，今年{age}岁')
# %ad a:宽度
print('%10d' % 95)
print('hellohello')
# %.af a:精度
print('%.3f' % 3.1415926)
# %a.bf a:宽度 b:精度
print('%10.3f' % 3.1415926)
# ｛?:b:.af｝a:几位有效数字，如加f就是几位小数位 b:宽度
print('{0:.3}'.format())
