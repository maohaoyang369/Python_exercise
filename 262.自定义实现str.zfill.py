# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.zfill(numbe) 用0将字符填充到指定长度


def zfill(sentance, number):
    len_sentance = len(sentance)
    add_zero = number-len_sentance
    if number <= len_sentance:
        return sentance, len(sentance)
    else:
        result = ("0" * add_zero) + sentance
    return result, len(result)


print(zfill("abc", 4))
