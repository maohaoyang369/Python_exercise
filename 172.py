# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个字符串的奇数坐标的字母拼成一个字符串

sentence = "qwertygfds"
sentence_list = []
for i in range(len(sentence)):
    if i % 2 == 1:
        sentence_list.append(sentence[i])

print("".join(sentence_list))
