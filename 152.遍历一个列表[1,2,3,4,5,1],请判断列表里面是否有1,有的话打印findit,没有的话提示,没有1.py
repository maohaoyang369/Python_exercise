# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 遍历一个列表[1,2,3,4,5,1]，请判断列表里面是否有1，有的话打印find it,没有的话提示，没有1

sentence = [1, 2, 3, 4, 5]
is_break = False
for i in sentence:
    if not isinstance(i, (int, float)):
        print("None")
    elif i == 1:
        print("find it!")
        break
    elif i != 1:
        is_break = True

if is_break:
    print("没有1")
