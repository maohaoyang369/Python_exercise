# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一下首字母为"a"的单词 s = "I am a boy!"

s = "I am a boy!"
s = s.split()
result = ""

for i in s:
    if i[0] == "a":
        result += i

print(result)
