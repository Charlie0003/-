# 文件名: 130.常用文件打开模式.py
# 开发时间: 2022/7/14 21:29
'''
file=open('c.txt','w')
file.write('Python')
file.close()
'''
'''
file=open('c.txt','a')
file.write('Python')
file.close()
'''
scr_file=open('level_1.png','rb')
target_file=open('ll.png','wb')
target_file.write(scr_file.read())
target_file.close()
scr_file.close()