#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，统计一下一句话中的数字个数

sentence = "I am a 19 years old boy! 666!"


def total_num(s):
    if not isinstance(s,str):
        print("the parameter is not a unicode string! ")
        return 0
    result = 0
    for i in s:
        if i in "0123456789":
            result += 1
    return result


print(total_num(sentence))