#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 倒序取出每个单词的第一个字母，I am a good boy！

sentence = "I am a good boy !"
sentence = sentence.replace("!", " ")
letter = []
letter_reverse = ""
for i in sentence.split()[::-1]:
    # print(i)
    letter.append(i[0])
print(letter)