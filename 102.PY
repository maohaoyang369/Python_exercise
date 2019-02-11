#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一下非字母和非数字的个数

sentence = "I am a 19 years old boy! 666!"


def total_num(s):
    if not isinstance(s, str):
        print("the parameter is not a unicode string! ")
        return 0
    result = 0
    for i in s:
        if i in "0123456789":
            result += 1
    return result


def total_letters(s):
    if not isinstance(s, str):
        print("the parameter is not a unicode string! ")
        return 0
    result = 0
    for i in s:
        if chr(65) <= i <= chr(123):
            result += 1
    return result


def count_no_letters_num(s):
    count = len(s)
    return count-(total_letters(s)+total_num(s))


print(count_no_letters_num(sentence))