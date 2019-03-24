# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 用户输入一个内容，判断里面是否包含了数字

num_input = input("Please enter the sentance：")
is_break = True

for i in num_input:
    if i in "0123456789":
        print("含有数字")
        is_break = False
        break

if is_break:
    print("没有数字")
