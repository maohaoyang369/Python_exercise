# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，如果传入的是list，且list长度大于3，只保留前3个元素并返回


def judge(list_sentance):
    if isinstance(list_sentance, list) and len(list_sentance) > 3:
        return list_sentance[0:3]
    else:
        return False


print(judge([1, 2, 3, 4, 5, 6, 7]))
print(judge(123))
