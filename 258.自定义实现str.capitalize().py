# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.capitalize()  第一个字母大写

import string


def capitalize(sentance):
    first_letter = sentance[0]
    if first_letter in string.ascii_lowercase:
        first_letter = chr(ord(first_letter) - 32)
    return first_letter + sentance[1:]


print(capitalize("acv ddghj,sdsd"))
