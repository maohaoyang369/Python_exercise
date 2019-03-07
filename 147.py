# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入5个字母，声明一个可变参数的函数，拼成一个单词


def sentance(*arg):        # 可变参数
    # print(type(arg))        # 类型是元组
    result = ""
    for i in arg:
        result += i
    return result


print(sentance("1", "2", "3", "4", "5"))
