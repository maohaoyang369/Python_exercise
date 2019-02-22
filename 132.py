# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 找出一段句子中最长的单词及其索引位置，以字典返回

# import string

sentence = "This is a beautiful city"
result = {}
max_length_str = ""
word_length = 0
sentence_list = sentence.split()
for i in sentence_list:
    if len(i) > word_length:
        max_length_str = i
        word_length += len(i)
for j in range(len(sentence)):
    # print(sentence[10:(10+9)])
    if max_length_str == sentence[j:(j + len(max_length_str))]:
        print("最长单词的位置是 " + str(j))

# print(max_length_str)
# print(sentence_list)
# print(sentence)
