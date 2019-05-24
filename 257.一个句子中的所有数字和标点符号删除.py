# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个句子中的所有数字和标点符号删除

import string

s = "i am a boy, my age is 19 years ."
result = ""

for i in s:
    # print(i)
    if i not in string.punctuation and i not in string.digits:
        result += i

print(result)
