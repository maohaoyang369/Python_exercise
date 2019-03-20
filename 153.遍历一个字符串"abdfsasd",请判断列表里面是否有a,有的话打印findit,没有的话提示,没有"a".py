# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 遍历一个字符串"abdfsasd"，请判断列表里面是否有a，有的话打印find it,没有的话提示，没有"a"

sentence = "abdfsasd"
is_break = False
for i in sentence:
    if i == "a":
        print("find it!")
        break
    elif i != "a":
        is_break = True

if is_break:
    print("没有a")
