# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计“You are ,a beautifull Girl,666! ”中数字和字母的总个数

import string

sentance = "You are ,a beautifull Girl,666!"
result_letter_num = 0
result_num = 0

for i in sentance:
    if i in string.ascii_letters:
        result_letter_num += 1
    if i in "01234567890":
        result_num += 1

print("字母个数为：", result_letter_num)
print("数字个数为：", result_num)
