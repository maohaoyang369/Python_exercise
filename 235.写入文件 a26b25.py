# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写入文件 a26  b25 ...

# 方法一

with open("D:\\python\\a.txt", 'w') as fp:
    for i in range(26):
        fp.write(chr(ord("a") + i) + str(26-i) + "\n")

with open("D:\\python\\a.txt", 'r') as fp:
    print(fp.read())

# 方法二

with open("D:\\python\\a.txt", 'w+') as fp:
    for i in range(26):
        fp.write(chr(ord("a") + i) + str(26-i) + "\n")
    fp.seek(0, 0)
    print(fp.read())
