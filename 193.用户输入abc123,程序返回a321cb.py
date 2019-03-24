# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 用户输入”abc123”,程序返回”a321cb”

sentence = input("Please enter sentence：")
result = sentence[0] + ""

for i in range(1, len(sentence)):
    # print(len(sentence))
    # print(sentence[0])
    result += sentence[-i]

print(result)
