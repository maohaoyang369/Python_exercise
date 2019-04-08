# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个字典，key 是26个小写字母a-z，value是她的acsii码

letter_dic = {}

for i in range(97, 97+26):
    letter_dic[chr(i)] = i

print(letter_dic)
