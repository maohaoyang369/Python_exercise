# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个字符串首字母、最后一个字母和中间字母，三个字符串拼成一个字符串

sentence = "qweriup"
sentance_list = []
sentance_list.append(sentence[0])
middle = int(len(sentence)/2)
# print(middle)
if len(sentence) % 2 == 1:
    sentance_list.append(sentence[middle])
else:
    sentance_list.append(sentence[middle-1])
sentance_list.append(sentence[-1])
print("".join(sentance_list))
