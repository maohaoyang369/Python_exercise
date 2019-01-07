#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 判断一个字符串是否为回文字符串
# 所谓回文字符串，就是一个字符串，从左到右读和从右到左读是完全一样的。比如"level" 、 “aaabbaaa”

sentence = "level"

revers_sentence = sentence[::-1]

if sentence == revers_sentence:
    print("是回文字符串")
else:
    print("不是回文字符串")