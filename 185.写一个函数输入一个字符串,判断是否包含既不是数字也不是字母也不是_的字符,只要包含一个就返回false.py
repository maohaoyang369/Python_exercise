# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数输入一个字符串，判断是否包含 既不是数字也 不是字母 也不是_ 的字符，只要包含一个就返回false

import string


def special(chars):
    for i in chars:
        if i not in "0123456789_" and i not in string.ascii_letters:
            return False


print(special("12345sfdsdf_"))
print(special("12345s$%^&"))
