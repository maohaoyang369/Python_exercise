# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一下一句话中有几个数字和几个空白，和几个字母，其他字符有几个
# "I am a 12 years old boy! hi,me!"

s = "I am a 12 years old boy! hi,me!"
count_num = 0
count_blank = 0
count_letters = 0
count_others = 0

for i in s:
    if i.isalpha():
        count_letters += 1
    elif i.isdigit():
        count_num += 1
    elif i.isspace():
        count_blank += 1
    else:
        count_others += 1

print(count_num)
print(count_blank)
print(count_letters)
print(count_others)
