# 文件名: 90.函数的返回值.py
# 开发时间: 2022/7/4 20:46
'''
1.如果函数没有返回值[函数执行完毕后，不需要给调用处提供数据]
  return可以省略，是否需要返回值，视情况而定
2.函数的返回值，如果是一个，直接返回类型
3.函数的返回值，如果是多个，返回结果为元组
'''
def fun(num):
    jishu=[]
    oushu=[]
    for i in num:
        if i%2==0:
            oushu.append(i)
        else:
            jishu.append(i)
    return jishu,oushu
lst=[10,29,34,23,44,53,55]
print(fun(lst))