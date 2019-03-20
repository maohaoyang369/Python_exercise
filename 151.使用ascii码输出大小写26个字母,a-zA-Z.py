# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用ascii码 输出大小写26个字母，a-zA-Z

lower_letters = ""
for i in range(97, 123):
    lower_letters += chr(i)

upper_letters = ""
for i in range(65, 91):
    upper_letters += chr(i)

all_letters = lower_letters + upper_letters
print(all_letters)
