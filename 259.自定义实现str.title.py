# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.title() 每个单词首字母大写

import string


def title(sentance):
    result_list = []
    for word in sentance.split():
        if word[0] in string.ascii_lowercase:
            first_letter = word[0]
            first_letter = chr(ord(first_letter) - 32)
            result_list.append(first_letter + word[1:])
    return " ".join(result_list)


print(title("acv ddghj sdsd"))