#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 简单字符加密，输入字母向后取四位


a = input("please write letters:")
b = ""
for i in a:
    if (i >= 'a' and i < 'w') or (i >= 'A' and i < 'W'):
        b += chr(ord(i)+4)
    elif i >= 'w' and i <= 'z':
        b += chr(ord(i)-ord('w')+98)
    elif i >= 'W' and i <= 'Z':
        b += chr(ord(i)-ord('W')+65)
    else:
        print("some content is not letter,please try again")
print(b)