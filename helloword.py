# print(bool(-123))
#
# print(bool(0))
#
# print(bool('abc'))
#
# print(bool('False'))
#
# print(bool(''))

# eg2:
# num = 10
# print('Guess what I think?')
# answer = int(input())
#
# if answer < num:
#     print('too small!')
#
# if answer > num:
#     print('too big!')
#
# if answer == num:
#     print('BINGO!')

# eg3:
# from 模块名 import 方法名
# from random import randint
# num = randint(1, 100)
# print(num)

# eg4:字符串输出
# print('''
#
# Stay hungry,
#
# stay foolish.
#
#              -- Steve Jobs
#
# ''')
#
# print("""
# \\\\_v_//
# """)
#
# print("this is the\
# same line")

# eg5:拼接字符串
# print('My age is' + str(18))
# print('Price is %.2f' % 4.99)

# eg6:嵌套
# for i in range(0, 5):
#     for j in range(0, i+1):
#         print('*', end=' ')
#     print()

# eg7:自定义函数
# def myFun():
#     print("myFun")
#
# myFun()

# eg8:
# a = ""
# b = "hell"
# c = (True and [a] or [b])[0]
# print(c)
# print(dir(c))

# eg9:
# import re
# 匹配出所有s(不区分大小写)开头，e结尾的单词
# str="site sea sue sweet See case sse ssee loses"
# # # res=re.findall(r"\b[sS]\S*?e\b",str)
# # # print(res)

# 写出能识别一下格式电话号码的正则表达式
# (021)88776543
# 010-55667890
# 02584453362
# 0571 66345673

# import re
# data=[]
# data.append("(021)88776543")
# data.append("010-55667890")
# data.append("02584453362")
# data.append("0571 66345673")
# for vlaue in data:
#     res=re.findall(r"^[\(|\d]{1}\d{2,3}\)?\s?\-?\d{8}$",vlaue)
#     print(res)

# 用字典类型替代list类型
# data={}
# data[0]="(021)88776543"
# data[1]="0571 66345673"
# for i in data:
#     print(data[i])

# eg10:序列化
# #
#
# import pickle
# import pprint
#
# info = [1, 2, 3, 'abc', 'ilovepython']
# print('原始数据：')
# pprint.pprint(info)
#
# data1 = pickle.dumps(info)
# data2 = pickle.loads(data1)
#
# print("序列化：%r" % data1)
# print("反序列化： %r" % data2)
#
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])
#
# t = (1,)
# print(t.__len__())
# print(len(t))

# eg:11
import os

a=os.path.join("osFile.csv")
print(a)

with open(a,'w') as wr:
    wr.write("123,456,789")
    wr.write("asd,def,ter")
datas=list()
with open(a,'r') as re:
    datas=re.read()

print(datas)

import csv

with open(a,'w') as f:
    w=csv.writer(f,delimiter=',')
    w.writerow([1,2,3])
    w.writerow(datas)