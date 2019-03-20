# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字符串中，分别输出奇数坐标字符或偶数坐标字符，奇数坐标的一行，偶数坐标的一行

sentence = "asdfghjkl12345678907"
sentence_odd = ""       # 偶数坐标字符
sentence_even = ""      # 奇数坐标字符

for i in range(len(sentence)):
    if i % 2 == 0:
        sentence_odd += sentence[i]
    elif i % 2 != 0:
        sentence_even += sentence[i]

print(sentence_odd)
print(sentence_even)
