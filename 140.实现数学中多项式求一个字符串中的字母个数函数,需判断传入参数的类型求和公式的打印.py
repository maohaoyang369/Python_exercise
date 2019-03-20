# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 求一个字符串中的字母个数函数，需判断传入参数的类型
# isinstance(s,str)，加个要求，必须使用ascii来判断是否字母

import string


def letter_num(s):
    if not isinstance(s, str):
        return None
    count = 0
    for i in s:
        if i in string.ascii_letters:
            count += 1
    return count


print("包含的字母有：", letter_num("124ertyu"), "个")
