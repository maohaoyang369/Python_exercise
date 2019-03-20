#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成列表[“a”,”c”,”e”,”g”,”i”]

import string

letters = string.ascii_letters[0:9]
result = []

for i in range(0, len(letters), 2):
    result.append(letters[i])

print(result)
