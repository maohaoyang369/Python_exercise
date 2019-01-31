#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一下字母个数

sentence = "I am a 19 years old boy! 666!"


def total_letters(s):
    if not isinstance(s,str):
        print("the parameter is not a unicode string! ")
        return 0
    result = 0
    for i in s:
        if chr(65) <= i <= chr(123):
            result += 1
    return result


print(total_letters(sentence))