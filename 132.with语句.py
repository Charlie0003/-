# 文件名: 132.with语句.py
# 开发时间: 2022/7/15 20:57
'''
with open('a.txt''r') as file:
    print(file.read())

class MyContentMgr(object):
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
    def show(self):
        print('show')
'''
with open('level_1.png','rb') as file:
    with open('copylever_1.png','wb') as file2:
        file2.write(file.read())