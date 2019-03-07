# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用ascii码 输出小写26个字母，a-z

lower_letters = ""
for i in range(97, 123):
    lower_letters += chr(i)
print(lower_letters)
