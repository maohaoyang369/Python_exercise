# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将['a','b','M','N']，将所有小写字母变为大写字母，大写字母变为小写字母["A","B","m","n"]

import string

lower_letter = ['a', 'b', 'M', 'N']
upper_letter = ["A", "B", "m", "n"]
result_upper = []
result_lower = []

for i in lower_letter:
    result_upper.append(i.upper())

for j in upper_letter:
    result_lower.append(j.lower())

print(result_upper)
print(result_lower)
