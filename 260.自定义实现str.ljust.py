# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.ljust(numbe)  左对齐


def ljust(sentance, number):
    len_sentance = len(sentance)
    if len_sentance < number:
        sentance += " " * (number-len_sentance)
    return sentance, len(sentance)


print(ljust("abc", 7))