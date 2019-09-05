# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1


def rfind(sentance, str, beg=None, end=None):
    if beg == None:
        beg = 0
    if end == None:
        end = len(sentance)
    for i in range(len(sentance)):
        if i <= end and i >= beg:
            if (sentance[i:i+len(str)] == str) and (i+len(str) <= end):
                return i
    return -1


print(rfind("abcdefr", "cde", 2, 10))
print(rfind("abcdefr", "cde", 3))
print(rfind("abcdefr", "cde"))
