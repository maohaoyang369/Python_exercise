#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成字符串：a1b2c3d4.....j10

result = ""
for i in range(1,11):
    result += chr(i+96) +str(i)
print(result)

# 生成字符串： AaBbCcDd.....Zz

letters = ""
for s in range(65,65+26):
    letters += chr(s)+chr(s+32)
print(letters)

# 输出奇数小写字母和偶数小写字母到两个列表中

even_num =[]
odd_num =[]
for i in range(97,97+26):
    if i%2 == 0:
        even_num += chr(i)
    elif i%2 == 1:
        odd_num += chr(i)
print(even_num)
print(odd_num)