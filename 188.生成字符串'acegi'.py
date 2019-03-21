# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成字符串"acegi”

import string

letters = string.ascii_letters[0:9]
result = ""

for i in range(0, len(letters), 2):
    result += letters[i]

print(result)
